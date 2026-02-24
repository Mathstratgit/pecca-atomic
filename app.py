import streamlit as st
from pecca import Pecca

client = Pecca(api_key="pecca_YOUR_API_KEY_HERE")

st.title("My RAG Chatbot")

uploaded_file = st.file_uploader("Upload a file")
if uploaded_file:
    with open(uploaded_file.name, "wb") as f:
        f.write(uploaded_file.getbuffer())
    client.upload_to_knowledge_base(file_path=uploaded_file.name)
    st.success("File uploaded!")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

query = st.chat_input("Ask a question about your data")
if query:
    st.session_state.messages.append({"role": "user", "content": query})
    with st.chat_message("user"):
        st.write(query)
    with st.spinner("Thinking..."):
        response = client.ask_pecca(user_query=query, use_only_knowledge_base=False)
        answer = response["response_text"]
    st.session_state.messages.append({"role": "assistant", "content": answer})
    with st.chat_message("assistant"):
        st.write(answer)
