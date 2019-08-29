from flask import Flask, send_from_directory

import numpy as np

GRID_SIZE = (4, 4)

INITIAL_HUMAN_LOCATION = np.array([0, 0])
INITIAL_AGENT_LOCATION = np.array([3, 3])

INITIAL_GRAPE_LOCATIONS = [np.array([1, 1]), np.array([2, 2])]
INITIAL_MANGO_LOCATIONS = [np.array([1, 2]), np.array([2, 1])]

CELL_BLANK = 0
CELL_HUMAN = 1
CELL_AGENT = 2
CELL_GRAPE = 3
CELL_MANGO = 4

ACTION_UP = 0
ACTION_DOWN = 1
ACTION_LEFT = 2
ACTION_RIGHT = 3

TIME_HORIZON = 15

CELL_SPACE = [CELL_BLANK, CELL_HUMAN, CELL_AGENT, CELL_GRAPE, CELL_MANGO]
ACTION_SPACE = [ACTION_UP, ACTION_DOWN, ACTION_LEFT, ACTION_RIGHT]

class State(object):

    def __init__(self, human_location, agent_location, grape_locations, mango_locations):

        self.human_location = human_location
        self.agent_location = agent_location
        self.grape_locations = grape_locations
        self.mango_locations = mango_locations

        self.grid = np.zeros(GRID_SIZE, dtype=np.int8)

        for grape_location in self.grape_locations: self.grid[tuple(grape_location)] = CELL_GRAPE
        for mango_location in self.mango_locations: self.grid[tuple(mango_location)] = CELL_MANGO

        self.grid[tuple(self.human_location)] = CELL_HUMAN
        self.grid[tuple(self.agent_location)] = CELL_AGENT

    def step(self, human_action, agent_action, grape_reward=10, mango_reward=-10):

        human_location = self.human_location
        agent_location = self.agent_location

        def get_next_location(location, action):

            if action == ACTION_UP    and location[0] > 0:                return location - np.array([1, 0])
            if action == ACTION_DOWN  and location[0] < GRID_SIZE[0] - 1: return location + np.array([1, 0])
            if action == ACTION_LEFT  and location[1] > 0:                return location - np.array([0, 1])
            if action == ACTION_RIGHT and location[1] < GRID_SIZE[1] - 1: return location + np.array([0, 1])

            return location

        next_human_location = get_next_location(human_location, human_action)
        next_agent_location = get_next_location(agent_location, agent_action)

        if np.array_equal(next_human_location, next_agent_location):

            if not np.array_equal(next_agent_location, agent_location): next_agent_location = agent_location
            else: next_human_location = human_location

        grape_locations = self.grape_locations
        mango_locations = self.mango_locations

        next_grape_locations = []
        next_mango_locations = []

        reward = 0

        for grape_location in grape_locations:

            if np.array_equal(grape_location, next_human_location) or np.array_equal(grape_location, next_agent_location): reward = reward + grape_reward
            else: next_grape_locations.append(grape_location)

        for mango_location in mango_locations:

            if np.array_equal(mango_location, next_human_location) or np.array_equal(mango_location, next_agent_location): reward = reward + mango_reward
            else: next_mango_locations.append(mango_location)

        return reward, State(next_human_location, next_agent_location, next_grape_locations, next_mango_locations)

state = State(INITIAL_HUMAN_LOCATION, INITIAL_AGENT_LOCATION, INITIAL_GRAPE_LOCATIONS, INITIAL_MANGO_LOCATIONS)
total_reward = 0

app = Flask(__name__, static_url_path='')

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/start')
def start():
    global state
    state = State(INITIAL_HUMAN_LOCATION, INITIAL_AGENT_LOCATION, INITIAL_GRAPE_LOCATIONS, INITIAL_MANGO_LOCATIONS)
    return str(state.grid).replace(' ', ',')

@app.route('/move/<action>')
def move(action):
    global state, total_reward
    human_action = ACTION_SPACE[int(action)]
    agent_action = ACTION_DOWN
    reward, next_state = state.step(human_action, agent_action)
    total_reward = total_reward + reward
    state = next_state
    return str(state.grid).replace(' ', ',')
