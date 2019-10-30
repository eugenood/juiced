class Level:

    @staticmethod
    def create(level_id):

        if level_id == "bapple":
            return Level.create_baby((5, 0, 20, 0))

        if level_id == "borange":
            return Level.create_baby((0, 5, 0, 20))

        if level_id == "sapple":
            return Level.create_simple((5, 0, 20, 0))

        if level_id == "sorange":
            return Level.create_simple((0, 5, 0, 20))

        return Level.create_simple((5, 5, 20, 20))

    @staticmethod
    def create_baby(reward_distribution):

        stage_size = (4, 3)
        human_location = (1, 1)
        robot_location = (2, 1)
        apple_locations = [(0, 1), (3, 1)]
        orange_locations = [(1, 2), (2, 2)]
        customer_locations = [(1, 0), (2, 0)]

        return {

            "stage_size": stage_size,
            "human_location": human_location,
            "robot_location": robot_location,
            "apple_locations": apple_locations,
            "orange_locations": orange_locations,
            "customer_locations": customer_locations,
            "reward_distribution": reward_distribution,

        }

    @staticmethod
    def create_simple(reward_distribution):

        stage_size = (4, 4)
        human_location = (1, 3)
        robot_location = (2, 3)
        apple_locations = [(0, 2), (3, 3)]
        orange_locations = [(0, 3), (3, 2)]
        customer_locations = [(1, 0), (2, 0)]

        return {

            "stage_size": stage_size,
            "human_location": human_location,
            "robot_location": robot_location,
            "apple_locations": apple_locations,
            "orange_locations": orange_locations,
            "customer_locations": customer_locations,
            "reward_distribution": reward_distribution,

        }
