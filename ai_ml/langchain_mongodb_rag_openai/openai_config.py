from openai import OpenAI
def getOpenAiClient():
    """
    Retrieves the OpenAI client object.

    Returns:
        client : openai.api_client.OpenAIClient
            The OpenAI client object configured with the API key.

    """
    api_key = ''
    with open('api_key') as f:
        api_key = f.readline().strip('\n')
    client = OpenAI(api_key=api_key)
    os.environ["OPENAI_API_KEY"] = api_key
    return client

def getOpenAIKey():
    with open('api_key') as f:
        api_key = f.readline().strip('\n')
    return api_key


