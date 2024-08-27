#Load libraries
from utils import *
import streamlit as st
from openai import OpenAI

#Load the environment variables from the st.secrets file
key = st.secrets["OPENAI_API_KEY"]

#Load and pre-process documents
texts = load_documents('downloaded_pdfs')

#Generate embeddings for documents
embeddings = get_embeddings(texts, model="text-embedding-3-small")

#Initialize OpenAI client
client = OpenAI(api_key=key)

#Function to generate a response from OpenAI
def generate_response(messages):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    return completion.choices[0].message.content

#Streamlit app
st.title("Intranet Search AI Assistant")

st.write("""
This chatbot can provide you with information from Kingston's HR intranet pages.
Simply enter a query and press 'send' to start the conversation.
""")

# Initialize session state for conversation history
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Display conversation history
for message in st.session_state.messages:
    if message['role'] == 'user':
        st.text_area("You:", message['content'], key=f"user_{message['content']}", height=50, max_chars=2000)
    elif message['role'] == 'assistant':
        st.text_area("Assistant:", message['content'], key=f"assistant_{message['content']}", height=50, max_chars=2000)

# Input form to avoid duplicating text_input key
with st.form(key='user_input_form', clear_on_submit=True):
    user_input = st.text_input("You:", key="user_input")
    submit_button = st.form_submit_button(label='Send')

if submit_button and user_input:
    # Add user message to conversation history
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Retrieve relevant text
    retrieved_text = retrieve_documents(user_input, embeddings, texts, model="text-embedding-3-small")

    # Add retrieved text to the context
    context = f"Context: {retrieved_text}\n\nUser Query: {user_input}"

    # Generate response from OpenAI
    response = generate_response(st.session_state.messages + [{"role": "system", "content": context}])

    # Add assistant message to conversation history
    st.session_state.messages.append({"role": "assistant", "content": response})

    # To clear the text input after submission
    st.experimental_rerun()

