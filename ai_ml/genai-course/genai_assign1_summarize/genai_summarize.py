from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, GenerationConfig
from generate_prompt import make_prompt_for_oneshot, print_ref_and_base_summaries

## Load DataSet
dataset = load_dataset("knkarthick/dialogsum")
print(dataset['test'])
example_indices = [40, 300]
dash_line = '-'.join('' for x in range(100))
print(dash_line)
'''for i, index in enumerate(example_indices):
    print(dash_line)
    print('Example', i + 1)
    print(dash_line)
    print('INPUT DIALOGUE:')
    print(dataset['test'][index]['dialogue'])
    print('Baseline  Human Summary:')
    print(dataset['test'][index]['dialogue'])
    print(dash_line '''

## Load Flan T5 model

model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-base")
tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-base")

## Generate Summary
question_data = "What time is it in New York?"
question_encoded = tokenizer(question_data, return_tensors='pt')
# print(question_encoded)

## Check if the encoding has happened correctly once.
question_decoded = tokenizer.decode(question_encoded['input_ids'][0], skip_special_tokens=True)
# print(question_decoded)

'''for i, index in enumerate(example_indices):
    dialogue = dataset['test'][index]['dialogue']
    summary = dataset['test'][index]['summary']
    dialogue_encoded = tokenizer(dialogue, return_tensors='pt')
    # print(dialogue_encoded)
    output = tokenizer.decode(model.generate(dialogue_encoded['input_ids'], max_length=30)[0], max_tokens=100)
    print("REFERENCE SUMMARY:")
    print(summary)
    print(dash_line)
    print("GENERATED SUMMARY:")
    print(output) '''

## Understanding Instruction Prompt

'''for i, index in enumerate(example_indices):
    dialogue = dataset['test'][index]['dialogue']
    summary = dataset['test'][index]['summary']
    prompt = f"""Summarize the following dialogue: {dialogue}."
               Summary:"""
    input_tokenized = tokenizer(prompt, return_tensors='pt')
    output = tokenizer.decode(model.generate(input_tokenized['input_ids'], max_length=50)[0], max_tokens=50)
    print("REFERENCE SUMMARY:")
    print(summary)
    print(dash_line)
    print("GENERATED SUMMARY:")
    print(output)
    print(dash_line)'''

## Understanding Instruction Prompt template from Flan - T5

'''for i,index in enumerate(example_indices):
    dialogue = dataset['test'][index]['dialogue']
    summary = dataset['test'][index]['summary']
    prompt = f"""Dialogue: {dialogue}. What is going on?
                   """
    input_tokenized = tokenizer(prompt, return_tensors='pt')
    output = tokenizer.decode(model.generate(input_tokenized['input_ids'], max_length=50)[0], max_tokens=50)
    print("REFERENCE SUMMARY:")
    print(summary)
    print(dash_line)
    print("GENERATED SUMMARY:")
    print(output)
    print(dash_line)'''

### Understanding One Shot Inference -  Example

example_indices_full = [40]
example_index_to_summarize = 200
one_shot_prompt = make_prompt_for_oneshot(dataset, example_indices_full, example_index_to_summarize)
print(one_shot_prompt)

summary = dataset['test'][example_index_to_summarize]['summary']
inputs = tokenizer(one_shot_prompt, return_tensors='pt')
output = tokenizer.decode(model.generate(inputs['input_ids'], max_length=50)[0], max_tokens=50,
                          skip_special_tokens=True)
print_ref_and_base_summaries(summary, output)
### Few One Shot Inference -  Examples


### Few One Shot Inference -  Examples

example_indices_full = [40, 80, 120, 160, 200, 240, 280, 300]
example_index_to_summarize = [400]
one_shot_prompt = make_prompt_for_oneshot(dataset, example_indices_full, example_index_to_summarize)

summary = dataset['test'][example_index_to_summarize]['summary']
inputs = tokenizer(one_shot_prompt, return_tensors='pt')

output = tokenizer.decode(model.generate(inputs['input_ids'], max_length=50)[0], max_tokens=50,
                          skip_special_tokens=True)

print_ref_and_base_summaries(summary, output)
##---------------------------------------------------------------------------------------------------------------------
generation_config = GenerationConfig(max_new_tokens=50)
# generation_config = GenerationConfig(max_new_tokens=10)
# generation_config = GenerationConfig(max_new_tokens=50, do_sample=True, temperature=0.1)
# generation_config = GenerationConfig(max_new_tokens=50, do_sample=True, temperature=0.5)
# generation_config = GenerationConfig(max_new_tokens=50, do_sample=True, temperature=1.0)

output = tokenizer.decode(model.generate(inputs['input_ids'], generation_config=generation_config)[0], max_tokens=50,skip_special_tokens=True)

print_ref_and_base_summaries(summary, output)