import torch
import torch.nn as nn
import torch.nn.functional as F

class Recognizer(nn.Module):
    def __init__(self):
        super(Recognizer, self).__init__()
        
        self.conv1 = nn.Conv2d(1, 16, kernel_size=3, stride=1, padding=1)
        self.conv2 = nn.Conv2d(16, 32, kernel_size=3, stride=1, padding=1)
        
        self.bn1 = nn.BatchNorm2d(16)
        self.bn2 = nn.BatchNorm2d(32)
        
        
        self.pool1 = nn.MaxPool2d(kernel_size=2, stride=2)
        self.pool2 = nn.MaxPool2d(kernel_size=2, stride=2)
        
        self.drop = nn.Dropout2d(0.25)
        
        self.fc1 = nn.Linear(32 * 16 *16, 2048)
        self.fc2 = nn.Linear(2048, 712)
        self.fc3 = nn.Linear(712, 178)

    def forward(self, x):
        x = self.pool1(F.relu(self.bn1(self.conv1(x))))
        x = self.pool2(F.relu(self.bn2(self.conv2(x))))
        
        x = x.view(-1, 32 * 16 * 16)
        x = self.drop(self.fc1(x))
        x = self.fc2(x)
        x = self.fc3(x)

        return x