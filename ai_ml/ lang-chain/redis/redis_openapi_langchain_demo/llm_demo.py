from langchain.chains import RetrievalQA
from langchain.llms.base import LLM
from langchain.vectorstores.redis import Redis as RedisVDB

from configs.openai_config import get_llm, get_openai_client
from data.data_loader import load_docs, get_vectorstore


def make_qna_chain(llm: LLM, vector_db: "RedisVDB", prompt: str = "", **kwargs):
    """Create the QA chain."""

    search_type = "similarity"
    if "search_type" in kwargs:
        search_type = kwargs.pop("search_type")

    # Create retreival QnA Chain
    chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vector_db.as_retriever(search_kwargs=kwargs, search_type=search_type),
        return_source_documents=True,
        chain_type_kwargs={"prompt": prompt},
        verbose=True
    )
    return chain

## We had to load docs as part of the job because getVectorstore without schema was failing
## in the new app it will be changed to  new thing
documents = load_docs()
vector_db = get_vectorstore(documents)
get_openai_client()
llm_to_be_used = get_llm()
print("Got LLM")
chain = make_qna_chain(llm_to_be_used, vector_db, "")
print("Created the Chain")
result = chain({"query": "Budget Highlights for 2023"})
print(result)
