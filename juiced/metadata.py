from juiced.carriable import Apple, Cup, Orange
from juiced.character import Character, Human, Robot
from juiced.interactable import AppleStorage, Juicer, OrangeStorage, StorageButton, Wall, Table


class MetadataEntry:

    _max_index = 0

    def __init__(self, url):

        MetadataEntry._max_index = MetadataEntry._max_index + 1

        self.index = MetadataEntry._max_index
        self.url = url


class Metadata:

    def __init__(self):

        self.meta_ground = MetadataEntry("misc/ground.png")
        self.meta_wall = MetadataEntry("misc/wall.png")
        self.meta_table = MetadataEntry("misc/table.png")

        self.meta_apple = MetadataEntry("fruit/apple.png")
        self.meta_orange = MetadataEntry("fruit/orange.png")

        self.meta_cup = {

            Cup.FILLING_EMPTY: MetadataEntry("cup/empty.png"),
            Cup.FILLING_APPLEJUICE: MetadataEntry("cup/applejuice.png"),
            Cup.FILLING_ORANGEJUICE: MetadataEntry("cup/orangejuice.png")

        }

        self.meta_juicer = {

            Juicer.FILLING_EMPTY: MetadataEntry("juicer/empty.png"),
            Juicer.FILLING_APPLEJUICE: MetadataEntry("juicer/applejuice.png"),
            Juicer.FILLING_ORANGEJUICE: MetadataEntry("juicer/orangejuice.png")

        }

        self.meta_apple_storage = {
                
            False: MetadataEntry("storage/apple/closed.png"),
            True: MetadataEntry("storage/apple/opened.png")

        }

        self.meta_orange_storage = {

            False: MetadataEntry("storage/orange/closed.png"),
            True: MetadataEntry("storage/orange/opened.png")

        }

        self.meta_storage_button = {

            AppleStorage: MetadataEntry("storage/apple/button.png"),
            OrangeStorage: MetadataEntry("storage/orange/button.png")

        }

        self.meta_human = {

            "default": {

                Character.DIRECTION_UP: MetadataEntry("human/default/up.png"),
                Character.DIRECTION_DOWN: MetadataEntry("human/default/down.png"),
                Character.DIRECTION_LEFT: MetadataEntry("human/default/left.png"),
                Character.DIRECTION_RIGHT: MetadataEntry("human/default/right.png")

            },

            "apple": {

                Character.DIRECTION_UP: MetadataEntry("human/apple/up.png"),
                Character.DIRECTION_DOWN: MetadataEntry("human/apple/down.png"),
                Character.DIRECTION_LEFT: MetadataEntry("human/apple/left.png"),
                Character.DIRECTION_RIGHT: MetadataEntry("human/apple/right.png")

            },

            "orange": {

                Character.DIRECTION_UP: MetadataEntry("human/orange/up.png"),
                Character.DIRECTION_DOWN: MetadataEntry("human/orange/down.png"),
                Character.DIRECTION_LEFT: MetadataEntry("human/orange/left.png"),
                Character.DIRECTION_RIGHT: MetadataEntry("human/orange/right.png")

            },

            "cup": {

                Cup.FILLING_EMPTY: {

                    Character.DIRECTION_UP: MetadataEntry("human/cup/empty/up.png"),
                    Character.DIRECTION_DOWN: MetadataEntry("human/cup/empty/down.png"),
                    Character.DIRECTION_LEFT: MetadataEntry("human/cup/empty/left.png"),
                    Character.DIRECTION_RIGHT: MetadataEntry("human/cup/empty/right.png")

                },

                Cup.FILLING_ORANGEJUICE: {

                    Character.DIRECTION_UP: MetadataEntry("human/cup/orangejuice/up.png"),
                    Character.DIRECTION_DOWN: MetadataEntry("human/cup/orangejuice/down.png"),
                    Character.DIRECTION_LEFT: MetadataEntry("human/cup/orangejuice/left.png"),
                    Character.DIRECTION_RIGHT: MetadataEntry("human/cup/orangejuice/right.png")

                },

                Cup.FILLING_APPLEJUICE: {

                    Character.DIRECTION_UP: MetadataEntry("human/cup/applejuice/up.png"),
                    Character.DIRECTION_DOWN: MetadataEntry("human/cup/applejuice/down.png"),
                    Character.DIRECTION_LEFT: MetadataEntry("human/cup/applejuice/left.png"),
                    Character.DIRECTION_RIGHT: MetadataEntry("human/cup/applejuice/right.png")

                }

            }

        }

        self.meta_robot = {

            "default": {

                Character.DIRECTION_UP: MetadataEntry("robot/default/up.png"),
                Character.DIRECTION_DOWN: MetadataEntry("robot/default/down.png"),
                Character.DIRECTION_LEFT: MetadataEntry("robot/default/left.png"),
                Character.DIRECTION_RIGHT: MetadataEntry("robot/default/right.png")

            },

            "apple": {

                Character.DIRECTION_UP: MetadataEntry("robot/apple/up.png"),
                Character.DIRECTION_DOWN: MetadataEntry("robot/apple/down.png"),
                Character.DIRECTION_LEFT: MetadataEntry("robot/apple/left.png"),
                Character.DIRECTION_RIGHT: MetadataEntry("robot/apple/right.png")

            },

            "orange": {

                Character.DIRECTION_UP: MetadataEntry("robot/orange/up.png"),
                Character.DIRECTION_DOWN: MetadataEntry("robot/orange/down.png"),
                Character.DIRECTION_LEFT: MetadataEntry("robot/orange/left.png"),
                Character.DIRECTION_RIGHT: MetadataEntry("robot/orange/right.png")

            },

            "cup": {

                Cup.FILLING_EMPTY: {

                    Character.DIRECTION_UP: MetadataEntry("robot/cup/empty/up.png"),
                    Character.DIRECTION_DOWN: MetadataEntry("robot/cup/empty/down.png"),
                    Character.DIRECTION_LEFT: MetadataEntry("robot/cup/empty/left.png"),
                    Character.DIRECTION_RIGHT: MetadataEntry("robot/cup/empty/right.png")

                },

                Cup.FILLING_ORANGEJUICE: {

                    Character.DIRECTION_UP: MetadataEntry("robot/cup/orangejuice/up.png"),
                    Character.DIRECTION_DOWN: MetadataEntry("robot/cup/orangejuice/down.png"),
                    Character.DIRECTION_LEFT: MetadataEntry("robot/cup/orangejuice/left.png"),
                    Character.DIRECTION_RIGHT: MetadataEntry("robot/cup/orangejuice/right.png")

                },

                Cup.FILLING_APPLEJUICE: {

                    Character.DIRECTION_UP: MetadataEntry("robot/cup/applejuice/up.png"),
                    Character.DIRECTION_DOWN: MetadataEntry("robot/cup/applejuice/down.png"),
                    Character.DIRECTION_LEFT: MetadataEntry("robot/cup/applejuice/left.png"),
                    Character.DIRECTION_RIGHT: MetadataEntry("robot/cup/applejuice/right.png")

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

        elif isinstance(entity, Table) and entity.filling is None:
            return self.meta_table

        elif isinstance(entity, Table) and entity.filling is not None:
            return self[entity.filling]

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
