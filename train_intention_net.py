import gym
import torch

from model.agent import LaurelAgentV1
from model.env import JuicedEnv


if __name__ == "__main__":

    env = JuicedEnv()
    agent = LaurelAgentV1(env)

    agent.initialize_policy_network("human_policy.pth", "robot_policy.pth")
    agent.initialize_intention_network("intention.pth")

    agent.initialize_policy_testing()
    agent.initialize_intention_training()

    agent.train_intention("intention.pth")
