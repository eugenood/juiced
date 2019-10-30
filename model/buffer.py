import random
import torch


class ReplayBuffer(object):
    
    def __init__(self, capacity):
        
        self.capacity = capacity
        self.buffer = []
        self.position = 0

    def push(self, intention, state, human_action, robot_action, reward, next_state, done):

        if len(self.buffer) < self.capacity:
            self.buffer.append(None)

        self.buffer[self.position] = (intention, state, human_action, robot_action, reward, next_state, done)
        self.position = (self.position + 1) % self.capacity

    def sample(self, batch_size):

        transitions = random.sample(self.buffer, batch_size)
        batch = list(zip(*transitions))

        intention = torch.stack(batch[0])
        state = torch.stack(batch[1])
        human_action = torch.stack(batch[2])
        robot_action = torch.stack(batch[3])
        reward = torch.stack(batch[4])
        next_state = torch.stack(batch[5])
        done = torch.stack(batch[6])

        return intention, state, human_action, robot_action, reward, next_state, done

    def __len__(self):

        return len(self.buffer)
