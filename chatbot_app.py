# chatbot_app.py

import streamlit as st

def main():
    st.header("Super-Intelligent Parrot Chatbot")

    option = st.selectbox(
        'Which GPT model do you want to use?',
        ["GPT3.5-Parrot", "Llama-Parrot-70b"])

    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "How can I help you?"}]

    for m in st.session_state.messages:
        st.chat_message(m["role"]).write(m["content"])

    # Move st.chat_input() outside the expander
    prompt = st.chat_input()
    if prompt:
        st.chat_message("user").write(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})
        messages = st.session_state.messages

        # Simulating a response, replace this part with actual OpenAI API call
        assistant_response = "Assistant response goes here"
        st.session_state.messages.append({"role": "assistant", "content": assistant_response})

    if st.checkbox('Show name'):
        name = st.text_input("Your name", key="name")
        if name:
            st.write(f"Hello, {name}!")

    # Display the name from session state
    if "name" in st.session_state:
        st.write(f"Name from session state: {st.session_state.name}")

if __name__ == "__main__":
    main()
