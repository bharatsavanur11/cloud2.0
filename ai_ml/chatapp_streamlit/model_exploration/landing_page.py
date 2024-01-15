import streamlit as st

from content_generation import content_gen_service

parent_container = st.container()
with parent_container:
    data = st.container()
    with data:
        output_container = st.container()


# Main function


def generate_rag_based_answer():
    pass


def main():
    st.sidebar.title("Generative AI/ML Exploration App")
    # Add options to the sidebar menu
    task_type = st.sidebar.selectbox("Task Type",
                                     ["Please Select Task to Perform", "Summarization Task", "Generate Content",
                                      "Sentiment Analysis", "Q&A", "Clustering Task"])
    with data:
        data.title("Welcome to the Model Exploration")
        data.write("Place for AI/ML enthusiasts to play around")
        data.divider()

    if task_type == "Summarization Task":
        with data:
            st.write("Summarization Task")
        st.session_state.response_label = ''
        st.session_state.response_data = ''
        data.text_area("Enter the text for which you want to generate content", key="selected_text")
        st.sidebar.selectbox("Please select Model Type",
                             ["gpt-3.5-turbo-instruct", "babbage-002", "davinci-002"],
                             key="selected_model")
        st.sidebar.text_input("Max Token", key="selected_token")
        st.sidebar.slider("Select Temperature", 0.0, 1.0, 0.5, key="selected_temperature", on_change=on_slider_change)
        data.button("Summarize Text", key="click_data", on_click=generate_summary())
        st.write(st.session_state.response_label)
        st.write(st.session_state.response_data)

    if task_type == "Generate Content":
        data.write("Generate Content")
        st.session_state.response_label = ''
        st.session_state.response_data = ''
        data.text_input("Enter the text for which you want to generate content", key="selected_text")
        st.sidebar.selectbox("Please select Model Type",
                             ["gpt-3.5-turbo-instruct", "babbage-002", "davinci-002"],
                             key="selected_model")
        select_db = st.sidebar.selectbox("Please select DB for RAG", ["DB1", "DB2", "DB3"], key="selected_db")
        st.sidebar.text_input("Max Token", key="selected_token")
        st.sidebar.slider("Select Temperature", 0.0, 1.0, 0.5, key="selected_temperature", on_change=on_slider_change)
        response_placeholder = st.empty()
        data.button("Generate Content", key="click_data", on_click=generate_content())
        st.write(st.session_state.response_label)
        st.write(st.session_state.response_data)

    if task_type == "Sentiment Analysis":
        st.write("Sentiment Analysis")
    if task_type == "Q&A":
        st.write("Chatbot Text")
        st.session_state.response_label = ''
        st.session_state.response_data = ''
        data.text_input("Enter the text for which you want to generate content", key="selected_text")
        st.sidebar.selectbox("Please select Model Type",
                             ["gpt-3.5-turbo-instruct", "babbage-002", "davinci-002"],
                             key="selected_model")
        select_db = st.sidebar.selectbox("Please select DB for RAG", ["DB1", "DB2", "DB3"], key="selected_db")
        st.sidebar.text_input("Max Token", key="selected_token")
        st.sidebar.slider("Select Temperature", 0.0, 1.0, 0.5, key="selected_temperature", on_change=on_slider_change)
        st.sidebar.selectbox("Please select RAG Source",
                             ["MongoDB","Redis"],
                             key="selected_rag")
        response_placeholder = st.empty()
        data.button("Generate Content", key="click_data", on_click=generate_rag_based_answer())
        st.write(st.session_state.response_label)
        st.write(st.session_state.response_data)


def on_slider_change() -> None:
    st.session_state.selected_temperature = st.session_state.selected_temperature


def generate_content():
    with output_container:
        if st.session_state.selected_text and st.session_state.selected_model:
            st.session_state.response_label = "Open AI Replied: "
            st.session_state.response_data = (content_gen_service.generate_content(st.session_state.selected_text,
                                                                            st.session_state.selected_model,
                                                                            st.session_state.selected_temperature,
                                                                            st.session_state.selected_token))

def generate_summary():
    with output_container:
        if st.session_state.selected_text and st.session_state.selected_model:
            st.session_state.response_label = "Open AI Replied: "
            st.session_state.response_data = (content_gen_service.generate_content(st.session_state.selected_text,
                                                                                   st.session_state.selected_model,
                                                                                   st.session_state.selected_temperature,
                                                                                   st.session_state.selected_token))


if __name__ == "__main__":
    main()
