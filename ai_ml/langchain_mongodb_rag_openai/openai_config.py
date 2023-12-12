from openai import OpenAI
import os

def getOpenAiClient():
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
    f =  open('api_key')
    lines = f.readlines()
    for line in lines:
        tokens = line.split("==")
        if tokens[0].strip() == 'openai_key':
            api_key = tokens[1].strip()
            os.environ["OPENAI_API_KEY"] = api_key
            return  OpenAI(api_key=api_key)

def getOpenAIKey():
    f =  open('api_key')
    lines = f.readlines()
    for line in lines:
        tokens = line.split("==")
        if tokens[0].strip() == 'openai_key':
            api_key = tokens[1].strip()
            os.environ["OPENAI_API_KEY"] = api_key
            return  api_key
    return None
