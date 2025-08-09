import streamlit as st
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key=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)

# Streamlit app UI
st.set_page_config(page_title="GPT Chatbot", page_icon="🤖")
st.title("🤖 GPT Chatbot")
st.write("Ask me anything!")

# User input
user_input = st.text_input("You:", placeholder="Type your question here...")

if user_input:
    try:
        # Generate response
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ]
        )

        # Display the chatbot's reply
        st.success(response.choices[0].message.content)

    except Exception as e:
        st.error(f"Error: {str(e)}")
