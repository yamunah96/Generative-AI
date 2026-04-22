from utils.reterival import load_chorma_collection,retrieve_chunks
from utils.prompt import my_prompt
from utils.completion import generate_completion
import streamlit as st


st.title("RAG App – AI History Chatbot")
st.write("Ask any question about the history of Artificial Intelligence.")

query = st.text_input("Enter your question here")

if query:
    with st.spinner("Thinking..."):
        collection =load_chorma_collection()
        top_chunks = retrieve_chunks(query, collection)
        prompt = my_prompt(top_chunks, query)
        response = generate_completion(prompt)

        st.subheader("Answer")
        st.write(response)