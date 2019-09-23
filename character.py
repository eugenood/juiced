from carriable import Carriable
from interactable import Interactable


class Character:

    DIRECTION_UP = 0
    DIRECTION_DOWN = 1
    DIRECTION_LEFT = 2
    DIRECTION_RIGHT = 3

    ACTION_UP = 0
    ACTION_DOWN = 1
    ACTION_LEFT = 2
    ACTION_RIGHT = 3
    ACTION_INTERACT = 4

    def __init__(self, stage):

        self.direction = Character.DIRECTION_RIGHT
        self.carriage = None
        self.stage = stage

        self.action_mapping = {

            Character.ACTION_UP: Character.DIRECTION_UP,
            Character.ACTION_DOWN: Character.DIRECTION_DOWN,
            Character.ACTION_LEFT: Character.DIRECTION_LEFT,
            Character.ACTION_RIGHT: Character.DIRECTION_RIGHT,

        }

    def act(self, action):

        if action in self.action_mapping:

            if self.direction == self.action_mapping[action]:
                self._move(action)

            elif self.direction != self.action_mapping[action]:
                self.direction = self.action_mapping[action]

        elif action == Character.ACTION_INTERACT:
            self._interact()

    def _move(self, action):

        old_x, old_y = self.stage.find(self)
        new_x, new_y = self._get_next_position(old_x, old_y, action, use_action=True)

        self.stage.move(old_x, old_y, new_x, new_y)

    def _interact(self):

        interactor_x, interactor_y = self.stage.find(self)
        interactee_x, interactee_y = self._get_next_position(interactor_x, interactor_y, self.direction)

        interactee = self.stage.get(interactee_x, interactee_y)

        if interactee is None and self.carriage is not None:

            is_success = self.stage.add(self.carriage, interactee_x, interactee_y)

            if is_success:
                self.carriage = None

        elif isinstance(interactee, Carriable) and self.carriage is None:

            self.stage.remove(interactee_x, interactee_y)
            self.carriage = interactee

        elif isinstance(interactee, Interactable):
            interactee.interact(self)

    def _get_next_position(self, x, y, direction, use_action=False):

        if use_action:
            direction = self.action_mapping[direction]

        if direction == Character.DIRECTION_UP:
            return x - 1, y

        elif direction == Character.DIRECTION_DOWN:
            return x + 1, y

        elif direction == Character.DIRECTION_LEFT:
            return x, y - 1

        elif direction == Character.DIRECTION_RIGHT:
            return x, y + 1


class Human(Character): pass


class Robot(Character): pass
