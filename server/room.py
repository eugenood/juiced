import json
import os

from juiced.stage import Stage


class Room:

    def __init__(self, room_id, configuration):
        
        self.room_id = room_id
        self.configuration = configuration

        self.stage = Stage(configuration)
        
        self.human_username = None
        self.robot_username = None

        self.human_actions = []
        self.robot_actions = []

        self.human_action = None
        self.robot_action = None

    def add_player(self, username):

        if self.human_username is None:
            self.human_username = username
        
        elif self.robot_username is None:
            self.robot_username = username

    def human_act(self, human_action):

        if self.human_action is None:
            self.human_action = human_action
        
        return self._act()

    def robot_act(self, robot_action):

        if self.robot_action is None:
            self.robot_action = robot_action
        
        return self._act()

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

        if not os.path.exists("trajectories"):
            os.makedirs("trajectories")

        trajectory_file = open("trajectories/" + self.room_id + ".json", "w")
        trajectory_file.write(json.dumps(history))
        trajectory_file.close()


    def _act(self):

        if self.human_action is None or self.robot_action is None:
            return False

        self.stage.human.act(self.human_action)
        self.stage.robot.act(self.robot_action)

        self.human_actions.append(self.human_action)
        self.robot_actions.append(self.robot_action)
        
        self.human_action = None
        self.robot_action = None

        return True
