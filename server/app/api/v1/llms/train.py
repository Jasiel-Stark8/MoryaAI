from torch.utils.data import Dataset, DataLoader
import json
import torch

path = 'GPT-2-conversation_dataset.json'

class ChatData(Dataset):
    """Dataset class for chat data"""
    def __init__(self, path: str, tokenizer, device: str = 'cpu'):
        """Initialize dataset"""
        self.tokenizer = tokenizer
        self.data = json.load(open(path, 'r', encoding='utf-8'))
        self.device = device

        self.dialogues = []
        for conversation in self.data:
            for i, dialog in enumerate(conversation['dialog']):
                if i < len(conversation['dialog']) -1:
                    prompt = dialog['text']
                    next_response = conversation['dialog'][i+1]['text']
                    combined_text = f'<startofstring> {prompt} <bot>: {next_response} <endostring>'
                    self.dialogues.append(combined_text)

    def __len__(self):
        """Get length of dataset"""
        return len(self.dialogues)

    def __getitem__(self, idx):
        """Get item from dataset at a specific index"""
        encoded_pair = self.tokenizer(self.dialogues[idx], truncation=True, padding='max_length', max_length=512, return_tensors='pt')
        input_ids = encoded_pair['input_ids'].squeeze().to(self.device)
        attention_mask = encoded_pair['attention_mask'].squeeze().to(self.device)
        return input_ids, attention_mask
