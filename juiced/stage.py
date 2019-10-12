from juiced.character import Human, Robot
from juiced.interactable import AppleStorage, Cup, Juicer, OrangeStorage, StorageButton, Table, Wall, Counter
from juiced.metadata import Metadata


class Stage:

    def __init__(self, level):

        self.level = level

        self.height = self.level["stage_size"][0]
        self.width = self.level["stage_size"][1]

        self.grid = [[None for _ in range(self.width)] for _ in range(self.height)]
        self.metadata = Metadata.get_instance()

        self.rewardables = []

        self._initialize_characters()
        self._initialize_entities()

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

        state = [[None for _ in range(self.width)] for _ in range(self.height)]

        for x in range(self.height):
            for y in range(self.width):
                item = self.get(x, y)
                state[x][y] = self.metadata[item].index

        return state

    def get_reward(self):

        total_reward = 0

        for rewardable in self.rewardables:
            total_reward = total_reward + rewardable.reward

        return total_reward

    def _initialize_characters(self):

        self.human = Human(self)
        self.robot = Robot(self)

        self.add(self.human, self.level["human_location"][0], self.level["human_location"][1])
        self.add(self.robot, self.level["robot_location"][0], self.level["robot_location"][1])

    def _initialize_entities(self):

        for wall_position in self.level["wall_locations"]:
            self.add(Wall(), wall_position[0], wall_position[1])

        for table_position in self.level["table_locations"]:
            self.add(Table(), table_position[0], table_position[1])

        for cup_position in self.level["cup_locations"]:
            self.add(Cup(), cup_position[0], cup_position[1])

        for juicer_position in self.level["juicer_locations"]:
            self.add(Juicer(), juicer_position[0], juicer_position[1])

        for apple_storage_position, apple_storage_button_position in self.level["apple_storage_locations"]:

            apple_storage = AppleStorage()
            apple_storage_button = StorageButton(apple_storage)

            self.add(apple_storage, apple_storage_position[0], apple_storage_position[1])
            self.add(apple_storage_button, apple_storage_button_position[0], apple_storage_button_position[1])

        for orange_storage_position, orange_storage_button_position in self.level["orange_storage_locations"]:

            orange_storage = OrangeStorage()
            orange_storage_button = StorageButton(orange_storage)

            self.add(orange_storage, orange_storage_position[0], orange_storage_position[1])
            self.add(orange_storage_button, orange_storage_button_position[0], orange_storage_button_position[1])

        for counter_position in self.level["counter_locations"]:

            counter = Counter()

            self.rewardables.append(counter)
            self.add(counter, counter_position[0], counter_position[1])
