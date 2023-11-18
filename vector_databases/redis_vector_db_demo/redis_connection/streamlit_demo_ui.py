import streamlit as st
from simple_streamlit_demo import search
import pandas as pd


def my_search():
    results = search(search_text)
    print(results)
    final_results = []
    for document in results:
        print(f'Movie Name: {document["title"]},\nMovie Plot: {document["plot"]}\n')
        final_results.append({
            "title": document["title"],
            "plot": document["plot"]
        })
    df = pd.DataFrame(final_results)
    st.table(df)
    #st.dataframe(df, use_container_width=False)


search_text = st.text_input("Enter Search String", "")
st.button("Search", on_click=my_search)
