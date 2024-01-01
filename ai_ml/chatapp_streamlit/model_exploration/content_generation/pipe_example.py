from transformers import pipeline

# Create a text generation pipeline with GPT-2
pipe = pipeline("text-generation", model="gpt2")
result = pipe("How are you")
print(result)