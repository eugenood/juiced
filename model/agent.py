import json
import random

import numpy as np
import matplotlib.pyplot as plt

import torch
import torch.nn.functional as F
import torch.optim as optim

from model.buffer import ReplayBuffer
from model.network import QNetwork, IntentionNetwork


BATCH_SIZE = 256
BUFFER_CAPACITY = 100000
DISCOUNT_FACTOR = 0.99
EPSILON_DECAY = 0.9999
EPSILON_END = 0.01
EPSILON_START = 1.0
LEARNING_RATE = 0.001
TARGET_UPDATE = 500
TOTAL_EPISODES = 250000


class LaurelAgent(object):

    # METHODS IN THIS CLASS
    # =====================
    # initialize_policy_network(human_policy_path, robot_policy_path)
    # initialize_intention_network(intention_net_path)
    # human_act(state, intention)
    # robot_act(state, intention)
    # initialize_policy_training()
    # initialize_intention_training()
    # train_policy(human_model_path, robot_model_path)
    # train_intention(intention_net_path)
    # initialize_policy_testing()
    # initialize_intention_testing()
    # convert_state(state)
    # convert_intention(intention)

    def __init__(self, env):

        self.env = env

        self.human_epsilon = EPSILON_END
        self.robot_epsilon = EPSILON_END
    
        self.dim_state = self.env.dim_state
        self.dim_action = self.env.dim_action
        self.dim_intention = self.env.dim_intention

    def initialize_policy_network(self, human_policy_path, robot_policy_path):

        self.human_policy_net = QNetwork(self.dim_state, self.dim_action, self.dim_intention).cuda()
        self.robot_policy_net = QNetwork(self.dim_state, self.dim_action, self.dim_intention).cuda()

        self.human_target_net = QNetwork(self.dim_state, self.dim_action, self.dim_intention).cuda()
        self.robot_target_net = QNetwork(self.dim_state, self.dim_action, self.dim_intention).cuda()

        if human_policy_path is not None:

            state_dict = torch.load(human_policy_path)
            self.human_policy_net.load_state_dict(state_dict)

        if robot_policy_path is not None:

            state_dict = torch.load(robot_policy_path)
            self.robot_policy_net.load_state_dict(state_dict)

        self.human_target_net.load_state_dict(self.human_policy_net.state_dict())
        self.robot_target_net.load_state_dict(self.robot_policy_net.state_dict())

        self.human_target_net.eval()
        self.robot_target_net.eval()

    def initialize_intention_network(self, intention_net_path):

        self.intention_net = IntentionNetwork(self.dim_state, self.dim_action, self.dim_intention).cuda()

        if intention_net_path is not None:

            state_dict = torch.load(intention_net_path)
            self.intention_net.load_state_dict(state_dict)
    
    def human_act(self, state, intention):

        if self.human_epsilon > EPSILON_END:
            self.human_epsilon = self.human_epsilon * EPSILON_DECAY

        if random.random() > self.human_epsilon:
            with torch.no_grad():
                return self.human_policy_net(state, intention).max(1)[1].view(1)
        
        return torch.tensor([random.randrange(self.dim_action)]).long().cuda()

    def robot_act(self, state, intention):

        if self.robot_epsilon > EPSILON_END:
            self.robot_epsilon = self.robot_epsilon * EPSILON_DECAY

        if random.random() > self.robot_epsilon:
            with torch.no_grad():
                return self.robot_policy_net(state, intention).max(1)[1].view(1)
        
        return torch.tensor([random.randrange(self.dim_action)]).long().cuda()

    def initialize_policy_training(self):

        self.buffer = ReplayBuffer(BUFFER_CAPACITY)

        self.human_optimizer = optim.Adam(self.human_policy_net.parameters(), lr=LEARNING_RATE)
        self.robot_optimizer = optim.Adam(self.robot_policy_net.parameters(), lr=LEARNING_RATE)

        self.human_epsilon = EPSILON_START
        self.robot_epsilon = EPSILON_START

        self.human_policy_net.train()
        self.robot_policy_net.train()

    def initialize_intention_training(self):

        self.intention_optimizer = optim.Adam(self.intention_net.parameters(), lr=LEARNING_RATE)
        self.intention_net.train()

    def train_policy(self, human_model_path, robot_model_path):

        rewards = []

        human_losses = []
        robot_losses = []

        for i_episode in range(TOTAL_EPISODES):

            state, intention = self.env.reset()
            state = self.convert_state(state)
            intention = self.convert_intention(intention)

            cumulative_reward = 0

            human_cumulative_loss = 0
            robot_cumulative_loss = 0
            
            while True:
                
                human_action = self.human_act(state, intention)
                robot_action = self.robot_act(state, intention)

                next_state, reward, done = self.env.step(human_action.item(), robot_action.item())

                cumulative_reward = cumulative_reward + reward

                next_state = self.convert_state(next_state)
                reward = torch.tensor([reward]).float().cuda()
                done = torch.tensor([done]).float().cuda()

                self.buffer.push(intention, state, human_action, robot_action, reward, next_state, done)

                if len(self.buffer) >= BATCH_SIZE:

                    human_loss, robot_loss = self.optimize_policy()

                    human_cumulative_loss = human_cumulative_loss + human_loss
                    robot_cumulative_loss = robot_cumulative_loss + robot_loss
                    
                state = next_state

                if done: break
            
            rewards.append(cumulative_reward)
            
            human_losses.append(human_cumulative_loss)
            robot_losses.append(robot_cumulative_loss)

            if i_episode % 100 == 0:

                average_human_loss = np.average(human_losses)
                average_robot_loss = np.average(robot_losses)

                average_reward = np.average(rewards)

                print("Training in progress... %06d/%06d  HLoss: %.6f  RLoss: %.6f  Reward: %.6f  Epsilon: %.6f" %
                        (i_episode, TOTAL_EPISODES, average_human_loss, average_robot_loss, average_reward, self.human_epsilon))

            if i_episode % TARGET_UPDATE == 0:

                torch.save(self.human_policy_net.state_dict(), human_model_path)
                torch.save(self.robot_policy_net.state_dict(), robot_model_path)

                self.human_target_net.load_state_dict(self.human_policy_net.state_dict())
                self.robot_target_net.load_state_dict(self.robot_policy_net.state_dict())

    def train_intention(self, intention_net_path):

        losses = []
        rewards = []

        for i_episode in range(TOTAL_EPISODES):

            self.intention_net.reset()

            state, intention = self.env.reset()
            state = self.convert_state(state)
            intention = self.convert_intention(intention)

            prev_human_action = torch.tensor([random.randrange(self.dim_action)]).long().cuda()
            prev_human_action = F.one_hot(prev_human_action, self.dim_action).float()

            cumulative_loss = 0
            cumulative_reward = 0
            
            while True:
                
                predicted_intention = self.intention_net(state, prev_human_action) 

                human_action = self.human_act(state, intention)
                robot_action = self.robot_act(state, predicted_intention)

                next_state, reward, done = self.env.step(human_action.item(), robot_action.item())

                cumulative_reward = cumulative_reward + reward

                next_state = self.convert_state(next_state)
                reward = torch.tensor([reward]).float().cuda()
                done = torch.tensor([done]).float().cuda()

                loss = F.binary_cross_entropy(predicted_intention, intention)
                self.intention_optimizer.zero_grad()
                loss.backward()

                self.intention_optimizer.step()

                state = next_state
                prev_human_action = F.one_hot(human_action, self.dim_action).float()
                cumulative_loss = cumulative_loss + loss.item()

                if done: break
            
            rewards.append(cumulative_reward)
            losses.append(cumulative_loss)

            if i_episode % 100 == 0:

                average_loss = np.average(losses)
                average_reward = np.average(rewards)

                print("Training in progress... %06d/%06d  Loss: %.6f  Reward: %.6f" %
                        (i_episode, TOTAL_EPISODES, average_loss, average_reward))

            if i_episode % TARGET_UPDATE == 0:

                torch.save(self.intention_net.state_dict(), intention_net_path)

    def optimize_policy(self):

        intention, state, human_action, robot_action, reward, next_state, done = self.buffer.sample(BATCH_SIZE)

        human_state_value = self.human_policy_net(state, intention).gather(1, human_action)
        robot_state_value = self.robot_policy_net(state, intention).gather(1, robot_action)

        human_next_action = self.human_policy_net(next_state, intention).max(1)[1].view(-1, 1)
        robot_next_action = self.robot_policy_net(next_state, intention).max(1)[1].view(-1, 1)

        human_next_state_value = self.human_target_net(next_state, intention).gather(1, human_next_action).view(-1, 1)
        robot_next_state_value = self.robot_target_net(next_state, intention).gather(1, robot_next_action).view(-1, 1)
        
        human_expected_state_value = reward + (DISCOUNT_FACTOR * human_next_state_value) * (1 - done)
        robot_expected_state_value = reward + (DISCOUNT_FACTOR * robot_next_state_value) * (1 - done)
        
        human_loss = F.smooth_l1_loss(human_state_value, human_expected_state_value)
        robot_loss = F.smooth_l1_loss(robot_state_value, robot_expected_state_value)
        
        self.human_optimizer.zero_grad()
        self.robot_optimizer.zero_grad()

        human_loss.backward()
        robot_loss.backward()

        self.human_optimizer.step()
        self.robot_optimizer.step()

        return human_loss.item(), robot_loss.item()

    def initialize_policy_testing(self):
        
        self.buffer = None

        self.human_optimizer = None
        self.robot_optimizer = None

        self.human_epsilon = EPSILON_END
        self.robot_epsilon = EPSILON_END

        self.human_policy_net.eval()
        self.robot_policy_net.eval()

    def initialize_intention_testing(self):

        self.intention_optimizer = None
        self.intention_net.eval()
    
    def convert_state(self, state):

        state = torch.tensor(state).long().cuda()
        state = F.one_hot(state, self.dim_state[0])
        state = state.permute(2, 0, 1).float()

        return state

    def convert_intention(self, intention):

        intention = torch.tensor(intention).long().cuda()
        intention = F.one_hot(intention, self.dim_intention)
        intention = intention.float()

        return intention
