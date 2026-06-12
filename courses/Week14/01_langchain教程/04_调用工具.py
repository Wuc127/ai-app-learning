from langchain.tools import tool
from langchain.tools import tool, ToolRuntime
from langchain.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent, AgentState
from langchain.agents.middleware import wrap_model_call, ModelRequest, ModelResponse
from pydantic import BaseModel, Field
from typing import Literal

class WeatherInput(BaseModel):
    """Input for weather queries."""
    location: str = Field(description="City name or coordinates")
    units: Literal["celsius", "fahrenheit"] = Field(
        default="celsius",
        description="Temperature unit preference"
    )
    include_forecast: bool = Field(
        default=False,
        description="Include 5-day forecast"
    )


@tool(args_schema=WeatherInput)
def get_weather(location: str, units: str = "celsius", include_forecast: bool = False) -> str:
    """Get current weather and optional forecast."""
    temp = 22 if units == "celsius" else 72
    result = f"Current weather in {location}: {temp} degrees {units[0].upper()}"
    if include_forecast:
        result += "\nNext 5 days: Sunny"
    return result


@tool
def search_database(query: str, limit: int = 10) -> str:
    """Search the customer database for records matching the query.

    Args:
        query: Search terms to look for
        limit: Maximum number of results to return
    """
    return f"Found {limit} results for '{query}'"


@tool("web_search")  # Custom name
def search(query: str) -> str:
    """Search the web for information."""
    return f"Results for: {query}"


@tool("calculator", description="Performs arithmetic calculations. Use this for any math problems.")
def calc(expression: str) -> str:
    """Evaluate mathematical expressions."""
    return str(eval(expression))

# ToolRuntime 运行时状态， 历史对话

@tool
def get_last_user_message(runtime: ToolRuntime) -> str:
    """Get the most recent message from the user."""
    messages = runtime.state["messages"]

    # Find the last human message
    for message in reversed(messages):
        if isinstance(message, HumanMessage):
            return message.content

    return "No user messages found"


# Access custom state fields
@tool
def get_user_preference(
    pref_name: str,
    runtime: ToolRuntime
) -> str:
    """Get a user preference value."""
    preferences = runtime.state.get("preferences", {})
    print("111", runtime.state)
    return preferences.get(pref_name, "Not set")


model = ChatOpenAI(
    model="qwen-flash",  # 模型的代号
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    api_key="sk-4fedee4ece6541d3b17a7173f0b3c16f"
    # https://reference.langchain.com/python/langchain-openai/chat_models/base/ChatOpenAI
    # 这里可以设置底层调用模型的参数
)


class CustomAgentState(AgentState):
    user_id: str
    preferences: dict


agent = create_agent(
    model=model,
    tools=[get_user_preference],
    system_prompt="You are a helpful assistant",
    state_schema=CustomAgentState,
)

result = agent.invoke(
    {
        "messages": [{"role": "user", "content": "what is the theme in preferences?"}],
        "user_id": "user_123",
        "preferences": {"theme": "dark"}
    },
    {"configurable": {"thread_id": "1"}}
)
print(result["messages"][-1])


# langchain的tool ，可以获取 历史对话、 也可以获取agent 配置
# 场景： 基于用户查询用户的消费, tool 可以基于 user id 查询对应的消费情况
"""
通过state的方式传入用户名
result = agent.invoke(
    {
        "messages": [{"role": "user", "content": "帮我查询我的消费记录"}],
        "user_id": "user_123",
    },
    {"configurable": {"thread_id": "1"}}
)
print(result["messages"][-1])


直接在对话中传入用户名
result = agent.invoke(
    {
        "messages": [{"role": "user", "content": "我是用户 user_123, 帮我查询我的消费记录"}],
    },
    {"configurable": {"thread_id": "1"}}
)
print(result["messages"][-1])
"""

