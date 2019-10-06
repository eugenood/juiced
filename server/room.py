import json
import os

from juiced.character import Character
from juiced.stage import Stage


class Room:

    def __init__(self, room_id, level):
        
        self.room_id = room_id
        self.level = level

        self.stage = Stage(level)
        
        self.human_username = None
        self.robot_username = None

        self.human_actions = []
        self.robot_actions = []

    def add_player(self, username):

        if self.human_username is None:
            self.human_username = username
        
        elif self.robot_username is None:
            self.robot_username = username

    def human_act(self, human_action):

        self._act(human_action, Character.ACTION_NONE)

    def robot_act(self, robot_action):
        
        self._act(Character.ACTION_NONE, robot_action)

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
            "level": self.level.to_dict(),
            "human_actions": self.human_actions,
            "robot_actions": self.robot_actions

        }

        if not os.path.exists("trajectories"):
            os.makedirs("trajectories")

        trajectory_file = open("trajectories/" + self.room_id + ".json", "w")
        trajectory_file.write(json.dumps(history))
        trajectory_file.close()

    def _act(self, human_action, robot_action):

        self.stage.human.act(human_action)
        self.stage.robot.act(robot_action)

        self.human_actions.append(human_action)
        self.robot_actions.append(robot_action)
