from md_exp_configs.openai_config import get_openai_client
from rag.mongo_db.langchain_operations import search_using_langchain,query_data


def generate_content(prompt, model, temperature: 0.7, max_tokens: 400):
    '''
    Generates content based on prompt from vanilla open API Call
    :param model:
    :param temperature:
    :param max_tokens:
    :param prompt:
    :return:
    '''
    client = get_openai_client()
    completion = client.completions.create(
        model=model,
        prompt=prompt,
        temperature=temperature,
        max_tokens=400,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return completion.choices[0].text


def generate_rag_based_content(selected_text, model, temperature, token:400):
    semantic_search_results,open_ai_search_result = query_data(selected_text)

    return open_ai_search_result
