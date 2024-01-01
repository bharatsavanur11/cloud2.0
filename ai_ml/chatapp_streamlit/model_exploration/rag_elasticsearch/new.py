from langchain.vectorstores.elasticsearch import ElasticsearchStore
from langchain.embeddings import OpenAIEmbeddings
import json
from urllib.request import urlopen
from langchain.text_splitter import RecursiveCharacterTextSplitter

embedding = OpenAIEmbeddings(api_key="748dd50a1c52448984c85adbe58a891d:dXMtY2VudHJhbDEuZ2NwLmNsb3VkLmVzLmlvOjQ0MyQ5NTI4NDdlNmY5MWM0OWM1OWFjNzhiZmQzOTY2YjY0YiRiYzY4ZjMwZmFkNWU0MzA1OWNmOTVmMDg0MzY1MzI4MQ==")

url = "https://raw.githubusercontent.com/elastic/elasticsearch-labs/main/example-apps/chatbot-rag-app/data/data.json"
response = urlopen(url)
workplace_docs = json.loads(response.read())


metadata = []
content = []

for doc in workplace_docs:
    content.append(doc["content"])
    metadata.append({
        "name": doc["name"],
        "summary": doc["summary"],
        "rolePermissions":doc["rolePermissions"]
    })

text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(chunk_size=512, chunk_overlap=256)
docs = text_splitter.create_documents(content, metadatas=metadata)
print("Starting to store",docs)
documents = ElasticsearchStore.from_documents(
    docs,
    es_cloud_id="748dd50a1c52448984c85adbe58a891d:dXMtY2VudHJhbDEuZ2NwLmNsb3VkLmVzLmlvOjQ0MyQ5NTI4NDdlNmY5MWM0OWM1OWFjNzhiZmQzOTY2YjY0YiRiYzY4ZjMwZmFkNWU0MzA1OWNmOTVmMDg0MzY1MzI4MQ==",
    es_user="elastic",
    es_password="dwCkifbdwNCaDY5d1vmJPnJX",
    index_name="workplace_index"
)

print(documents)