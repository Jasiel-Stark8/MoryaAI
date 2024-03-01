from torch.utils.data import Dataset
import json

path = 'GPT-2-conversation_dataset.json'

class ChatData(Dataset):
    """Dataset class for chat data"""
    def __init__(self, path: str, tokenizer: object, max_length: int = 50, device: str = 'cpu'):
        """Initialize dataset"""
        self.data = json.loads(open(path, 'r', encoding='utf-8'))

        self.X = []
        for i in self.data:
            for j in i['dialog']:
                self.X.append(j['text'])

        for idx, i in enumerate(self.X):
            try:
                self.X[idx] = '<startofstring> '+i+' <bot>: '+self.X[i+1]+' <endostring>'
            except IndexError:
                break

        self.X = self.X[:-1]

        self.X_encoded = tokenizer(self.X, truncation=True, padding=True)
        self.input_ids = self.X_encoded['input_ids']
        self.attention_mask = self.X_encoded['attention_mask']

    def __len__(self):
        """Get length of dataset"""
        return len(self.X)

        def __get_item__(self, idx):
            """Get item from dataset at a specific index"""
            return (self.input_ids[idx], self.attention_mask[idx])
