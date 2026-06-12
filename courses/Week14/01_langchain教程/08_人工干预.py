from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain.agents.middleware import wrap_model_call, ModelRequest, ModelResponse
from langgraph.types import Command
from pydantic import BaseModel
from langchain.agents import create_agent
from langchain.agents.structured_output import ToolStrategy
from langchain.messages import AIMessage, HumanMessage
from langchain.agents import create_agent
from langchain.agents.middleware import HumanInTheLoopMiddleware
from langgraph.checkpoint.memory import InMemorySaver
from langchain.tools import tool

@tool
def your_read_email_tool(email_id: str) -> str:
    """Mock function to read an email by its ID."""
    return f"Email content for ID: {email_id}, 我今天很开心"

@tool
def your_send_email_tool(recipient: str, subject: str, body: str) -> str:
    """Mock function to send an email."""
    return f"Email sent to {recipient} with subject '{subject}'"

config = {"configurable": {"thread_id": "some_id"}}
model_flash = ChatOpenAI(
    model="qwen-flash",  # 模型的代号
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    api_key="sk-9c6195bf91f7435d88ea4b819073c92c"
)

agent = create_agent(
    model=model_flash,
    system_prompt="You are a helpful assistant",
    tools=[your_read_email_tool, your_send_email_tool],
    checkpointer=InMemorySaver(),
    middleware=[
        # 人工介入、人工确认
        HumanInTheLoopMiddleware(
            interrupt_on={
                "your_send_email_tool": {
                    "allowed_decisions": ["approve", "edit", "reject"],
                },
                "your_read_email_tool": {
                    "allowed_decisions": ["approve", "edit", "reject"],
                }
            }
        ),
    ],
)

result = agent.invoke(
    {"messages": [{"role": "user", "content": "Read email 123.'"}]},
    config=config,
    version="v2",
)
print(result["messages"][-1])
print(result.interrupts)

result = agent.invoke(
    Command(
        resume={"decisions": [{"type": "approve"}]}  # or "reject"
    ),
    config=config, # Same thread ID to resume the paused conversation
    version="v2",
)
print(result["messages"][-1])
