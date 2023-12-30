import streamlit as st


def chatbot_response(user_input):
    # Replace this with your chatbot logic
    # For simplicity, let's just echo the user's input for now
    return f"You said: {user_input}"


def main():
    st.sidebar.title("Chatbot Menu")

    # Add options to the sidebar menu
    select_task = st.sidebar.selectbox("Select Option", ["Home", "Chat"])
    model_by_task = st.sidebar.selectbox("Select Model", ["GPT-3", "GPT-2", "GPT-1"])
    temp_value = st.sidebar.slider("Select a value", 0, 100, 50)

    if select_task == "Home":
        st.title("Welcome to the Machine Learning Playground App")
        st.write("This is where you learn/play/understand different ML Algorithms and LLM's.")

    elif select_task == "Chat":
        st.title("Chatbot with Streamlit")

        user_input = st.text_input("You:", "")
        if st.button("Ask"):
            response = chatbot_response(user_input)
            st.text_area("Chatbot:", response)
            st.write(f"Slider value: {temp_value}")


# Run the app

if __name__ == "__main__":
    main()
