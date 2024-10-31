# Python File Management and Execution Tool

## Overview
This tool provides a simple way to find and run Python files on your computer. It uses artificial intelligence (through Groq LLM) to help understand and execute your commands.

## Step-by-Step Installation Guide for Beginners

### Step 1: Install Python
1. Go to [Python's official website](https://www.python.org/downloads/)
2. Click on "Download Python" (choose the latest version for your operating system)
3. Run the downloaded installer
   - For Windows: Make sure to check "Add Python to PATH" during installation
   - For Mac: Double click the downloaded .pkg file and follow the instructions
   - For Linux: Python usually comes pre-installed

### Step 2: Verify Python Installation
1. Open your computer's terminal/command prompt
   - Windows: Press Windows key + R, type "cmd" and press Enter
   - Mac: Press Command + Space, type "terminal" and press Enter
   - Linux: Press Ctrl + Alt + T
2. Type `python --version` or `python3 --version`
3. If you see a version number (like "Python 3.x.x"), the installation was successful

### Step 3: Install Required Packages
1. Open terminal/command prompt
2. Copy and paste these commands one by one:
```bash
pip install langchain==0.2.27
pip install langchain-groq
pip install langgraph==0.2.1
pip install python-dotenv
```

3. Verify the installations by running:
```bash
pip list | grep langchain
pip list | grep langgraph
pip list | grep python-dotenv
```

### Step 4: Set Up Environment Variables
1. Create a file named `.env` in the same directory as mmh.py
2. Open the `.env` file in a text editor
3. Add your Groq API key in this format:
```
GROQ_API_KEY=your_api_key_here
```
4. Save and close the `.env` file
5. Make sure not to share your `.env` file with others

### Step 5: Running the Tool
1. Download all the project files to a folder on your computer
2. Open terminal/command prompt
3. Navigate to the folder containing mmh.py:
   - Windows: `cd path\to\your\folder`
   - Mac/Linux: `cd path/to/your/folder`
4. Run the script:
   ```bash
   python mmh.py
   ```
   or
   ```bash
   python3 mmh.py
   ```

### Step 6: Using the Tool
1. When prompted, type what you want to do. For example:
   - `run good.py` (to run a Python file named good.py)
2. The tool will:
   - Search for the file
   - Execute it if found
   - Show you the output

## Common Commands and Examples

### Example 1: Running a Python File
```bash
Enter what you want to do: run good.py
```

### Example 2: What to Do if File is Not Found
If you see "File not found":
1. Make sure the file exists in your folder
2. Check if you typed the filename correctly
3. Verify the file has .py extension

## Troubleshooting Guide

### Common Issues and Solutions

1. **"Python not found" error**
   - Solution: Reinstall Python and make sure to check "Add to PATH"

2. **"Package not found" error**
   - Solution: Run these commands:
     ```bash
     pip install --upgrade pip
     pip install langchain langchain-groq
     ```

3. **"Permission denied" error**
   - Windows: Run Command Prompt as Administrator
   - Mac/Linux: Use `sudo python3 mmh.py`

4. **API Key Issues**
   - Verify your Groq API key is correct
   - Make sure you've replaced the default key in the code

## Features in Detail
- **File Search**: Automatically finds Python files in your folder and subfolders
- **File Execution**: Runs Python files and shows their output
- **Output Saving**: Can save results to a text file
- **AI Integration**: Uses Groq AI to understand your commands

## Support
If you need help:
1. Check this troubleshooting guide
2. Verify all installation steps
3. Make sure all files are in the correct folder

## System Requirements
- Any operating system (Windows/Mac/Linux)
- Python 3.6 or newer
- Internet connection (for AI features)
- Minimum 4GB RAM recommended

## Safety Notes
- Only run Python files that you trust
- Keep your API key private
- Don't share mmh.py with your API key inside

## Updates and Maintenance
- Check regularly for updates
- Keep Python and all packages updated
- Update your API key if needed

This tool is designed to make running Python files easier, even for beginners. If you encounter any issues, follow the troubleshooting guide or seek help from the support community.