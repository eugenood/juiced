from carriable import Cup, Apple, Orange, Fruit
from character import Character, Human, Robot
from interactable import AppleStorage, OrangeStorage, Wall, Juicer, StorageButton


class Metadata:

    def __init__(self, index, image_url):

        self.index = index
        self.image_url = image_url


class MetadataStore:

    def __init__(self):

        self.max_index = 40

        self.meta_ground = Metadata(0, "images/misc/ground.png")
        self.meta_wall = Metadata(1, "images/misc/wall.png")

        self.meta_apple = Metadata(2, "images/fruit/apple.png")
        self.meta_orange = Metadata(3, "images/fruit/orange.png")

        self.meta_cup = {

            Cup.FILLING_EMPTY: Metadata(4, "images/cup/empty.png"),
            Cup.FILLING_APPLEJUICE: Metadata(5, "images/cup/applejuice.png"),
            Cup.FILLING_ORANGEJUICE: Metadata(6, "images/cup/orangejuice.png")

        }

        self.meta_juicer = {

            Cup.FILLING_EMPTY: Metadata(7, "images/juicer/empty.png"),
            Cup.FILLING_APPLEJUICE: Metadata(8, "images/juicer/applejuice.png"),
            Cup.FILLING_ORANGEJUICE: Metadata(9, "images/juicer/orangejuice.png")

        }

        self.meta_apple_storage = {

            False: Metadata(10, "images/storage/apple/closed.png"),
            True: Metadata(11, "images/storage/apple/opened.png")

        }

        self.meta_orange_storage = {

            False: Metadata(12, "images/storage/orange/closed.png"),
            True: Metadata(13, "images/storage/orange/opened.png")

        }

        self.meta_storage_button = {

            AppleStorage: Metadata(14, "images/storage/apple/button.png"),
            OrangeStorage: Metadata(15, "images/storage/orange/button.png")

        }

        self.meta_human = {

            Character.DIRECTION_UP: Metadata(16, "images/human/default/up.png"),
            Character.DIRECTION_DOWN: Metadata(17, "images/human/default/down.png"),
            Character.DIRECTION_LEFT: Metadata(18, "images/human/default/left.png"),
            Character.DIRECTION_RIGHT: Metadata(19, "images/human/default/right.png")

        }

        self.meta_human_fruit = {

            Apple: {

                Character.DIRECTION_UP: Metadata(20, "images/human/apple/up.png"),
                Character.DIRECTION_DOWN: Metadata(21, "images/human/apple/down.png"),
                Character.DIRECTION_LEFT: Metadata(22, "images/human/apple/left.png"),
                Character.DIRECTION_RIGHT: Metadata(23, "images/human/apple/right.png")

            },

            Orange: {

                Character.DIRECTION_UP: Metadata(24, "images/human/orange/up.png"),
                Character.DIRECTION_DOWN: Metadata(25, "images/human/orange/down.png"),
                Character.DIRECTION_LEFT: Metadata(26, "images/human/orange/left.png"),
                Character.DIRECTION_RIGHT: Metadata(27, "images/human/orange/right.png")

            }

        }

        self.meta_human_cup = {

            Cup.FILLING_EMPTY: {

                Character.DIRECTION_UP: Metadata(28, "images/human/cup/empty/up.png"),
                Character.DIRECTION_DOWN: Metadata(29, "images/human/cup/empty/down.png"),
                Character.DIRECTION_LEFT: Metadata(30, "images/human/cup/empty/left.png"),
                Character.DIRECTION_RIGHT: Metadata(31, "images/human/cup/empty/right.png")

            },

            Cup.FILLING_ORANGEJUICE: {

                Character.DIRECTION_UP: Metadata(32, "images/human/cup/orangejuice/up.png"),
                Character.DIRECTION_DOWN: Metadata(33, "images/human/cup/orangejuice/down.png"),
                Character.DIRECTION_LEFT: Metadata(34, "images/human/cup/orangejuice/left.png"),
                Character.DIRECTION_RIGHT: Metadata(35, "images/human/cup/orangejuice/right.png")

            },

            Cup.FILLING_APPLEJUICE: {

                Character.DIRECTION_UP: Metadata(36, "images/human/cup/applejuice/up.png"),
                Character.DIRECTION_DOWN: Metadata(37, "images/human/cup/applejuice/down.png"),
                Character.DIRECTION_LEFT: Metadata(38, "images/human/cup/applejuice/left.png"),
                Character.DIRECTION_RIGHT: Metadata(39, "images/human/cup/applejuice/right.png")

            }

        }

        self.meta_robot = Metadata(40, "images/robot/robot.png")

    def get_metadata(self, entity):

        if entity is None:
            return self.meta_ground

        elif isinstance(entity, Wall):
            return self.meta_wall

        elif isinstance(entity, Apple):
            return self.meta_apple

        elif isinstance(entity, Orange):
            return self.meta_orange

        elif isinstance(entity, Cup):
            return self.meta_cup[entity.filling]

        elif isinstance(entity, Juicer):
            return self.meta_juicer[entity.filling]

        elif isinstance(entity, AppleStorage):
            return self.meta_apple_storage[entity.is_open]

        elif isinstance(entity, OrangeStorage):
            return self.meta_orange_storage[entity.is_open]

        elif isinstance(entity, StorageButton):
            return self.meta_storage_button[type(entity.storage)]

        elif isinstance(entity, Human) and entity.carriage is None:
            return self.meta_human[entity.direction]

        elif isinstance(entity, Human) and isinstance(entity.carriage, Fruit):
            return self.meta_human_fruit[type(entity.carriage)][entity.direction]

        elif isinstance(entity, Human) and isinstance(entity.carriage, Cup):
            return self.meta_human_cup[entity.carriage.filling][entity.direction]

        elif isinstance(entity, Robot):
            return self.meta_robot
