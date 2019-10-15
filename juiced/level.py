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

        if level_id == "maze":
            return Level.MAZE

        return Level.SMALL

    SMALL = {

        "stage_size": (6, 6),
        "human_location": (5, 0),
        "robot_location": (5, 1),
        "wall_locations": [],
        "table_locations": [],
        "cup_locations": [(4, 5)],
        "juicer_locations": [(0, 5)],
        "apple_storage_locations": [((0, 1), (0, 0))],
        "orange_storage_locations": [((0, 2), (0, 3))],
        "counter_locations": [(5, 5)]

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
        "juicer_locations": [(7, 0), (8, 0)],
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
        "cup_locations": [(0, 0), (0, 1)],
        "juicer_locations": [(8, 7), (8, 8)],
        "apple_storage_locations": [((0, 8), (0, 7))],
        "orange_storage_locations": [((0, 5), (0, 4))],
        "counter_locations": [(8, 0)]

    }

    MAZE = {

        "stage_size": (10, 10),
        "human_location": (9, 2),
        "robot_location": (2, 2),
        "wall_locations": [(9, 7), (8, 7), (7, 7), (5, 7), (9, 4), (8, 4), (7, 4), (6, 4), (5, 4)],
        "table_locations": [(6, 0), (6, 1), (6, 2)],
        "cup_locations": [(9, 0), (9,1)],
        "juicer_locations": [(7, 0)],
        "apple_storage_locations": [(9, 2)],
        "orange_storage_locations": [(8, 2)],
        "counter_locations": ([9, 5])

    }
