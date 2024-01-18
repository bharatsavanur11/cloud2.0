from openai import OpenAI
import os


file_path =  os.path.join(os.path.dirname(__file__), '..', 'md_exp_configs', 'api_key')

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
    f = open(file_path)
    lines = f.readlines()
    for line in lines:
        tokens = line.split("==")
        if tokens[0].strip() == 'openai_key':
            api_key = tokens[1].strip()
            os.environ["OPENAI_API_KEY"] = api_key
            return OpenAI(api_key=api_key)


def get_openai_key():
    f = open(file_path)
    lines = f.readlines()
    for line in lines:
        tokens = line.split("==")
        if tokens[0].strip() == 'openai_key':
            api_key = tokens[1].strip()
            os.environ["OPENAI_API_KEY"] = api_key
            return api_key
    return None

