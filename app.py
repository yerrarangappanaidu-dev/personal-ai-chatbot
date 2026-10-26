
import streamlit as st
import ollama

st.set_page_config(
    page_title="Personal AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

SYSTEM_PROMPT = """
You are a helpful AI tutor for a beginner learning programming
and artificial intelligence.

Explain concepts in simple English.
Use small code examples when useful.
Explain important code line by line.
If you are unsure about an answer, say so.
"""

st.title("🤖 Personal AI Chatbot")
st.caption("Powered by Gemma 3 1B and Ollama")

# Create conversation history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Clear conversation button
if st.button("Clear conversation"):
    st.session_state.messages = []
    st.rerun()

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Get user input
user_message = st.chat_input("Ask me anything...")

if user_message:
    st.session_state.messages.append({
        "role": "user",
        "content": user_message
    })

    with st.chat_message("user"):
        st.markdown(user_message)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                messages_for_model = [
                    {
                        "role": "system",
                        "content": SYSTEM_PROMPT
                    }
                ] + st.session_state.messages

                response = ollama.chat(
                    model="gemma3:1b",
                    messages=messages_for_model
                )

                answer = response["message"]["content"]

                st.markdown(answer)

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": answer
                })

            except Exception as error:
                st.error(
                    "Unable to get an AI response. "
                    "Check that Ollama is running and the model is available."
                )
                st.caption(f"Technical details: {error}")

                # Remove the unanswered user message
                st.session_state.messages.pop()
