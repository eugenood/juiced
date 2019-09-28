from json import dumps
from random import randint

from juiced.stage import Stage


class Room:

    def get_configuration():
        
        return {

            "stage": (10, 10),
            "human": (randint(0, 9), randint(0, 9)),
            "robot": (randint(0, 9), randint(0, 9)),
            "walls": [(2, 7), (2, 6), (2, 5), (2, 4), (2, 3), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2)],
            "cups": [(2, 0), (4, 0), (6, 0)],
            "juicers": [(2, 9), (4, 9), (6, 9)],
            "apple_storages": [((3, 0), (5, 0)), ((3, 3), (5, 3))],
            "orange_storages": [((3, 9), (5, 9)), ((5, 6), (3, 6))],

        }

    def __init__(self, room_id, configuration):
        
        self.room_id = room_id
        self.configuration = configuration

        self.stage = Stage(configuration)
        
        self.human_username = None
        self.robot_username = None
        
        self.human_action = None
        self.robot_action = None

        self.human_actions = []
        self.robot_actions = []

    def add_player(self, username):

        if self.human_username is None:
            self.human_username = username
        
        elif self.robot_username is None:
            self.robot_username = username

    def human_act(self, human_action):

        if self.human_action is None:
            self.human_action = human_action
        
        if self.robot_action is not None:
            self._act()
            return True
        
        return False

    def robot_act(self, robot_action):

        if self.robot_action is None:
            self.robot_action = robot_action
        
        if self.human_action is not None:
            self._act()
            return True
        
        return False

    def get_state(self, in_url=False):

        state = self.stage.get_state(in_url)

        if not in_url:
            return state

        for i in range(len(state)):
            for j in range(len(state[i])):
                state[i][j] = "../../images/" + state[i][j]

        return state

    def is_full(self):

        return self.human_username is not None and self.robot_username is not None

    def dump_history(self):
        
        history = {

            "room_id": self.room_id,
            "human_username": self.human_username,
            "robot_username": self.robot_username,
            "configuration": self.configuration,
            "human_actions": self.human_actions,
            "robot_actions": self.robot_actions

        }

        json = dumps(history)
        f = open(self.room_id + ".json", "w")
        f.write(json)
        f.close()


    def _act(self):

        self.stage.human.act(self.human_action)
        self.stage.robot.act(self.robot_action)

        self.human_actions.append(self.human_action)
        self.robot_actions.append(self.robot_action)
        
        self.human_action = None
        self.robot_action = None
