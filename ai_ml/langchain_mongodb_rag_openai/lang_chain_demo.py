from pymongo import MongoClient
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import MongoDBAtlasVectorSearch
from langchain.document_loaders import DirectoryLoader
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
import gradio as gr
from gradio.themes.base import Base
from pymongo import MongoClient
from mongo_operations import get_mongo_client
from openai_config import getOpenAIKey

client = get_mongo_client()
dbName = "langchain_demo"
collectionName = "text_data_1"
collection = client[dbName][collectionName]
index_name = "lang_demo_test"

api_key = getOpenAIKey()

# Define the text embedding model
embeddings = OpenAIEmbeddings(openai_api_key=api_key)

# Initialize the Vector Store
vectorStore = MongoDBAtlasVectorSearch(collection, embeddings, index_name=index_name)


def query_data(query):
    # Convert question to vector using OpenAI embeddings
    # Perform Atlas Vector Search using Langchains vectorStore
    # similarity_search returns MongoDB documents most similar to the query
    print(query)
    docs = vectorStore.similarity_search(query,)
    as_output = docs

    # Leveraging Atlas Vector Search paired with Langchain's QARetriever

    # Define the LLM that we want to use -- note that this is the Language Generation Model and NOT an Embedding Model
    # If it's not specified (for example like in the code below),
    # then the default OpenAI model used in LangChain is OpenAI GPT-3.5-turbo, as of August 30, 2023

    llm = OpenAI(openai_api_key=api_key, temperature=0)

    # Get VectorStoreRetriever: Specifically, Retriever for MongoDB VectorStore.
    # Implements _get_relevant_documents which retrieves documents relevant to a query.

    retriever = vectorStore.as_retriever()

    # Load "stuff" documents chain. Stuff documents chain takes a list of documents,
    # inserts them all into a prompt and passes that prompt to an LLM.

    qa = RetrievalQA.from_chain_type(llm, chain_type="refine", retriever=retriever)

    # Execute the chain
    retriever_output = qa.run(query)

    # Return Atlas Vector Search output, and output generated using RAG Architecture
    return as_output, retriever_output


# Create a web interface for the app, using Gradio

with gr.Blocks(theme=Base(), title="Question Answering App using Vector Search + RAG") as demo:
    gr.Markdown(
        """
        # Question Answering App using Atlas Vector Search + RAG Architecture
        """)
    textbox = gr.Textbox(label="Enter your Question:")
    with gr.Row():
        button = gr.Button("Submit", variant="primary")
    with gr.Column():
        output1 = gr.Textbox(lines=1, max_lines=10,
                             label="Output with just Atlas Vector Search (returns text field as is):")
        output2 = gr.Textbox(lines=1, max_lines=10,
                             label="Output generated by chaining Atlas Vector Search to Langchain's RetrieverQA + OpenAI LLM:")

    # Call query_data function upon clicking the Submit button

    button.click(query_data, textbox, outputs=[output1, output2])

demo.launch()