class Level:

    @staticmethod
    def create(level_id):

        if level_id == "small":
            return Level.SMALL

        if level_id == "large":
            return Level.LARGE

        if level_id == "split":
            return Level.SPLIT

        if level_id == "order":
            return Level.ORDER

        return Level.SMALL

    SMALL = {

        "stage_size": (4, 4),
        "human_location": (0, 0),
        "robot_location": (3, 3),
        "wall_locations": [],
        "table_locations": [],
        "cup_locations": [],
        "juicer_locations": [],
        "apple_storage_locations": [((1, 1), (2, 2))],
        "orange_storage_locations": [((1, 2), (2, 1))],
        "counter_locations": []

    }

    LARGE = {

        "stage_size": (10, 10),
        "human_location": (0, 0),
        "robot_location": (9, 9),
        "wall_locations": [(2, 7), (2, 6), (2, 5), (2, 4), (2, 3), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2)],
        "table_locations": [],
        "cup_locations": [(2, 0), (4, 0), (6, 0)],
        "juicer_locations": [(2, 9), (4, 9), (6, 9)],
        "apple_storage_locations": [((3, 0), (5, 0)), ((3, 3), (5, 3))],
        "orange_storage_locations": [((3, 9), (5, 9)), ((5, 6), (3, 6))],
        "counter_locations": []

    }

    SPLIT = {

        "stage_size": (9, 9),
        "human_location": (2, 5),
        "robot_location": (7, 5),
        "wall_locations": [(4, 0), (4, 1), (4, 2), (4, 6), (4, 7), (4, 8)],
        "table_locations": [(4, 3), (4, 4), (4, 5)],
        "cup_locations": [(0, 0), (1, 0), (2, 0)],
        "juicer_locations": [(7, 0), (8, 0), (9, 0)],
        "apple_storage_locations": [((0, 8), (0, 7))],
        "orange_storage_locations": [((0, 5), (0, 4))],
        "counter_locations": []

    }

    ORDER = {

        "stage_size": (9, 9),
        "human_location": (2, 5),
        "robot_location": (7, 5),
        "wall_locations": [(4, 0), (4, 1), (4, 2), (4, 6), (4, 7), (4, 8)],
        "table_locations": [(4, 3), (4, 4), (4, 5)],
        "cup_locations": [(0, 0), (1, 0), (2, 0)],
        "juicer_locations": [(7, 0), (8, 0), (9, 0)],
        "apple_storage_locations": [((0, 8), (0, 7))],
        "orange_storage_locations": [((0, 5), (0, 4))],
        "counter_locations": [(3, 0)]
    }
