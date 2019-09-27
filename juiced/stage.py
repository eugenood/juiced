import numpy as np

from juiced.character import Human, Robot
from juiced.interactable import AppleStorage, Cup, Juicer, OrangeStorage, StorageButton, Wall
from juiced.metadata import Metadata


class Stage:

    def __init__(self, configuration):

        self.height = configuration["stage"][0]
        self.width = configuration["stage"][1]

        self.grid = [[None for _ in range(self.width)] for _ in range(self.height)]
        self.metadata = Metadata()

        self._initialize_characters(configuration)
        self._initialize_entities(configuration)

    def get(self, x, y):

        if x < 0 or x >= self.height: return None
        if y < 0 or y >= self.width: return None

        return self.grid[x][y]

    def add(self, entity, x, y):

        if x < 0 or x >= self.height: return False
        if y < 0 or y >= self.width: return False
        if self.grid[x][y] is not None: return False

        self.grid[x][y] = entity

        return True

    def remove(self, x, y):

        if x < 0 or x >= self.height: return None
        if y < 0 or y >= self.width: return None

        entity = self.grid[x][y]
        self.grid[x][y] = None

        return entity

    def move(self, old_x, old_y, new_x, new_y):

        if new_x < 0 or new_x >= self.height: return False
        if new_y < 0 or new_y >= self.width: return False
        if self.grid[new_x][new_y] is not None: return False

        self.grid[new_x][new_y] = self.grid[old_x][old_y]
        self.grid[old_x][old_y] = None

        return True

    def find(self, entity):

        for x in range(self.height):
            for y in range(self.width):
                if self.grid[x][y] == entity:
                    return x, y

        return -1, -1

    def get_state(self):

        state = np.zeros((self.height, self.width), dtype=np.int8)

        for x in range(self.height):
            for y in range(self.width):
                item = self.get(x, y)
                state[x][y] = self.metadata[item].index

        return state

    def get_state_image(self):

        state_image = [[None for _ in range(self.width)] for _ in range(self.height)]

        for x in range(self.height):
            for y in range(self.width):
                item = self.get(x, y)
                state_image[x][y] = self.metadata[item].url

        return state_image

    def _initialize_characters(self, configuration):

        self.human = Human(self)
        self.robot = Robot(self)

        self.grid[configuration["human"][0]][configuration["human"][1]] = self.human
        self.grid[configuration["robot"][0]][configuration["robot"][1]] = self.robot

    def _initialize_entities(self, configuration):

        for wall_position in configuration["walls"]:
            self.add(Wall(), wall_position[0], wall_position[1])

        for cup_position in configuration["cups"]:
            self.add(Cup(), cup_position[0], cup_position[1])

        for juicer_position in configuration["juicers"]:
            self.add(Juicer(), juicer_position[0], juicer_position[1])

        for apple_storage_position, apple_storage_button_position in configuration["apple_storages"]:

            apple_storage = AppleStorage()
            apple_storage_button = StorageButton(apple_storage)

            self.add(apple_storage, apple_storage_position[0], apple_storage_position[1])
            self.add(apple_storage_button, apple_storage_button_position[0], apple_storage_button_position[1])

        for orange_storage_position, orange_storage_button_position in configuration["orange_storages"]:

            orange_storage = OrangeStorage()
            orange_storage_button = StorageButton(orange_storage)

            self.add(orange_storage, orange_storage_position[0], orange_storage_position[1])
            self.add(orange_storage_button, orange_storage_button_position[0], orange_storage_button_position[1])
