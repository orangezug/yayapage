import streamlit as st
from langchain.memory import ConversationBufferMemory
from utils2 import get_chat_response

api_key = st.secrets["api"]["key"]



st.title("🦆 克隆gpt-4o-mini")

if "memory" not in st.session_state:
    st.session_state["memory"] = ConversationBufferMemory(return_messages=True)
    st.session_state["messages"] = [{"role": "ai",
                                     "content": "你好，我是你的AI助手，有什么可以帮你的吗？"}]

placeholder = st.empty()
with placeholder.container():
    for message in st.session_state["messages"]:
        st.chat_message(message["role"]).write(message["content"])

prompt = st.chat_input()
if prompt:

    st.session_state["messages"].append({"role": "human", "content": prompt})
    st.chat_message("human").write(prompt)

    with st.spinner("AI正在思考中，请稍等..."):
        response = get_chat_response(prompt, st.session_state["memory"], api_key)
    msg = {"role": "ai", "content": response}
    st.session_state["messages"].append(msg)
    st.chat_message("ai").write(response)

st.divider()

cl1, cl2 = st.columns([5,1])

with cl1:
    if st.button("清空记忆"):
        st.session_state.clear()
        st.rerun()

with cl2:
    if st.button("清空对话"):
        st.session_state.messages.clear()  # 清空消息列表
        placeholder.empty()  # 清空占位符内容