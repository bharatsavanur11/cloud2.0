from transformers import GPT2Tokenizer, GPT2LMHeadModel, GPT2Config
from transformers import TextDataset, DataCollatorForLanguageModeling
from transformers import Trainer, TrainingArguments


# Load pre-trained GPT-2 model and tokenizer
model_name = "gpt2"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Load your fine-tuning d   ataset (replace with your actual dataset)
train_file_path = "/Users/bharatsavanur/Desktop/projects/personal_git_2/ai_ml/train-llm-demo/gpt2/training_data.txt"
train_dataset = TextDataset(
    tokenizer=tokenizer,
    file_path=train_file_path,
    block_size=64,
)

#with open("/Users/bharatsavanur/Desktop/projects/personal_git_2/ai_ml/train-llm-demo/gpt2/training_data.txt", "r") as f:
    #print(f.read())

print(train_dataset.examples)

# Configure fine-tuning settings
training_args = TrainingArguments(
    output_dir="./fine_tuned_gpt2",
    overwrite_output_dir=True,
    num_train_epochs=3,
    per_device_train_batch_size=2,
    save_steps=10_000,
    save_total_limit=2,
    evaluation_strategy="steps",
    eval_steps=10_000,
    logging_steps=10_000,
)

# Define data collator
data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer,
    mlm=False,  # Set to True if using masked language modeling
)

# Create Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=data_collator,
    train_dataset=train_dataset,

)

# Fine-tune the GPT-2 model
trainer.train()

# Save the fine-tuned model
model.save_pretrained("./fine_tuned_gpt2")
tokenizer.save_pretrained("./fine_tuned_gpt2")
