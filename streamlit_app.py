import streamlit as st
import requests

# Streamlit UI
st.title("QA Chatbot")

# Input fields for context and question
context = st.text_area("Enter the context:", "")
question = st.text_input("Ask a question:", "")

# Send request to Flask backend
if st.button("Get Answer"):
    if context and question:
        response = requests.post(
            "http://localhost:5000/predict",
            json={"context": context, "question": question},
        )
        if response.status_code == 200:
            answer = response.json().get("answer")
            st.write(f"Answer: {answer}")
        else:
            st.write("Error: Unable to get an answer.")
    else:
        st.write("Please provide both context and a question.")
