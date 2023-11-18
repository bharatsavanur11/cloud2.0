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
    # show_table(df)
    return df
    # st.dataframe(df, use_container_width=False)


st.title("MongoDB Vector Search for Movies")

search_text = st.text_input("Enter Search String", "")
searched = st.button("Search")
# table_placeholder = st.container()
if searched:
    result_df = my_search()
    st.table(result_df)
