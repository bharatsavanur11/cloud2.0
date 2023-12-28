
dash_line = '-'.join('' for x in range(100))

def make_prompt_for_oneshot(dataset,example_indices_full, example_index_to_summarize):
    prompt = ''
    for index in example_indices_full:
        dialogue = dataset['test'][index]['dialogue']
        summary = dataset['test'][index]['summary']

        # The stop sequence '{summary}\n\n\n' is important for FLAN-T5. Other models may have their own preferred stop sequence.
        prompt += f"""
Dialogue:

{dialogue}

What was going on?
{summary}


"""

    dialogue = dataset['test'][example_index_to_summarize]['dialogue']
    prompt += f"""
Dialogue:

{dialogue}

What was going on?
"""
    print("Hello")
    return prompt

def print_ref_and_base_summaries(summary, output):
    print(dash_line)
    print(f'REFERENCE SUMMARY: {summary}')
    print(dash_line)
    print(f'GENERATED SUMMARY: {output}')
    print(dash_line)