import gym
import torch

from model.agent import LaurelAgentV1
from model.env import JuicedEnv


if __name__ == "__main__":

    env = JuicedEnv()
    agent = LaurelAgentV1(env)

    agent.initialize_policy_network(None, None)
    agent.initialize_policy_training()
    agent.train_policy("human_policy.pth", "robot_policy.pth")
