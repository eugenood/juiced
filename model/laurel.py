import math
import random

import numpy as np

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

from juiced.character import Character
from juiced.level import Level
from juiced.stage import Stage


BATCH_SIZE = 128
BUFFER_SIZE = 200000
GAMMA = 1
EPS_START = 1.0
EPS_END = 0.0
EPS_DECAY = 10000
LEARNING_RATE = 2e-4
NUM_EPISODES = 20000
TARGET_UPDATE = 100
TIME_HORIZON = 15


ACTION_SPACE = [Character.ACTION_NONE,
                Character.ACTION_UP,
                Character.ACTION_DOWN,
                Character.ACTION_LEFT,
                Character.ACTION_RIGHT,
                Character.ACTION_INTERACT]


class ReplayBuffer(object):

    def __init__(self, capacity):

        self.capacity = capacity
        self.buffer = []
        self.position = 0

    def push(self, state, human_action, agent_action, reward, next_state):

        if len(self.buffer) < self.capacity: self.buffer.append(None)

        self.buffer[self.position] = (state, human_action, agent_action, reward, next_state)
        self.position = (self.position + 1) % self.capacity

    def sample(self, batch_size):

        return random.sample(self.buffer, batch_size)

    def __len__(self):

        return len(self.buffer)


class HumanModel(nn.Module):

    def __init__(self, width, height):

        super(HumanModel, self).__init__()

        self.cnn = nn.Conv2d(1, 10, (3, 3))
        self.lstm = nn.LSTM(10 * (width - 2) * (height - 2), 50)
        self.fcn = nn.Linear(50, 6)

    def forward(self, x):

        batch_size = x.shape[0]

        x = self.cnn(x)
        x = F.relu(x)
        x = x.reshape((batch_size, 1, -1))

        x, h = self.lstm(x)
        x = F.relu(x)
        x = x.reshape((batch_size, -1))

        return self.fcn(x)


human_policy = HumanModel(6, 6)
human_target = HumanModel(6, 6)

human_target.load_state_dict(human_policy.state_dict())
human_target.eval()

optimizer = optim.RMSprop(human_policy.parameters(), lr=LEARNING_RATE)
buffer = ReplayBuffer(BUFFER_SIZE)

steps_done = 0


def human_act(state):

    global steps_done

    eps_threshold = EPS_END + (EPS_START - EPS_END) * math.exp(-1. * steps_done / EPS_DECAY)
    steps_done = steps_done + 1

    if random.random() < eps_threshold: return random.choice(ACTION_SPACE)

    with torch.no_grad():

        q_values = human_policy(state).numpy()
        action = np.argmax(q_values)

        return action


total_reward = 0

for episode in range(NUM_EPISODES):

    stage = Stage(Level.create("small"))

    state = torch.Tensor(stage.get_state())
    state = state[None, None, :, :]

    reward_previous = 0

    for t in range(TIME_HORIZON):

        human_action = human_act(state)
        stage.human.act(human_action)

        next_state = torch.Tensor(stage.get_state())
        next_state = next_state[None, None, :, :]

        reward_current = stage.get_reward()
        reward_diff = reward_current - reward_previous
        reward_previous = reward_current

        buffer.push(state, human_action, Character.ACTION_NONE, reward_diff, next_state)

        state = next_state

        if len(buffer) < BATCH_SIZE: continue

        transitions = buffer.sample(BATCH_SIZE)
        batch = list(zip(*transitions))

        state_batch = torch.stack(batch[0]).squeeze(1)
        next_state_batch = torch.stack(batch[4]).squeeze(1)

        reward_batch = torch.Tensor(batch[3]).view((-1, 1))

        human_action_batch = torch.Tensor(batch[1]).type(torch.LongTensor).view((-1, 1))
        agent_action_batch = torch.Tensor(batch[2]).type(torch.LongTensor).view((-1, 1))

        state_action_values = human_policy(state_batch).gather(1, human_action_batch)
        next_state_values = human_target(next_state_batch).max(1)[0].view((-1, 1))
        expected_state_action_values = reward_batch + GAMMA * next_state_values

        loss = F.smooth_l1_loss(state_action_values, expected_state_action_values)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    if episode % TARGET_UPDATE == TARGET_UPDATE - 1:

        human_target.load_state_dict(human_policy.state_dict())
        print('{:5d}   {:6.2f}   {:0.5f}'.format(episode + 1, total_reward / TARGET_UPDATE, loss.item()))
        total_reward = 0
