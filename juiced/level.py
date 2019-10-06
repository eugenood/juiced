from juiced.carriable import Cup
from juiced.metadata import Metadata


class Level(object):

    @staticmethod
    def get_level(level_id):

        if level_id == 'small':
            return SmallWorld()

        if level_id == 'big':
            return BigWorld()

        if level_id == 'coop':
            return CoopWorld()

    def __init__(self,
                 stage_size=(2, 2),
                 human_location=(0, 0),
                 robot_location=(1, 1),
                 wall_locations=None,
                 table_locations=None,
                 cup_locations=None,
                 juicer_locations=None,
                 apple_storage_locations=None,
                 orange_storage_locations=None):

        self.metadata = Metadata()

        if orange_storage_locations is None:
            orange_storage_locations = []

        if apple_storage_locations is None:
            apple_storage_locations = []

        if juicer_locations is None:
            juicer_locations = []

        if cup_locations is None:
            cup_locations = []

        if table_locations is None:
            table_locations = []

        if wall_locations is None:
            wall_locations = []

        self.stage_size = stage_size
        self.human_location = human_location
        self.robot_location = robot_location
        self.wall_locations = wall_locations
        self.table_locations = table_locations
        self.cup_locations = cup_locations
        self.juicer_locations = juicer_locations
        self.apple_storage_locations = apple_storage_locations
        self.orange_storage_locations = orange_storage_locations

    def get_reward(self, stage):

        return 0

    def to_dict(self):

        return {

            "stage_size": self.stage_size,
            "human_location": self.human_location,
            "robot_location": self.robot_location,
            "wall_locations": self.wall_locations,
            "table_locations": self.table_locations,
            "cup_locations": self.cup_locations,
            "juicer_locations": self.juicer_locations,
            "apple_storage_locations": self.apple_storage_locations,
            "orange_storage_locations": self.orange_storage_locations

        }


class SmallWorld(Level):

    def __init__(self):

        super().__init__(stage_size=(4, 4),
                         human_location=(0, 0),
                         robot_location=(3, 3),
                         apple_storage_locations=[((1, 1), (2, 2))],
                         orange_storage_locations=[((1, 2), (2, 1))])

    def get_reward(self, stage):

        return 0


class BigWorld(Level):

    def __init__(self):

        super().__init__(stage_size=(10, 10),
                         human_location=(0, 0),
                         robot_location=(9, 9),
                         wall_locations=[(2, 7), (2, 6), (2, 5), (2, 4), (2, 3), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2)],
                         cup_locations=[(2, 0), (4, 0), (6, 0)],
                         juicer_locations=[(2, 9), (4, 9), (6, 9)],
                         apple_storage_locations=[((3, 0), (5, 0)), ((3, 3), (5, 3))],
                         orange_storage_locations=[((3, 9), (5, 9)), ((5, 6), (3, 6))])

    def get_reward(self, stage):

        return 0


class CoopWorld(Level):

    def __init__(self):

        super().__init__(stage_size=(9, 9),
                         human_location=(2, 5),
                         robot_location=(7, 5),
                         wall_locations=[(4, 0), (4, 1), (4, 2), (4, 6), (4, 7), (4, 8)],
                         table_locations=[(4, 3), (4, 4), (4, 5)],
                         cup_locations=[(0, 0), (1, 0), (2, 0)],
                         juicer_locations=[(7, 0), (8, 0), (9, 0)],
                         apple_storage_locations=[((0, 8), (1, 8))],
                         orange_storage_locations=[((0, 5), (1, 5))])

        self.has_rewarded = False

    def get_reward(self, stage):

        if self.has_rewarded:
            return 0

        entity = stage.get(0, 0)

        if isinstance(entity, Cup) and entity.filling == Cup.FILLING_APPLEJUICE:
            self.has_rewarded = True
            return 1

        else:
            return 0
