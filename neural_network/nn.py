import os
import torch
from torch import nn
from torch.utils.data import Dataset, DataLoader
from torchvision import datasets, transforms
import pandas as pd

class OptionsDataset(Dataset):
    def __init__(self, csv_file):
        self.data = pd.read_csv(csv_file).dropna()
        self.data = self.data.drop(columns=[' [QUOTE_READTIME]', ' [QUOTE_DATE]', ' [EXPIRE_DATE]'], errors='ignore')
        print(self.data.head())

        self.X = torch.tensor(self.data.iloc[:, :-1].values, dtype=torch.float32)  # Features
        self.y = torch.tensor(self.data.iloc[:, -1].values, dtype=torch.float32)   # Target (modify based on use case)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.X[idx], self.y[idx]

path = "C:/Users/kjg23/gitstuff/MachineLearningForEuropeanOptions/optionsdx/aapl_eod_2023q1-fslib7/aapl_eod_202301.csv"

dataset = OptionsDataset(path)
dataloader = DataLoader(dataset, batch_size=32, shuffle=True)

for X_batch, y_batch in dataloader:
    print("Feature batch shape:", X_batch.shape)
    print("Target batch shape:", y_batch.shape)
    break