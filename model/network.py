import torch.nn as nn
import torch.nn.functional as F

class QNetwork(nn.Module):
    
    def __init__(self, dim_state, dim_action):
        
        super(QNetwork, self).__init__()
        
        self.conv1 = nn.Conv2d(dim_state[0], 32, 1)
        self.conv2 = nn.Conv2d(32, 16, 3)
        self.fc1 = nn.Linear(32, 32)
        self.fc2 = nn.Linear(32 ,32)
        self.fc3 = nn.Linear(32, dim_action)
    
    def forward(self, x):
        
        is_batch = (x.ndim == 4)

        if not is_batch: x = x.unsqueeze(0)

        x = F.relu(self.conv1(x))
        x = F.relu(self.conv2(x))
        x = x.flatten(1) 
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        
        return self.fc3(x)
