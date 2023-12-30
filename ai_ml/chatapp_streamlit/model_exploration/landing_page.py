import streamlit as st


def main():

    st.sidebar.title("Chatbot Menu")

    # Add options to the sidebar menu
    task_type = st.sidebar.selectbox("Task Type", ["Please Select Task to Perform","Summarization Task", "Generate Content","Sentiment Analysis", "Chatbot Text",])

    st.title("Welcome to the Model Exploration App for different LLM Tasks")
    st.write("This is the place for AI/ML enthusiasts to play around.")

    if task_type == "Summarization Task":
        st.write("Summarization Task")
        applicable_models = st.sidebar.selectbox("Please select Model Type",["GPT 2","GPT 3","FLAN T5"])

if __name__ == "__main__":
    main()
