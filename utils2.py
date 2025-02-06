from langchain.chains import ConversationChain
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory


def get_chat_response(prompt, memory, key):
    model = ChatOpenAI(model="gpt-4o-mini", openai_api_key=key, openai_api_base = "https://api.aigc369.com/v1")
    chain = ConversationChain(llm=model, memory=memory)

    response = chain.invoke({"input": prompt})
    return response["response"]


memory = ConversationBufferMemory(return_messages=True)

# print(get_chat_response("牛顿提出过哪些知名的定律",memory,os.getenv("OPENAI_API_KEY")))
# print(get_chat_response("牛顿提出过哪些知名的定律",memory,os.getenv("OPENAI_API_KEY")))