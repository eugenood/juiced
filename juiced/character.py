from juiced.carriable import Carriable
from juiced.interactable import Interactable


class Character:

    DIRECTION_UP = 0
    DIRECTION_DOWN = 1
    DIRECTION_LEFT = 2
    DIRECTION_RIGHT = 3

    ACTION_NONE = 0
    ACTION_UP = 1
    ACTION_DOWN = 2
    ACTION_LEFT = 3
    ACTION_RIGHT = 4
    ACTION_INTERACT = 5

    def __init__(self, stage):

        self.stage = stage

        self.direction = Character.DIRECTION_RIGHT
        self.carriage = None

        self.movement_mapping = {

            Character.ACTION_UP: Character.DIRECTION_UP,
            Character.ACTION_DOWN: Character.DIRECTION_DOWN,
            Character.ACTION_LEFT: Character.DIRECTION_LEFT,
            Character.ACTION_RIGHT: Character.DIRECTION_RIGHT,

        }

    def act(self, action):

        if action == Character.ACTION_INTERACT:

            self._interact()

        elif action in self.movement_mapping:

            self._turn(action)
            self._move(action)

    def _move(self, action):

        old_x, old_y = self.stage.find(self)
        new_x, new_y = old_x, old_y

        if action == Character.ACTION_UP: new_x = old_x - 1
        if action == Character.ACTION_DOWN: new_x = old_x + 1
        if action == Character.ACTION_LEFT: new_y = old_y - 1
        if action == Character.ACTION_RIGHT: new_y = old_y + 1

        self.stage.move(old_x, old_y, new_x, new_y)

    def _turn(self, action):

        self.direction = self.movement_mapping[action]

    def _interact(self):

        interactor_x, interactor_y = self.stage.find(self)
        interactee_x, interactee_y = interactor_x, interactor_y

        if self.direction == Character.DIRECTION_UP: interactee_x = interactor_x - 1
        if self.direction == Character.DIRECTION_DOWN: interactee_x = interactor_x + 1
        if self.direction == Character.DIRECTION_LEFT: interactee_y = interactor_y - 1
        if self.direction == Character.DIRECTION_RIGHT: interactee_y = interactor_y + 1

        interactee = self.stage.get(interactee_x, interactee_y)

        if isinstance(interactee, Interactable):

            interactee.interact(self)

        elif isinstance(interactee, Carriable) and self.carriage is None:

            self.stage.remove(interactee_x, interactee_y)
            self.carriage = interactee

        elif interactee is None and self.carriage is not None:

            is_success = self.stage.add(self.carriage, interactee_x, interactee_y)

            if is_success:
                self.carriage = None


class Human(Character): pass


class Robot(Character): pass
