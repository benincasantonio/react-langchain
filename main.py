from typing import Union, List
from dotenv import load_dotenv
from langchain.agents.format_scratchpad import format_log_to_str
from langchain_core.agents import AgentAction, AgentFinish
from langchain.agents import tool, Tool
from langchain.prompts import PromptTemplate
from langchain.tools.render import render_text_description
from langchain.agents.output_parsers import ReActSingleInputOutputParser
from langchain_ollama import ChatOllama

from callbacks import AgentCallbackHandler

load_dotenv()


@tool
def get_text_length(text: str) -> int:
    """Returns the length of the text by counting the number of characters in the text."""
    # Strip away any leading or trailing whitespace and non-alphabetical characters
    text = text.strip("\n").strip('"').strip()
    return len(text)


def find_tool_by_name(tools: List[Tool], tool_name: str) -> Tool:
    for tool in tools:
        if tool.name == tool_name:
            return tool

    raise f"The tool with name {tool_name} was not found"


if __name__ == "__main__":
    print("Hello ReAct Langchain!")

    tools: List[Tool] = [get_text_length]

    template = """
    Answer the following questions as best you can. You have access to the following tools:

    {tools}

    Use the following format:

    Question: the input question you must answer
    Thought: you should always think about what to do
    Action: the action to take, should be one of [{tool_names}]
    Action Input: the input to the action
    Observation: the result of the action
    ... (this Thought/Action/Action Input/Observation can repeat N times)
    Thought: I now know the final answer
    Final Answer: the final answer to the original input question

    Begin!
    Question: {input}
    Thought: {agent_scratchpad}
    """

    prompt_template = PromptTemplate.from_template(template=template).partial(
        tools=render_text_description(tools),
        tool_names=", ".join([tool.name for tool in tools]),
    )

    llm = ChatOllama(
        model="phi4",
        temperature=0,
        stop=["\nObservation"],
        callbacks=[AgentCallbackHandler()]
    )

    intermediate_steps = []

    chain = (
        {
            "input": lambda x: x["input"],
            "agent_scratchpad": lambda x: format_log_to_str(x["agent_scratchpad"]),
        }
        | prompt_template
        | llm
        | ReActSingleInputOutputParser()
    )

    agent_step = None

    while not isinstance(agent_step, AgentFinish):
        agent_step: Union[AgentAction, AgentFinish] = chain.invoke(
            {"input": "What is the length of Capibara?", "agent_scratchpad": intermediate_steps}
        )

        if isinstance(agent_step, AgentAction):
            tool_name = agent_step.tool
            tool_to_run = find_tool_by_name(tools, tool_name)

            tool_input = agent_step.tool_input

            observation = tool_to_run.func(str(tool_input))
            print(f"{observation=}")
            intermediate_steps.append((agent_step, str(observation)))


    if isinstance(agent_step, AgentFinish):
        print(agent_step.return_values)
