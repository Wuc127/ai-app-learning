from langchain.agents import create_agent
from langchain_openai import ChatOpenAI

model = ChatOpenAI(
    model="qwen-flash", # 模型的代号
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    api_key="sk-4fedee4ece6541d3b17a7173f0b3c16f"
)

def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

# langchain agent 和  openai-agents agent 很相识，在llm调用基础上加入了额外的功能
agent = create_agent(
    model=model,
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)

result = agent.invoke(
    {"messages": [{"role": "user", "content": "北京天气怎么样？"}]}
)

print(result["messages"])
print(result["messages"][-1])