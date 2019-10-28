from gym cimport Env
import numpy as np
import gym

from level cimport Level
from metadata cimport Metadata
from stage cimport Stage


cdef class JuicedEnv(Env):

    def __init__(self, level_id):

        super(JuicedEnv, self).__init__()

        self.level_id = level_id
        self.stage = Stage(Level.create(self.level_id))

        self.reward_previous = 0
        self.n_steps = 0

        self.metadata = Metadata.get_instance()

        self.observation_space = gym.spaces.Box(low=0,
                                                high=len(Metadata.urls) - 1,
                                                shape=(self.stage.height, self.stage.width),
                                                dtype=np.uint8)

        self.action_space = gym.spaces.Tuple((gym.spaces.Discrete(6), gym.spaces.Discrete(6)))
        self.action_space.n = 6

    cpdef step(self, (int, int) action):

        cdef int reward_current, reward_diff
        cdef int[:,:] state
        self.n_steps = self.n_steps + 1

        self.stage.human.act(action[0])
        self.stage.robot.act(action[1])

        reward_current = self.stage.get_reward()
        reward_diff = reward_current - self.reward_previous
        self.reward_previous = reward_current

        state = np.asarray(self.stage.get_state())

        return state, reward_diff, self.n_steps > 100, {}

    cpdef reset(self):

        cdef int[:,:] state
        self.stage = Stage(Level.create(self.level_id))

        self.reward_previous = 0
        self.n_steps = 0

        state = np.asarray(self.stage.get_state())

        return state

    cpdef render(self, str mode='human', bint close=False):

        print(self.stage.get_state())
