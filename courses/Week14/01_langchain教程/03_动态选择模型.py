from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain.agents.middleware import wrap_model_call, ModelRequest, ModelResponse

model_flash = ChatOpenAI(
    model="qwen-flash",  # 模型的代号
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    api_key="sk-4fedee4ece6541d3b17a7173f0b3c16f"
    # https://reference.langchain.com/python/langchain-openai/chat_models/base/ChatOpenAI
    # 这里可以设置底层调用模型的参数
)

model_max = ChatOpenAI(
    model="qwen-max",  # 模型的代号
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    api_key="sk-4fedee4ece6541d3b17a7173f0b3c16f"
    # https://reference.langchain.com/python/langchain-openai/chat_models/base/ChatOpenAI
    # 这里可以设置底层调用模型的参数
)

# 通过 @wrap_model_call 装饰器创建的中间件函数
# 它把你的普通函数包装成 LangChain 认可的中间件格式
@wrap_model_call
def dynamic_model_selection(request: ModelRequest, handler) -> ModelResponse:
    """Choose model based on conversation complexity."""
    message_count = len(request.state["messages"])

    if message_count > 10:
        # Use an advanced model for longer conversations
        model = model_max # 复杂的模型，慢，但对历史记忆好
    else:
        model = model_flash # 简单的模型，快，但是对历史记忆差

    return handler(request.override(model=model))


# 创建模型，static model，调用的时候模型版本和参数不会变化
static_agent = create_agent(
    model=model_flash,
    system_prompt="You are a helpful assistant",
)


# middleware 是一个中间件机制，它允许你在 Agent 调用模型之前拦截和修改请求。
# 创建模型，dynamic model，调用时候结合输入来选择模型
dynamic_agent = create_agent(
    model=model_flash,  # Default model
    middleware=[dynamic_model_selection]
)



result = static_agent.invoke(
    {"messages": [{"role": "user", "content": "帮我介绍机器学习和大模型的关系"}]}
)
print(result["messages"][-1])


result = dynamic_agent.invoke(
    {"messages": [{"role": "user", "content": "帮我介绍机器学习和大模型的关系"}]}
)
print(result["messages"][-1])