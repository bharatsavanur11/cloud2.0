import json

from openai import OpenAI
from md_exp_configs.openai_config import get_openai_client

client = get_openai_client()
prompt = '{"content": "How are you?")'
#data = json.loads(prompt)
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[prompt]
)

print(completion.choices[0].message)
