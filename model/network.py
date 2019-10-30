import torch

import torch.nn as nn
import torch.nn.functional as F


class QNetwork(nn.Module):
    
    def __init__(self, dim_state, dim_action, dim_intention):
        
        super(QNetwork, self).__init__()
        
        self.conv1 = nn.Conv2d(dim_state[0], 32, 1)
        self.conv2 = nn.Conv2d(32, 16, 3)

        dim_flatten = 16 * (dim_state[1] - 2) * (dim_state[2] - 2) + dim_intention

        self.fc1 = nn.Linear(dim_flatten, 64)
        self.fc2 = nn.Linear(64 ,32)
        self.fc3 = nn.Linear(32, dim_action)
    
    def forward(self, state, intention):
        
        is_batch = (state.ndim == 4)

        if not is_batch:
            
            state = state.unsqueeze(0)
            intention = intention.unsqueeze(0)

        x = F.relu(self.conv1(state))
        x = F.relu(self.conv2(x))
        x = x.flatten(1) 
        x = torch.cat((x, intention), 1)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        
        return self.fc3(x)


class IntentionNetwork(nn.Module):

    def __init__(self, dim_state, dim_action, dim_intention):

        super(IntentionNetwork, self).__init__()

        self.conv1 = nn.Conv2d(dim_state[0], 32, 1)
        self.conv2 = nn.Conv2d(32, 16, 3)

        dim_flatten = 16 * (dim_state[1] - 2) * (dim_state[2] - 2) + dim_action

        self.gru = nn.GRUCell(dim_flatten, 64)

        self.fc1 = nn.Linear(64, 32)
        self.fc2 = nn.Linear(32, dim_intention)
        
        self.hidden = None

    def forward(self, state, action):

        state = state.unsqueeze(0)

        x = F.relu(self.conv1(state))
        x = F.relu(self.conv2(x))
        x = x.flatten(1)
        x = torch.cat((x, action), 1)

        h = self.gru(x, self.hidden)

        x = F.relu(h)
        x = F.relu(self.fc1(x))
        x = F.softmax(self.fc2(x), 1)
        x = x.squeeze()

        self.hidden = h.detach()

        return x

    def reset(self):

        self.hidden = None
