import streamlit as st
from main import generate_response 

st.title("🍽️ Chicken Station Menu Chatbot")
st.markdown("Ask me anything about the menu!")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display past messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
user_input = st.chat_input("Type your message...")

if user_input:
    # Display user message
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Generate and display response
    with st.spinner("Thinking..."):
        response = generate_response(user_input)
        st.chat_message("assistant").markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
