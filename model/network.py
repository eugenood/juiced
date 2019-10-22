import torch.nn as nn
import torch.nn.functional as F

class QNetwork(nn.Module):
    
    def __init__(self, dim_state, dim_action):
        
        super(QNetwork, self).__init__()
        
        self.fc1 = nn.Linear(dim_state[0] * dim_state[1], 24)
        self.fc2 = nn.Linear(24, 24)
        self.fc3 = nn.Linear(24, dim_action)
    
    def forward(self, x):
        
        if x.dim() == 3: x = x.reshape(x.shape[0], -1)
        else: x = x.reshape(1, -1)

        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        
        return self.fc3(x)
