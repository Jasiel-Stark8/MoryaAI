from transformers import GPT2Tokenizer, GPT2LMHeadModel
from .train import ChatData

model_path = './distilgpt2'

# Load the tokenizer for the GPT-2 model from the specified path
tokenizer = GPT2Tokenizer.from_pretrained(model_path)

# Add special tokens for the start and end of the sequence
tokenizer.add_speacial_tokens({'bos_token': '<startofstring>',
                               'eos_token': '<endofstring>'})

model = GPT2LMHeadModel.from_pretrained(model_path)
