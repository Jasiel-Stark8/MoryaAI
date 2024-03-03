from transformers import GPT2Tokenizer, GPT2LMHeadModel
from torch.optim import Adam
from train import ChatData
from torch.utils.data import DataLoader
import torch
from tqdm import tqdm

# model_path = './distilgpt2'
model = GPT2LMHeadModel.from_pretrained('gpt2')
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
tokenizer.pad_token = tokenizer.eos_token
special_tokens_dict = {'bos_token': '<startofstring>',
                       'eos_token': '<endofstring>',
                       'additional_special_tokens': ['<bot> :']}
num_added_tokens = tokenizer.add_special_tokens(special_tokens_dict)
model.resize_token_embeddings(len(tokenizer))

# Load dataset
chatData = ChatData('GPT-2-conversation_dataset.json', tokenizer)
sample_data = chatData[0] # debug line
print(sample_data)

# Prepare DataLoader
data_loader = DataLoader(chatData, batch_size=16, shuffle=True)

# Correct device setup
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model.to(device)  # Correct method to move model to device

num_epochs = 5
optimizer = Adam(model.parameters(), lr=5e-5)

for epoch in range(num_epochs):
    model.train()
    total_loss = 0
    progress_bar = tqdm(enumerate(data_loader), total=len(data_loader), desc=f'Epoch {epoch+1}/{num_epochs}')
    for batch_idx, batch in progress_bar:
        input_ids, attention_mask = [b.to(device) for b in batch]

        optimizer.zero_grad()
        outputs = model(input_ids, attention_mask=attention_mask, labels=input_ids.detach())
        loss = outputs.loss
        loss.backward()
        optimizer.step()
        total_loss += loss.item()

        if (batch_idx + 1) % 100 == 0:  # Adjust the modulus value to control print frequency
            print(f'Epoch: {epoch+1}, Batch: {batch_idx+1}/{len(data_loader)}, Loss: {loss.item()}')

    avg_loss = total_loss / len(data_loader)
    print(f'Epoch: {epoch+1}, Average Loss: {avg_loss}')
