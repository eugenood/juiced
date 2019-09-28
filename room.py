from juiced.stage import Stage


class Room:

    def __init__(self, room_id, configuration):

        self.room_id = room_id
        self.stage = Stage(configuration)

        self.human_username = None
        self.robot_username = None

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
    
    def _act(self):

        self.stage.human.act(self.human_action)
        self.stage.robot.act(self.robot_action)

        self.human_action = None
        self.robot_action = None

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
