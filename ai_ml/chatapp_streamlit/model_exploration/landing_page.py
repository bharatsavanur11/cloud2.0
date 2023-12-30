import streamlit as st

data = st.container()


def main():
    st.sidebar.title("Generative AI/ML Exploration App")
    # Add options to the sidebar menu
    task_type = st.sidebar.selectbox("Task Type",
                                     ["Please Select Task to Perform", "Summarization Task", "Generate Content",
                                      "Sentiment Analysis", "Chatbot Text", "Clustering Task"])
    with data:
        st.title("Welcome to the Model Exploration")
        st.write("Place for AI/ML enthusiasts to play around")
        st.divider()

    if task_type == "Summarization Task":

        with data:
            st.write("Summarization Task")
        applicable_models = st.sidebar.selectbox("Please select Model Type", ["GPT 2", "GPT 3", "FLAN T5"],
                                                 key="selected_model")
        if applicable_models:
            if len(applicable_models) > 0:
                temperature = st.sidebar.slider("Select Temperature", 0.0, 1.0, 0.5, key="selected_temperature",
                                                on_change=on_slider_change)
    if task_type == "Generate Content":
        st.write("Generate Content")
        applicable_models = st.sidebar.selectbox("Please select Model Type", ["GPT 2", "GPT 3", "FLAN T5"],
                                                 key="selected_model")
        select_db = st.sidebar.selectbox("Please select DB for RAG", ["DB1", "DB2", "DB3"], key="selected_db")
        if applicable_models:
            if len(applicable_models) > 0:
                temperature = st.sidebar.slider("Select Temperature", 0.0, 1.0, 0.5, key="selected_temperature",
                                                on_change=on_slider_change)
    if task_type == "Sentiment Analysis":
        st.write("Sentiment Analysis")
    if task_type == "Chatbot Text":
        st.write("Chatbot Text")


def on_slider_change():
    with data:
        st.write(
            f"The Current temperature {st.session_state.selected_temperature} and model selected is {st.session_state.selected_model}")


if __name__ == "__main__":
    main()
