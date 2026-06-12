from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain.agents.middleware import wrap_model_call, ModelRequest, ModelResponse
from pydantic import BaseModel
from langchain.agents import create_agent
from langchain.agents.structured_output import ToolStrategy

class ContactInfo(BaseModel):
    name: str
    email: str
    phone: str

model_flash = ChatOpenAI(
    model="qwen-flash",  # 模型的代号
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    api_key="sk-4fedee4ece6541d3b17a7173f0b3c16f"
)

agent = create_agent(
    model=model_flash,
    system_prompt="You are a helpful assistant",
    response_format=ToolStrategy(ContactInfo),
    # response_format=ProviderStrategy(ContactInfo)
)
# 结构化输出， 默认是 ToolStrategy， langchain 自己实现的，通用的实现
# ProviderStrategy chatgpt、claude 支持的，其他的模型不支持， 非通用的场景


# ToolStrategy uses artificial tool calling to generate structured output.
# This works with any model that supports tool calling.
# ToolStrategy should be used when provider-native structured output (via ProviderStrategy) is not available or reliable.


result = agent.invoke({
    "messages": [{"role": "user", "content": "Extract contact info from: John Doe, john@example.com, (555) 123-4567"}]
})

print(result["structured_response"])