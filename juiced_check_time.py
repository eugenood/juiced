from juiced.character import Character as PyChar
from juiced.level import Level as PyLevel
from juiced.stage import Stage as PyStage

from character import Character as CyChar
from level import Level as CyLevel
from stage import Stage as CyStage

import time as time
import numpy as np
import random

# Set parameters
NUM_EPISODES = 1000
TIME_HORIZON = 25

ACTION_SPACE_Py = [PyChar.ACTION_NONE,
                PyChar.ACTION_UP,
                PyChar.ACTION_DOWN,
                PyChar.ACTION_LEFT,
                PyChar.ACTION_RIGHT,
                PyChar.ACTION_INTERACT]

level_str = "maze"

# Start timer
start_time_py = time.time()

for eps in range(NUM_EPISODES):

    # Start of episode
    stage = PyStage(PyLevel.create(level_str))

    # Loop through time steps
    for t in range(TIME_HORIZON):

        # Take random action
        stage.human.act(random.choice(ACTION_SPACE_Py))
        stage.get_state()
        stage.get_reward()

# End timer
time_taken_py = time.time() - start_time_py
print("Total time taken for Python = ", np.round(time_taken_py, 3), "seconds")

##### Cython #####

ACTION_SPACE_Cy = [CyChar.ACTION_NONE,
                CyChar.ACTION_UP,
                CyChar.ACTION_DOWN,
                CyChar.ACTION_LEFT,
                CyChar.ACTION_RIGHT,
                CyChar.ACTION_INTERACT]

# Start timer
start_time_cy = time.time()

for eps in range(NUM_EPISODES):

    # Start of episode
    stage = CyStage(CyLevel.create(level_str))

    # Loop through time steps
    for t in range(TIME_HORIZON):

        # Take random action
        stage.human.act(random.choice(ACTION_SPACE_Cy))
        stage.get_state()
        stage.get_reward()

# End timer
time_taken_cy = time.time() - start_time_cy
print("Total time taken for Cython = ", np.round(time_taken_cy, 3), "seconds")

# Comparison:
print("Cython is", np.round(time_taken_py / time_taken_cy, 3), "times faster than Python")
