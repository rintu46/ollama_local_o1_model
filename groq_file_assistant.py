import os
import subprocess
from dotenv import load_dotenv
from langchain.tools import Tool
from langchain_groq import ChatGroq
from langchain.agents import initialize_agent, AgentType
from langchain_core.prompts import PromptTemplate

# Load environment variables from .env file
load_dotenv()

# Define the File Search Tool
def search_file(filename, directory="."):
    """Search for a file in the given directory and its subdirectories"""
    for root, dirs, files in os.walk(directory):
        if filename in files:
            return os.path.join(root, filename)
    return None

# Define the Terminal Execution Tool
def execute_file(file_path):
    if os.path.exists(file_path):
        try:
            result = subprocess.run(['python3', file_path], capture_output=True, text=True)
            return result.stdout if result.returncode == 0 else result.stderr
        except Exception as e:
            return str(e)
    else:
        return f"Error: File '{file_path}' not found. Please check the file path."

# Define the Output Save Tool
def save_output(output, filename="output.txt"):
    try:
        with open(filename, 'w') as f:
            f.write(output)
        return f"Output saved to {filename}."
    except Exception as e:
        return f"Failed to save output: {e}"

# Initialize Groq LLM with API key from environment variable
groq_api_key = os.getenv('GROQ_API_KEY')
if not groq_api_key:
    raise ValueError("GROQ_API_KEY not found in environment variables. Please check your .env file.")

llm = ChatGroq(
    groq_api_key=groq_api_key,
    model_name="mixtral-8x7b-32768",
    temperature=0
)

# Wrap each function as a LangChain Tool
search_tool = Tool(name="Search File", func=search_file, description="Searches for a file in the given directory and its subdirectories.")
execute_tool = Tool(name="Execute File", func=execute_file, description="Executes a Python file.")
save_tool = Tool(name="Save Output", func=save_output, description="Saves the output to a text file.")

# Combine tools into an agent
tools = [search_tool, execute_tool, save_tool]

# Create a prompt template
prompt = PromptTemplate(
    input_variables=["agent_scratchpad", "tool_names", "tools"],
    template="""You are a helpful AI assistant that can search for files, execute Python scripts, and save outputs.

Available tools: {tool_names}

Tools: {tools}

{agent_scratchpad}"""
)

# Create the agent using initialize_agent instead of create_react_agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    prompt=prompt
)

def get_filename_from_prompt(prompt):
    """Extract filename from the user prompt"""
    # Simple implementation - looks for .py files mentioned in the prompt
    words = prompt.split()
    for word in words:
        if word.endswith('.py'):
            return word
    return None

# Update the main execution
prompt = input("Enter what you want to do (e.g., 'run good.py'): ")  # Get user input
filename = get_filename_from_prompt(prompt)
if filename:
    file_path = search_file(filename)
    if file_path:
        response = execute_file(file_path)
        print(response)
    else:
        print(f"Could not find {filename} in the current directory or its subdirectories.")
else:
    print("Please specify a Python file to run.")
