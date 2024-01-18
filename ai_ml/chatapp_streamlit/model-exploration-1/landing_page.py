import streamlit as st

from content_generation import content_gen_service

parent_container = st.container()
with parent_container:
    data = st.container()
    with data:
        output_container = st.container()


def main():
    st.sidebar.title("Generative AI/ML Exploration App")
    # Add options to the sidebar menu
    task_type = st.sidebar.selectbox("Task Type",
                                     ["Please Select Task to Perform", "Summarization/Generation Task",
                                      "Q&A", "Sentiment Analysis", "Clustering"])
    with data:
        data.title("Welcome to the Model Exploration")
        data.write("Place for AI/ML enthusiasts to play around")
        data.divider()

    if task_type == "Summarization Task":
        st.session_state.response_label = ''
        st.session_state.response_data = ''
        data.text_area("Enter the text for which you want to generate content", key="selected_text")
        st.sidebar.selectbox("Please select Model Type", ["gpt-3.5-turbo-instruct", "babbage-002", "davinci-002"],
                             key="selected_model")
        st.sidebar.text_input("Max Token", key="selected_token")
        st.sidebar.slider("Select Temperature", 0.0, 1.0, 0.5, key="selected_temperature", on_change=on_slider_change)
        st.sidebar.selectbox("Please select RAG Source", ["MongoDB", "Redis"], key="selected_rag")
        data.text_area("Enter the text for which you want to generate content", key="selected_text")
        data.button("Summarize Text", key="click_data", on_click=generate_summary())
        st.write(st.session_state.response_label)
        st.write(st.session_state.response_data)
    if task_type == "Q&A":
        st.write("Chatbot Text")
        st.session_state.response_label = ''
        st.session_state.response_data = ''
        data.text_input("Enter the text for which you want to generate content", key="selected_text")
        st.sidebar.selectbox("Please select Model Type",
                             ["gpt-3.5-turbo-instruct", "babbage-002", "davinci-002"],
                             key="selected_model")
        st.sidebar.text_input("Max Token", key="selected_token")
        st.sidebar.selectbox("Please select RAG Source", ["MongoDB", "Redis"], key="selected_rag")
        st.sidebar.slider("Select Temperature", 0.0, 1.0, 0.5, key="selected_temperature", on_change=on_slider_change)
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


def generate_rag_based_answer():
    with output_container:
        if st.session_state.selected_text and st.session_state.selected_model:
            st.session_state.response_label = "Context Based Reply from Open AI:"
            st.session_state.response_data = content_gen_service.generate_rag_based_content(
                st.session_state.selected_text,
                st.session_state.selected_model,
                st.session_state.selected_temperature,
                st.session_state.selected_token

            )


if __name__ == "__main__":
    main()
