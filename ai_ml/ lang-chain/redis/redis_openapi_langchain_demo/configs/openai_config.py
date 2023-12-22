from openai import OpenAI
import os
from langchain.embeddings import OpenAIEmbeddings

from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.llms.base import LLM



def get_openai_client():
    """
    Retrieves the OpenAI client object.

    Returns:
        client : openai.api_client.OpenAIClient
            The OpenAI client object configured with the API key.

  api_key = ''
    with open('api_key') as f:
        api_key = f.readline().strip('\n')
    client = OpenAI(api_key=api_key)
    os.environ["OPENAI_API_KEY"] = api_key
    return client
    """
    f = open(
        '/Users/bharatsavanur/Desktop/projects/personal_git_2/ai_ml/ lang-chain/redis/redis_openapi_langchain_demo/configs/api_key')
    lines = f.readlines()
    for line in lines:
        tokens = line.split("==")
        if tokens[0].strip() == 'openai_key':
            api_key = tokens[1].strip()
            os.environ["OPENAI_API_KEY"] = api_key
            return OpenAI(api_key=api_key)


def getOpenAIKey():
    f = open(
        '/Users/bharatsavanur/Desktop/projects/personal_git_2/ai_ml/ lang-chain/redis/redis_openapi_langchain_demo/configs/api_key')
    lines = f.readlines()
    for line in lines:
        tokens = line.split("==")
        if tokens[0].strip() == 'openai_key':
            api_key = tokens[1].strip()
            os.environ["OPENAI_API_KEY"] = api_key
            return api_key
    return None


def get_embeddings():
    embedding = OpenAIEmbeddings(
        model="text-embedding-ada-002"
    )
    return embedding


def get_llm(max_tokens=100) -> LLM:
    llm = ChatOpenAI(model_name='gpt-3.5-turbo-16k', max_tokens=max_tokens)
    return llm
