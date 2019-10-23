import gym
import numpy as np

from gym import spaces

from juiced.level import Level
from juiced.metadata import Metadata
from juiced.stage import Stage

class JuicedEnv(gym.Env):

    def __init__(self, level_id):

        super(JuicedEnv, self).__init__()

        self.level_id = level_id
        self.stage = Stage(Level.create(self.level_id))

        self.reward_previous = 0
        self.n_steps = 0

        self.metadata = Metadata.get_instance()

        self.action_space = spaces.Tuple((spaces.Discrete(6), spaces.Discrete(6)))
        self.observation_space = spaces.Box(low=0, high=len(Metadata.urls), shape=(self.stage.height, self.stage.width), dtype=np.uint8)

        self.action_space.n = 6

    def step(self, action):

        self.n_steps = self.n_steps + 1

        self.stage.human.act(action[0])
        self.stage.robot.act(action[1])

        reward_current = self.stage.get_reward()
        reward_diff = reward_current - self.reward_previous
        self.reward_previous = reward_current

        state = self.stage.get_state()
        state = np.asarray(state)

        return state, reward_diff, self.n_steps > 100, {}
    
    def reset(self):

        self.stage = Stage(Level.create(self.level_id))

        self.reward_previous = 0
        self.n_steps = 0

        state = self.stage.get_state()
        state = np.asarray(state)

        return state

    def render(self, mode='human', close=False):

        print(self.stage.get_state())

