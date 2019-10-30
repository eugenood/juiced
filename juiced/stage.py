from juiced.character import Human, Robot
from juiced.interactable import Apple, AppleStorage, Customer, Cup, Juicer, Orange, OrangeStorage, StorageButton, Table, Wall
from juiced.metadata import Metadata


class Stage:

    def __init__(self, level):

        self.height = level["stage_size"][0]
        self.width = level["stage_size"][1]

        self.grid = [[None for _ in range(self.width)] for _ in range(self.height)]
        self.metadata = Metadata.get_instance()

        self.rewardables = []

        self._initialize_characters(level)
        self._initialize_entities(level)

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

    def _initialize_characters(self, level):

        self.human = Human(self)
        self.robot = Robot(self)

        self.add(self.human, level["human_location"][0], level["human_location"][1])
        self.add(self.robot, level["robot_location"][0], level["robot_location"][1])

    def _initialize_entities(self, level):

        if "wall_locations" in level:
            for wall_location in level["wall_locations"]:
                self.add(Wall(), wall_location[0], wall_location[1])

        if "apple_locations" in level:
            for apple_location in level["apple_locations"]:
                self.add(Apple(), apple_location[0], apple_location[1])

        if "orange_locations" in level:
            for orange_location in level["orange_locations"]:
                self.add(Orange(), orange_location[0], orange_location[1])

        if "cup_locations" in level:
            for cup_location in level["cup_locations"]:
                self.add(Cup(), cup_location[0], cup_location[1])

        if "table_locations" in level:
            for table_location in level["table_locations"]:
                self.add(Table(), table_location[0], table_location[1])

        if "juicer_locations" in level:
            for juicer_location in level["juicer_locations"]:
                self.add(Juicer(), juicer_location[0], juicer_location[1])

        if "apple_storage_locations" in level:

            for apple_storage_location, apple_storage_button_location in level["apple_storage_locations"]:

                apple_storage = AppleStorage()
                apple_storage_button = StorageButton(apple_storage)

                self.add(apple_storage, apple_storage_location[0], apple_storage_location[1])
                self.add(apple_storage_button, apple_storage_button_location[0], apple_storage_button_location[1])

        if "orange_storage_locations" in level:

            for orange_storage_location, orange_storage_button_location in level["orange_storage_locations"]:

                orange_storage = OrangeStorage()
                orange_storage_button = StorageButton(orange_storage)

                self.add(orange_storage, orange_storage_location[0], orange_storage_location[1])
                self.add(orange_storage_button, orange_storage_button_location[0], orange_storage_button_location[1])

        if "customer_locations" in level:

            for customer_location in level["customer_locations"]:

                reward_distribution = level["reward_distribution"]
                customer = Customer(reward_distribution)

                self.rewardables.append(customer)
                self.add(customer, customer_location[0], customer_location[1])
