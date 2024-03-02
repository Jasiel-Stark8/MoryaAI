from transformers import GPT2Tokenizer, GPT2LMHeadModel
from torch.optim import Adam
from train import ChatData
from torch.utils.data import DataLoader
import torch

model_path = './distilgpt2'
model = GPT2LMHeadModel.from_pretrained(model_path)
tokenizer = GPT2Tokenizer.from_pretrained(model_path)
tokenizer.pad_token = tokenizer.eos_token
special_tokens_dict = {'bos_token': '<startofstring>',
                        'eos_token': '<endofstring>',
                        'additional_special_tokens': ['<bot> :']}
num_added_tokens = tokenizer.add_special_tokens(special_tokens_dict)
model.resize_token_embeddings(len(tokenizer))

# Load dataset
chatData = ChatData('GPT-2-conversation_dataset.json', tokenizer)

# Prepare DataLoader
data_loader = DataLoader(chatData, batch_size=2, shuffle=True)

# Run on device
device = torch.device('cuda', if torch.cuda.is_available() else 'cpu')
model.to(device)

num_epochs = 5
optimizer = Adam(model.parameters(), lr=5e-5)

for epoch in range(num_epochs):
    model.train()
    total_loss = 0
    for batch in data_loader:
        # Move batch to the correct device
        input_ids, attention_mask = [b.to(device) for b in batch]
        
        optimizer.zero_grad()
        
        # Ensure labels are also on the correct device by duplicating input_ids
        outputs = model(input_ids, attention_mask=attention_mask, labels=input_ids.detach())
        
        loss = outputs.loss
        loss.backward()
        optimizer.step()
        total_loss += loss.item()
    
    # Print progress
    print(f'Epoch: {epoch+1}, Loss: {total_loss / len(data_loader)}')