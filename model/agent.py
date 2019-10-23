import json
import random

import numpy as np
import matplotlib.pyplot as plt

import torch
import torch.nn.functional as F
import torch.optim as optim

from model.buffer import ReplayBuffer
from model.network import QNetwork

BATCH_SIZE = 64
BUFFER_CAPACITY = 10000
DISCOUNT_FACTOR = 0.99
EPSILON_DECAY = 0.999
EPSILON_END = 0.01
EPSILON_START = 1.0
LEARNING_RATE = 0.0001
TARGET_UPDATE = 100
TOTAL_EPISODES = 100000

class DDQNAgent(object):

    def __init__(self, env):

        self.env = env
        self.epsilon = EPSILON_END
    
    def initialize_network(self, state_dict):

        dim_state = self.env.observation_space.shape
        dim_action = self.env.action_space.n
        
        self.policy_net = QNetwork(dim_state, dim_action).cuda()
        self.target_net = QNetwork(dim_state, dim_action).cuda()

        if state_dict is not None:
            self.policy_net.load_state_dict(state_dict)

        self.target_net.load_state_dict(self.policy_net.state_dict())
        self.target_net.eval()
    
    def act(self, state):

        if self.epsilon > EPSILON_END:
            self.epsilon = self.epsilon * EPSILON_DECAY

        if random.random() > self.epsilon:
            with torch.no_grad():
                return self.policy_net(state).max(1)[1].view(1)
        
        dim_action = self.env.action_space.n

        return torch.tensor([random.randrange(dim_action)], dtype=torch.int64).cuda()

    def initialize_training(self):

        self.optimizer = optim.Adam(self.policy_net.parameters(), lr=LEARNING_RATE)
        self.buffer = ReplayBuffer(BUFFER_CAPACITY)
        self.epsilon = EPSILON_START

        self.policy_net.train()

    def initialize_demo(self, demo_url):

        with open(demo_url) as demo_data:

            demo = json.load(demo_data)
            human_actions = demo['human_actions']

            state = self.env.reset()
            state = torch.from_numpy(state).float().cuda()

            cumulative_reward = 0

            for action in human_actions:

                action = torch.tensor([action], dtype=torch.int64).cuda()
                next_state, reward, done, _ = self.env.step((action.item(), 0))

                cumulative_reward = cumulative_reward + reward

                next_state = torch.from_numpy(next_state).float().cuda()
                reward = torch.tensor([reward], dtype=torch.float32).cuda()

                self.buffer.push(state, action, reward, next_state, done)
                self.buffer.push(state, action, reward, next_state, done)
                self.buffer.push(state, action, reward, next_state, done)
                self.buffer.push(state, action, reward, next_state, done)
                self.buffer.push(state, action, reward, next_state, done)
                
                state = next_state

                if done: break

            print(cumulative_reward)

        for i_episode in range(10000):

            self.optimize(debug=(i_episode % TARGET_UPDATE == 0))

            if i_episode % TARGET_UPDATE == 0:
                
                self.target_net.load_state_dict(self.policy_net.state_dict())
    
    def train(self, model_path):

        rewards = []

        for i_episode in range(TOTAL_EPISODES):

            state = self.env.reset()
            state = torch.from_numpy(state).float().cuda()

            cumulative_reward = 0
            
            while True:
                
                action = self.act(state)
                next_state, reward, done, _ = self.env.step((action.item(), 0))

                cumulative_reward = cumulative_reward + reward

                next_state = torch.from_numpy(next_state).float().cuda()
                reward = torch.tensor([reward], dtype=torch.float32).cuda()

                self.buffer.push(state, action, reward, next_state, done)
                self.optimize()
                
                state = next_state

                if done: break
            
            rewards.append(cumulative_reward)

            if cumulative_reward > 0: print(i_episode, cumulative_reward)

            if i_episode % TARGET_UPDATE == 0:
                
                torch.save(self.policy_net.state_dict(), model_path)
                self.target_net.load_state_dict(self.policy_net.state_dict())
                self.optimize(debug=True)
        
    def optimize(self, debug=False):

        if len(self.buffer) < BATCH_SIZE: return
    
        transitions = self.buffer.sample(BATCH_SIZE)
        batch = list(zip(*transitions))

        state_batch = torch.stack(batch[0])
        action_batch = torch.stack(batch[1])
        reward_batch = torch.stack(batch[2])
        next_state_batch = torch.stack(batch[3])

        non_final_mask = [not done for done in batch[4]]
        non_final_next_states = next_state_batch[non_final_mask]

        state_values = self.policy_net(state_batch).gather(1, action_batch)
        next_state_values = torch.zeros((BATCH_SIZE, 1)).cuda()

        next_actions = self.policy_net(non_final_next_states).max(1)[1].view(-1, 1)
        next_state_values[non_final_mask] = self.target_net(non_final_next_states).gather(1, next_actions).view(-1, 1)
        
        expected_state_values = reward_batch + (DISCOUNT_FACTOR * next_state_values)
        
        loss = F.smooth_l1_loss(state_values, expected_state_values)
        
        self.optimizer.zero_grad()
        loss.backward()
        
        for param in self.policy_net.parameters():
            param.grad.data.clamp_(-1, 1)
        
        self.optimizer.step()

    def initialize_testing(self):
        
        self.optimizer = None
        self.buffer = None
        self.epsilon = EPSILON_END

        self.policy_net.eval()
    
    def test(self):

        rewards = []

        for i_episode in range(TOTAL_EPISODES):

            state = self.env.reset()
            state = torch.from_numpy(state).float().cuda()

            cumulative_reward = 0
            
            while True:
                
                action = self.act(state)
                state, reward, done, _ = self.env.step((action.item(), 0))
                state = torch.from_numpy(state).float().cuda()

                cumulative_reward = cumulative_reward + reward

                if done: break
            
            rewards.append(cumulative_reward)

            if i_episode % TARGET_UPDATE == 0: print(i_episode, np.mean(rewards))
        
    def visualize_rewards(self, rewards):

        rewards = torch.tensor(rewards)
        
        plt.xlabel('Episode')
        plt.ylabel('Reward')

        plt.plot(rewards.numpy())

        if len(rewards) >= 100:

            means = rewards.unfold(0, 100, 1).mean(1).view(-1)
            means = torch.cat((torch.zeros(99), means))
            plt.plot(means.numpy())

        plt.show()

