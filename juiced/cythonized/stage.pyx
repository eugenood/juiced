from character cimport Human, Robot
from interactable cimport AppleStorage, Juicer, OrangeStorage, StorageButton, Table, Wall, Chicken, Gorilla
from carriable cimport Cup, Apple, Orange
from metadata cimport Metadata

cdef class Stage:

    def __init__(self, level):

        self.level = level

        self.height = self.level["stage_size"][0]
        self.width = self.level["stage_size"][1]

        self.grid = [[None for _ in range(self.width)] for _ in range(self.height)]
        self.metadata = Metadata()

        self.rewardables = []

        self._initialize_characters()
        self._initialize_entities()

    cpdef object get(self, int x, int y):

        if x < 0 or x >= self.height: return None
        if y < 0 or y >= self.width: return None

        return self.grid[x][y]

    cpdef bint add(self, object entity, int x, int y):

        if x < 0 or x >= self.height: return False
        if y < 0 or y >= self.width: return False
        if self.grid[x][y] is not None: return False

        self.grid[x][y] = entity

        return True

    cpdef object remove(self, int x, int y):

        if x < 0 or x >= self.height: return None
        if y < 0 or y >= self.width: return None

        entity = self.grid[x][y]
        self.grid[x][y] = None

        return entity

    cpdef bint move(self, int old_x, int old_y, int new_x, int new_y):

        if new_x < 0 or new_x >= self.height: return False
        if new_y < 0 or new_y >= self.width: return False
        if self.grid[new_x][new_y] is not None: return False

        self.grid[new_x][new_y] = self.grid[old_x][old_y]
        self.grid[old_x][old_y] = None

        return True

    cpdef (int, int) find(self, object entity):
        cdef unsigned int x, y
        for x in range(self.height):
            for y in range(self.width):
                if self.grid[x][y] == entity:
                    return x, y

        return -1, -1

    cpdef get_state(self):

        cdef unsigned int x, y

        state = [[None for _ in range(self.width)] for _ in range(self.height)]

        for x in range(self.height):
            for y in range(self.width):
                item = self.get(x, y)
                state[x][y] = self.metadata[item].index

        return state

    cpdef int get_reward(self):
        cdef:
           int total_reward

        total_reward = 0

        for rewardable in self.rewardables:
            total_reward = total_reward + rewardable.reward

        return total_reward

    def _initialize_characters(self):

        self.human = Human(self)
        self.robot = Robot(self)

        self.add(self.human, self.level["human_location"][0], self.level["human_location"][1])
        self.add(self.robot, self.level["robot_location"][0], self.level["robot_location"][1])

    cpdef void _initialize_entities(self):

        for wall_location in self.level["wall_locations"]:
                self.add(Wall(), wall_location[0], wall_location[1])

        for apple_location in self.level["apple_locations"]:
            self.add(Apple(), apple_location[0], apple_location[1])

        for orange_location in self.level["orange_locations"]:
            self.add(Orange(), orange_location[0], orange_location[1])

        for cup_location in self.level["cup_locations"]:
            self.add(Cup(), cup_location[0], cup_location[1])

        for table_location in self.level["table_locations"]:
            self.add(Table(), table_location[0], table_location[1])

        for juicer_location in self.level["juicer_locations"]:
            self.add(Juicer(), juicer_location[0], juicer_location[1])

        for apple_storage_location, apple_storage_button_location in self.level["apple_storage_locations"]:

            apple_storage = AppleStorage()
            apple_storage_button = StorageButton(apple_storage)

            self.add(apple_storage, apple_storage_location[0], apple_storage_location[1])
            self.add(apple_storage_button, apple_storage_button_location[0], apple_storage_button_location[1])

        for orange_storage_location, orange_storage_button_location in self.level["orange_storage_locations"]:

            orange_storage = OrangeStorage()
            orange_storage_button = StorageButton(orange_storage)

            self.add(orange_storage, orange_storage_location[0], orange_storage_location[1])
            self.add(orange_storage_button, orange_storage_button_location[0], orange_storage_button_location[1])

        for chicken_location in self.level["chicken_locations"]:

            chicken = Chicken()

            self.rewardables.append(chicken)
            self.add(chicken, chicken_location[0], chicken_location[1])

        for gorilla_location in self.level["gorilla_locations"]:

            gorilla = Gorilla()

            self.rewardables.append(gorilla)
            self.add(gorilla, gorilla_location[0], gorilla_location[1])
