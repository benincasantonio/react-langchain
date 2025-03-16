# ReAct Agent with LangChain

A simple implementation of the ReAct (Reasoning and Acting) agent pattern using LangChain and Ollama.

## Overview

This project demonstrates how to build a ReAct agent using LangChain. The ReAct pattern combines reasoning and acting in an iterative process:

1. **Reasoning**: The agent thinks about how to solve a problem
2. **Acting**: The agent takes an action using available tools
3. **Observing**: The agent observes the result
4. **Repeating**: The cycle continues until the agent reaches a final answer

## Features

- Simple ReAct agent implementation with LangChain
- Uses Ollama with Phi-4 as the LLM
- Custom callback handler to display prompts and responses
- Example tool implementation (`get_text_length`)

## Requirements

- Python 3.8+
- Ollama running locally with the Phi-4 model

## Installation

1. Clone the repository
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set up your environment variables in a `.env` file

## Usage

Run the main script:

```bash
python main.py
```

This will execute a ReAct agent that answers the question "What is the length of Capibara?" by using the `get_text_length` tool.

## Project Structure

- `main.py` - Contains the ReAct agent implementation and tool definition
- `callbacks.py` - Defines a custom callback handler to display prompts and responses
- `requirements.txt` - Lists required dependencies

## How It Works

1. The agent receives a question
2. It thinks about how to solve the problem
3. It selects a tool to use
4. It provides input to the tool
5. It observes the result
6. It continues this process until it has enough information to provide a final answer

The agent follows a specific prompt template that instructs it on how to reason and act using the available tools.

## Adding New Tools

To add new tools, follow this pattern:

```python
@tool
def your_new_tool(input_param: str) -> Any:
    """Description of what the tool does."""
    # Tool implementation
    return result
```

Then, add the tool to the `tools` list in `main.py`.

## License

MIT
