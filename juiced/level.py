class Level:

    @staticmethod
    def create(level_id):

        if level_id == "small":
            return Level.SMALL

        if level_id == "large":
            return Level.LARGE

        if level_id == "split":
            return Level.SPLIT

        if level_id == "infer":
            return Level.INFER

        if level_id == "maze":
            return Level.MAZE

        return Level.SMALL

    SMALL = {

        "stage_size": (4, 3),
        "human_location": (0, 2),
        "robot_location": (1, 2),
        "wall_locations": [],
        "apple_locations": [],
        "orange_locations": [],
        "cup_locations": [],
        "table_locations": [],
        "juicer_locations": [],
        "apple_storage_locations": [((1, 0), (0, 0))],
        "orange_storage_locations": [((2, 0), (3, 0))],
        "chicken_locations": [(3, 2)],
        "gorilla_locations": []

    }

    LARGE = {

        "stage_size": (6, 6),
        "human_location": (5, 0),
        "robot_location": (5, 1),
        "wall_locations": [],
        "apple_locations": [],
        "orange_locations": [],
        "cup_locations": [(4, 5)],
        "table_locations": [],
        "juicer_locations": [(0, 5)],
        "apple_storage_locations": [((0, 1), (0, 0))],
        "orange_storage_locations": [((0, 2), (0, 3))],
        "chicken_locations": [(5, 5)],
        "gorilla_locations": []

    }

    SPLIT = {

        "stage_size": (9, 9),
        "human_location": (2, 5),
        "robot_location": (7, 5),
        "wall_locations": [(4, 0), (4, 1), (4, 2), (4, 6), (4, 7), (4, 8)],
        "apple_locations": [],
        "orange_locations": [],
        "cup_locations": [(0, 0), (1, 0), (2, 0)],
        "table_locations": [(4, 3), (4, 4), (4, 5)],
        "juicer_locations": [(8, 0)],
        "apple_storage_locations": [((0, 8), (0, 7))],
        "orange_storage_locations": [((0, 5), (0, 4))],
        "chicken_locations": [(8, 8)],
        "gorilla_locations": []

    }

    INFER = {

        "stage_size": (9, 9),
        "human_location": (7, 5),
        "robot_location": (2, 5),
        "wall_locations": [(4, 0), (4, 1), (4, 2), (4, 6), (4, 7), (4, 8)],
        "apple_locations": [],
        "orange_locations": [],
        "cup_locations": [(0, 0), (1, 0), (2, 0)],
        "table_locations": [(4, 3), (4, 4), (4, 5)],
        "juicer_locations": [(8, 0)],
        "apple_storage_locations": [((0, 8), (0, 7))],
        "orange_storage_locations": [((0, 5), (0, 4))],
        "chicken_locations": [(8, 8)],
        "gorilla_locations": []

    }

    MAZE = {

        "stage_size": (10, 10),
        "human_location": (3, 3),
        "robot_location": (9, 0),
        "wall_locations": [(7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8),
                           (6, 8), (5, 8), (4, 8), (3, 8), (2, 8), (1, 8),
                           (1, 7), (1, 6), (1, 5), (1, 4), (1, 3), (1, 2), (1, 1),
                           (2, 1), (3, 1), (4, 1), (5, 1),
                           (5, 2), (5, 3), (5, 4), (5, 5)],
        "apple_locations": [],
        "orange_locations": [],
        "cup_locations": [],
        "table_locations": [(8, 5), (9, 5)],
        "juicer_locations": [],
        "apple_storage_locations": [((8, 0), (8, 1)), ((2, 2), (2, 4))],
        "orange_storage_locations": [((8, 3), (8, 2)), ((4, 2), (4, 4))],
        "chicken_locations": [(9, 9)],
        "gorilla_locations": []

    }
