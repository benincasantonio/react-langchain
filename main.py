from typing import Union
from dotenv import load_dotenv
from langchain_core.agents import AgentAction, AgentFinish
from langchain.agents import tool
from langchain.prompts import PromptTemplate
from langchain.tools.render import render_text_description
from langchain.agents.output_parsers import ReActSingleInputOutputParser
from langchain_ollama import ChatOllama
load_dotenv()


@tool
def get_text_length(text: str) -> int:
    """Returns the length of the text by counting the number of characters in the text."""
    return len(text)


if __name__ == "__main__":
    print("Hello ReAct Langchain!")

    tools = [get_text_length]

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
    Thought:
    """

    prompt_template = PromptTemplate.from_template(template=template).partial(
        tools=render_text_description(tools),
        tool_names=", ".join([tool.name for tool in tools]),
    )

    llm = ChatOllama(
        model="llama3.2",
        temperature=0,
        stop=["\nObservation"],
    )

    chain = {"input": lambda x:x["input"]} | prompt_template | llm | ReActSingleInputOutputParser()

    agent_step: Union[AgentAction, AgentFinish] = chain.invoke({"input": "What is the length of 'GTA V'?"})

    print(agent_step)
