import gym
import torch

from model.agent import LaurelAgent

from juiced.env import JuicedEnv
from juiced.level import Level

if __name__ == "__main__":

    # enable cuda

    device = torch.device("cuda")

    # create environment

    env = JuicedEnv("small")
    env.reset()

    # create agent

    agent = LaurelAgent(env)
    agent.initialize_network(None)
    agent.initialize_training()
    agent.initialize_demo("trajectories/demo.small.json")
    agent.train("./model/policy.pth")
