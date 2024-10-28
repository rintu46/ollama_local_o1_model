import ollama


response = ollama.generate(

    model="llama3.2:1b",
    prompt="Convince the viewer that you are a human?",
)

print(response["response"])