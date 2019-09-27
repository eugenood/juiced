from juiced.carriable import Apple, Cup, Orange
from juiced.character import Character, Human, Robot
from juiced.interactable import AppleStorage, Juicer, OrangeStorage, StorageButton, Wall


class MetadataEntry:

    def __init__(self, index, url):

        self.index = index
        self.url = url


class Metadata:

    def __init__(self):

        self.max_index = 40

        self.meta_ground = MetadataEntry(0, "misc/ground.png")
        self.meta_wall = MetadataEntry(1, "misc/wall.png")

        self.meta_apple = MetadataEntry(2, "fruit/apple.png")
        self.meta_orange = MetadataEntry(3, "fruit/orange.png")

        self.meta_cup = {

            Cup.FILLING_EMPTY: MetadataEntry(4, "cup/empty.png"),
            Cup.FILLING_APPLEJUICE: MetadataEntry(5, "cup/applejuice.png"),
            Cup.FILLING_ORANGEJUICE: MetadataEntry(6, "cup/orangejuice.png")

        }

        self.meta_juicer = {

            Juicer.FILLING_EMPTY: MetadataEntry(7, "juicer/empty.png"),
            Juicer.FILLING_APPLEJUICE: MetadataEntry(8, "juicer/applejuice.png"),
            Juicer.FILLING_ORANGEJUICE: MetadataEntry(9, "juicer/orangejuice.png")

        }

        self.meta_apple_storage = {
                
            False: MetadataEntry(10, "storage/apple/closed.png"),
            True: MetadataEntry(11, "storage/apple/opened.png")

        }

        self.meta_orange_storage = {

            False: MetadataEntry(12, "storage/orange/closed.png"),
            True: MetadataEntry(13, "storage/orange/opened.png")

        }

        self.meta_storage_button = {

            AppleStorage: MetadataEntry(14, "storage/apple/button.png"),
            OrangeStorage: MetadataEntry(15, "storage/orange/button.png")

        }

        self.meta_human = {

            "default": {

                Character.DIRECTION_UP: MetadataEntry(16, "human/default/up.png"),
                Character.DIRECTION_DOWN: MetadataEntry(17, "human/default/down.png"),
                Character.DIRECTION_LEFT: MetadataEntry(18, "human/default/left.png"),
                Character.DIRECTION_RIGHT: MetadataEntry(19, "human/default/right.png")

            },

            "apple": {

                Character.DIRECTION_UP: MetadataEntry(20, "human/apple/up.png"),
                Character.DIRECTION_DOWN: MetadataEntry(21, "human/apple/down.png"),
                Character.DIRECTION_LEFT: MetadataEntry(22, "human/apple/left.png"),
                Character.DIRECTION_RIGHT: MetadataEntry(23, "human/apple/right.png")

            },

            "orange": {

                Character.DIRECTION_UP: MetadataEntry(24, "human/orange/up.png"),
                Character.DIRECTION_DOWN: MetadataEntry(25, "human/orange/down.png"),
                Character.DIRECTION_LEFT: MetadataEntry(26, "human/orange/left.png"),
                Character.DIRECTION_RIGHT: MetadataEntry(27, "human/orange/right.png")

            },

            "cup": {

                Cup.FILLING_EMPTY: {

                    Character.DIRECTION_UP: MetadataEntry(28, "human/cup/empty/up.png"),
                    Character.DIRECTION_DOWN: MetadataEntry(29, "human/cup/empty/down.png"),
                    Character.DIRECTION_LEFT: MetadataEntry(30, "human/cup/empty/left.png"),
                    Character.DIRECTION_RIGHT: MetadataEntry(31, "human/cup/empty/right.png")

                },

                Cup.FILLING_ORANGEJUICE: {

                    Character.DIRECTION_UP: MetadataEntry(32, "human/cup/orangejuice/up.png"),
                    Character.DIRECTION_DOWN: MetadataEntry(33, "human/cup/orangejuice/down.png"),
                    Character.DIRECTION_LEFT: MetadataEntry(34, "human/cup/orangejuice/left.png"),
                    Character.DIRECTION_RIGHT: MetadataEntry(35, "human/cup/orangejuice/right.png")

                },

                Cup.FILLING_APPLEJUICE: {

                    Character.DIRECTION_UP: MetadataEntry(36, "human/cup/applejuice/up.png"),
                    Character.DIRECTION_DOWN: MetadataEntry(37, "human/cup/applejuice/down.png"),
                    Character.DIRECTION_LEFT: MetadataEntry(38, "human/cup/applejuice/left.png"),
                    Character.DIRECTION_RIGHT: MetadataEntry(39, "human/cup/applejuice/right.png")

                }

            }

        }

        self.meta_robot = {

            "default": {

                Character.DIRECTION_UP: MetadataEntry(40, "robot/default/up.png"),
                Character.DIRECTION_DOWN: MetadataEntry(41, "robot/default/down.png"),
                Character.DIRECTION_LEFT: MetadataEntry(42, "robot/default/left.png"),
                Character.DIRECTION_RIGHT: MetadataEntry(43, "robot/default/right.png")

            },

            "apple": {

                Character.DIRECTION_UP: MetadataEntry(44, "robot/apple/up.png"),
                Character.DIRECTION_DOWN: MetadataEntry(45, "robot/apple/down.png"),
                Character.DIRECTION_LEFT: MetadataEntry(46, "robot/apple/left.png"),
                Character.DIRECTION_RIGHT: MetadataEntry(47, "robot/apple/right.png")

            },

            "orange": {

                Character.DIRECTION_UP: MetadataEntry(48, "robot/orange/up.png"),
                Character.DIRECTION_DOWN: MetadataEntry(49, "robot/orange/down.png"),
                Character.DIRECTION_LEFT: MetadataEntry(50, "robot/orange/left.png"),
                Character.DIRECTION_RIGHT: MetadataEntry(51, "robot/orange/right.png")

            },

            "cup": {

                Cup.FILLING_EMPTY: {

                    Character.DIRECTION_UP: MetadataEntry(52, "robot/cup/empty/up.png"),
                    Character.DIRECTION_DOWN: MetadataEntry(53, "robot/cup/empty/down.png"),
                    Character.DIRECTION_LEFT: MetadataEntry(54, "robot/cup/empty/left.png"),
                    Character.DIRECTION_RIGHT: MetadataEntry(55, "robot/cup/empty/right.png")

                },

                Cup.FILLING_ORANGEJUICE: {

                    Character.DIRECTION_UP: MetadataEntry(56, "robot/cup/orangejuice/up.png"),
                    Character.DIRECTION_DOWN: MetadataEntry(57, "robot/cup/orangejuice/down.png"),
                    Character.DIRECTION_LEFT: MetadataEntry(58, "robot/cup/orangejuice/left.png"),
                    Character.DIRECTION_RIGHT: MetadataEntry(59, "robot/cup/orangejuice/right.png")

                },

                Cup.FILLING_APPLEJUICE: {

                    Character.DIRECTION_UP: MetadataEntry(60, "robot/cup/applejuice/up.png"),
                    Character.DIRECTION_DOWN: MetadataEntry(61, "robot/cup/applejuice/down.png"),
                    Character.DIRECTION_LEFT: MetadataEntry(62, "robot/cup/applejuice/left.png"),
                    Character.DIRECTION_RIGHT: MetadataEntry(63, "robot/cup/applejuice/right.png")

                }

            }

        }

    def __getitem__(self, entity):

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
            return self.meta_human["default"][entity.direction]

        elif isinstance(entity, Human) and isinstance(entity.carriage, Apple):
            return self.meta_human["apple"][entity.direction]

        elif isinstance(entity, Human) and isinstance(entity.carriage, Orange):
            return self.meta_human["orange"][entity.direction]

        elif isinstance(entity, Human) and isinstance(entity.carriage, Cup):
            return self.meta_human["cup"][entity.carriage.filling][entity.direction]

        elif isinstance(entity, Robot) and entity.carriage is None:
            return self.meta_robot["default"][entity.direction]

        elif isinstance(entity, Robot) and isinstance(entity.carriage, Apple):
            return self.meta_robot["apple"][entity.direction]

        elif isinstance(entity, Robot) and isinstance(entity.carriage, Orange):
            return self.meta_robot["orange"][entity.direction]

        elif isinstance(entity, Robot) and isinstance(entity.carriage, Cup):
            return self.meta_robot["cup"][entity.carriage.filling][entity.direction]
