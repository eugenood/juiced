import random

from juiced.level import Level
from juiced.metadata import Metadata
from juiced.stage import Stage


class JuicedEnv:

    MAX_ACTIONS = 5

    def __init__(self):

        self.reset()

        self.dim_state = (len(Metadata.entries), self.stage.height, self.stage.width)
        self.dim_action = 6
        self.dim_intention = 2

    def reset(self):

        intention = random.randint(0, 1)

        if intention == 0: self.stage = Stage(Level.create("bapple"))
        if intention == 1: self.stage = Stage(Level.create("borange"))

        state = self.stage.get_state()

        self.prev_state = state
        self.prev_reward = 0

        self.n_steps = 0

        return state, intention

    def step(self, human_action, robot_action):

        self.n_steps = self.n_steps + 1

        self.stage.human.act(human_action)
        self.stage.robot.act(robot_action)

        state = self.stage.get_state()
        reward = 0
        done = False

        if state == self.prev_state:

            done = True
            reward = reward - 10
        
        cumulative_reward = self.stage.get_reward()
        reward = reward + (cumulative_reward - self.prev_reward)

        done = done or (self.n_steps > JuicedEnv.MAX_ACTIONS)

        self.prev_state = state
        self.prev_reward = cumulative_reward

        return state, reward, done
