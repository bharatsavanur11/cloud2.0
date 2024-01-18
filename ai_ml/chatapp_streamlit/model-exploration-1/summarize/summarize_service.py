from md_exp_configs.openai_config import get_openai_client


# Split text into chunks of 2048 characters

def split_text(text):
    max_chunk_size = 2048
    chunks = []
    current_chunk = ""
    for sentence in text.split("."):
        if len(current_chunk) + len(sentence) < max_chunk_size:
            current_chunk += sentence + "."
        else:
            chunks.append(current_chunk.strip())
            current_chunk = sentence + "."
    if current_chunk:
        chunks.append(current_chunk.strip())
    return chunks

def generate_content_chunk(chunk, model, temperature, max_tokens):
    client = get_openai_client()
    completion = client.completions.create(
        model=model,
        prompt=chunk,
        temperature=temperature,
        max_tokens=400,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return completion.choices[0].text


def generate_content(prompt, model, temperature: 0.7, max_tokens: 400):
    chunks = split_text(prompt)
    output_chunks = []
    for chunk in chunks:
        output_chunks.append(generate_content_chunk(chunk, model, temperature, max_tokens))
    return " ".join(output_chunks)



