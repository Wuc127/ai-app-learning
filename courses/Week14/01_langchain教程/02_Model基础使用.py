from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain.messages import HumanMessage, AIMessage, SystemMessage

model = ChatOpenAI(
    model="qwen-flash", # 模型的代号
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    api_key="sk-4fedee4ece6541d3b17a7173f0b3c16f"
)

# 方法1
responses = model.invoke("你好")
print(responses)

# 方法2
conversation = [
    {"role": "system", "content": "You are a helpful assistant that translates English to French."},
    {"role": "user", "content": "Translate: I love programming."},
    {"role": "assistant", "content": "J'adore la programmation."},
    {"role": "user", "content": "Translate: I love building applications."}
]
response = model.invoke(conversation)
print(response)

# 对话内容，都是人工确定
# 方法3
conversation = [
    SystemMessage("You are a helpful assistant that translates English to French."),
    HumanMessage("Translate: I love programming."),
    AIMessage("J'adore la programmation."),
    HumanMessage("Translate: I love building applications.")
]
response = model.invoke(conversation)
print(response)

# stream输出
for chunk in model.stream("你好"):
    print(chunk.text, end="|", flush=True)


# batch调用
# By default, batch() will only return the final output for the entire batch.
responses = model.batch([
    "Why do parrots have colorful feathers?",
    "How do airplanes fly?",
    "What is quantum computing?"
])
for response in responses:
    print(response)

# batch 调用，其中一个有执行完成，就返回
# If you want to receive the output for each individual input as it finishes generating, you can stream results with batch_as_completed():
responses = model.batch_as_completed([
    "Why do parrots have colorful feathers?",
    "How do airplanes fly?",
    "What is quantum computing?"
])
for response in responses:
    print(response)