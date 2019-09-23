import numpy as np

from stage import Stage


class Room:

    def __init__(self, room_id, configuration):

        self.room_id = room_id
        self.stage = Stage(configuration)

        self.human_username = None
        self.robot_username = None

    def add_player(self, username):

        if self.human_username is None:
            self.human_username = username

        elif self.robot_username is None:
            self.robot_username = username

    def act(self, human_action, robot_action):

        self.stage.human.act(human_action)
        self.stage.robot.act(robot_action)

    def get_state_image(self):

        state_image = self.stage.get_state_image()

        for i in range(len(state_image)):
            for j in range(len(state_image[i])):
                state_image[i][j] = "../" + state_image[i][j]

        return state_image
