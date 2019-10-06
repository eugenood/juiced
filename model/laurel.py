import torch
import torch.nn.functional as F
import torch.nn as nn


class HumanModel(nn.Module):

    def __init__(self):

        super(HumanModel, self).__init__()

        self.cnn = nn.Conv2d(1, 10, (3, 3))
        self.lstm = nn.LSTM(10 * 13 * 13, 50)
        self.fcn = nn.Linear(50, 5)

    def forward(self, x):

        x = self.cnn(x)
        x = F.relu(x)
        x = x.reshape((1, 1, -1))

        x, h = self.lstm(x)
        x = F.relu(x)
        x = x.reshape((1, -1))

        x = self.fcn(x)

        return x


human_model = HumanModel()
human_target = HumanModel()
human_target.load_state_dict(human_model.state_dict())

X = torch.randn((1, 1, 15, 15))
print(human_model(X))
print(human_target(X))
