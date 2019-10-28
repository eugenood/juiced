import gym
import torch

from model.agent import LaurelAgent

from juiced.env import JuicedEnv
from juiced.level import Level


if __name__ == "__main__":

    env = JuicedEnv("small")
    agent = LaurelAgent(env)

    agent.initialize_network(None)
    agent.initialize_training()
    agent.initialize_demo("trajectories/demo.small.json")
    agent.train("policy.pth")
