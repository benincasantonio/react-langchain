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
- LangSmith integration for tracing and debugging

## LangSmith Integration

This project includes integration with [LangSmith](https://smith.langchain.com/), which provides tracing, monitoring, and evaluation capabilities for LangChain applications:

- **Tracing**: Track and visualize the execution of your agent's reasoning steps
- **Debugging**: Easily identify issues with your agent's reasoning process
- **Performance Monitoring**: Analyze latency, token usage, and other metrics

To use LangSmith, you need to:

1. Create a LangSmith account at https://smith.langchain.com/
2. Get your API key from the LangSmith dashboard
3. Configure the environment variables in your `.env` file

## Requirements

- Python 3.8+
- Ollama running locally with the Phi-4 model
- LangSmith account (for tracing and debugging)

## Installation

1. Clone the repository
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set up your environment variables in a `.env` file (copy from `.env.example`):

```
LANGSMITH_TRACING=true
LANGSMITH_ENDPOINT="https://api.smith.langchain.com"
LANGSMITH_API_KEY="your-langsmith-api-key"
LANGSMITH_PROJECT="your-project-name"
```

## Usage

Run the main script:

```bash
python main.py
```

This will execute a ReAct agent that answers the question "What is the length of Capibara?" by using the `get_text_length` tool.

After running the agent, you can view the trace in your LangSmith dashboard to analyze the agent's reasoning steps and performance.

## Project Structure

- `main.py` - Contains the ReAct agent implementation and tool definition
- `callbacks.py` - Defines a custom callback handler to display prompts and responses
- `requirements.txt` - Lists required dependencies
- `.env.example` - Template for environment variables including LangSmith configuration

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
