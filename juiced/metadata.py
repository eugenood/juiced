from juiced.carriable import Apple, Cup, Orange
from juiced.character import Character, Human, Robot
from juiced.interactable import AppleStorage, Chicken, Gorilla, Juicer, OrangeStorage, StorageButton, Table, Wall


class Metadata:

    urls = []
    instance = None

    class Entry:

        def __init__(self, url):

            self.index = len(Metadata.urls)
            self.url = url

            Metadata.urls.append(url)

    @staticmethod
    def get_instance():

        if Metadata.instance is None:
            Metadata.instance = Metadata()

        return Metadata.instance

    def __init__(self):

        self.ground = Metadata.Entry("misc/ground.png")
        self.wall = Metadata.Entry("misc/wall.png")

        self.apple = Metadata.Entry("fruit/apple.png")
        self.orange = Metadata.Entry("fruit/orange.png")

        self.cup = {

            Cup.FILLING_EMPTY: Metadata.Entry("cup/empty.png"),
            Cup.FILLING_APPLEJUICE: Metadata.Entry("cup/applejuice.png"),
            Cup.FILLING_ORANGEJUICE: Metadata.Entry("cup/orangejuice.png")

        }

        self.table = {

            "default": Metadata.Entry("table/empty.png"),

            "apple": Metadata.Entry("table/apple.png"),

            "orange": Metadata.Entry("table/orange.png"),

            "cup": {

                Cup.FILLING_EMPTY: Metadata.Entry("table/cup/empty.png"),
                Cup.FILLING_APPLEJUICE: Metadata.Entry("table/cup/applejuice.png"),
                Cup.FILLING_ORANGEJUICE: Metadata.Entry("table/cup/orangejuice.png")

            }

        }

        self.juicer = {

            Juicer.FILLING_EMPTY: Metadata.Entry("juicer/empty.png"),
            Juicer.FILLING_APPLEJUICE: Metadata.Entry("juicer/applejuice.png"),
            Juicer.FILLING_ORANGEJUICE: Metadata.Entry("juicer/orangejuice.png")

        }

        self.apple_storage = {

            False: Metadata.Entry("storage/apple/closed.png"),
            True: Metadata.Entry("storage/apple/opened.png")

        }

        self.orange_storage = {

            False: Metadata.Entry("storage/orange/closed.png"),
            True: Metadata.Entry("storage/orange/opened.png")

        }

        self.storage_button = {

            AppleStorage: Metadata.Entry("storage/apple/button.png"),
            OrangeStorage: Metadata.Entry("storage/orange/button.png")

        }

        self.chicken = Metadata.Entry("customer/chicken.png")
        self.gorilla = Metadata.Entry("customer/gorilla.png")

        self.human = {

            "default": {

                Character.DIRECTION_UP: Metadata.Entry("human/default/up.png"),
                Character.DIRECTION_DOWN: Metadata.Entry("human/default/down.png"),
                Character.DIRECTION_LEFT: Metadata.Entry("human/default/left.png"),
                Character.DIRECTION_RIGHT: Metadata.Entry("human/default/right.png")

            },

            "apple": {

                Character.DIRECTION_UP: Metadata.Entry("human/apple/up.png"),
                Character.DIRECTION_DOWN: Metadata.Entry("human/apple/down.png"),
                Character.DIRECTION_LEFT: Metadata.Entry("human/apple/left.png"),
                Character.DIRECTION_RIGHT: Metadata.Entry("human/apple/right.png")

            },

            "orange": {

                Character.DIRECTION_UP: Metadata.Entry("human/orange/up.png"),
                Character.DIRECTION_DOWN: Metadata.Entry("human/orange/down.png"),
                Character.DIRECTION_LEFT: Metadata.Entry("human/orange/left.png"),
                Character.DIRECTION_RIGHT: Metadata.Entry("human/orange/right.png")

            },

            "cup": {

                Cup.FILLING_EMPTY: {

                    Character.DIRECTION_UP: Metadata.Entry("human/cup/empty/up.png"),
                    Character.DIRECTION_DOWN: Metadata.Entry("human/cup/empty/down.png"),
                    Character.DIRECTION_LEFT: Metadata.Entry("human/cup/empty/left.png"),
                    Character.DIRECTION_RIGHT: Metadata.Entry("human/cup/empty/right.png")

                },

                Cup.FILLING_ORANGEJUICE: {

                    Character.DIRECTION_UP: Metadata.Entry("human/cup/orangejuice/up.png"),
                    Character.DIRECTION_DOWN: Metadata.Entry("human/cup/orangejuice/down.png"),
                    Character.DIRECTION_LEFT: Metadata.Entry("human/cup/orangejuice/left.png"),
                    Character.DIRECTION_RIGHT: Metadata.Entry("human/cup/orangejuice/right.png")

                },

                Cup.FILLING_APPLEJUICE: {

                    Character.DIRECTION_UP: Metadata.Entry("human/cup/applejuice/up.png"),
                    Character.DIRECTION_DOWN: Metadata.Entry("human/cup/applejuice/down.png"),
                    Character.DIRECTION_LEFT: Metadata.Entry("human/cup/applejuice/left.png"),
                    Character.DIRECTION_RIGHT: Metadata.Entry("human/cup/applejuice/right.png")

                }

            }

        }

        self.robot = {

            "default": {

                Character.DIRECTION_UP: Metadata.Entry("robot/default/up.png"),
                Character.DIRECTION_DOWN: Metadata.Entry("robot/default/down.png"),
                Character.DIRECTION_LEFT: Metadata.Entry("robot/default/left.png"),
                Character.DIRECTION_RIGHT: Metadata.Entry("robot/default/right.png")

            },

            "apple": {

                Character.DIRECTION_UP: Metadata.Entry("robot/apple/up.png"),
                Character.DIRECTION_DOWN: Metadata.Entry("robot/apple/down.png"),
                Character.DIRECTION_LEFT: Metadata.Entry("robot/apple/left.png"),
                Character.DIRECTION_RIGHT: Metadata.Entry("robot/apple/right.png")

            },

            "orange": {

                Character.DIRECTION_UP: Metadata.Entry("robot/orange/up.png"),
                Character.DIRECTION_DOWN: Metadata.Entry("robot/orange/down.png"),
                Character.DIRECTION_LEFT: Metadata.Entry("robot/orange/left.png"),
                Character.DIRECTION_RIGHT: Metadata.Entry("robot/orange/right.png")

            },

            "cup": {

                Cup.FILLING_EMPTY: {

                    Character.DIRECTION_UP: Metadata.Entry("robot/cup/empty/up.png"),
                    Character.DIRECTION_DOWN: Metadata.Entry("robot/cup/empty/down.png"),
                    Character.DIRECTION_LEFT: Metadata.Entry("robot/cup/empty/left.png"),
                    Character.DIRECTION_RIGHT: Metadata.Entry("robot/cup/empty/right.png")

                },

                Cup.FILLING_ORANGEJUICE: {

                    Character.DIRECTION_UP: Metadata.Entry("robot/cup/orangejuice/up.png"),
                    Character.DIRECTION_DOWN: Metadata.Entry("robot/cup/orangejuice/down.png"),
                    Character.DIRECTION_LEFT: Metadata.Entry("robot/cup/orangejuice/left.png"),
                    Character.DIRECTION_RIGHT: Metadata.Entry("robot/cup/orangejuice/right.png")

                },

                Cup.FILLING_APPLEJUICE: {

                    Character.DIRECTION_UP: Metadata.Entry("robot/cup/applejuice/up.png"),
                    Character.DIRECTION_DOWN: Metadata.Entry("robot/cup/applejuice/down.png"),
                    Character.DIRECTION_LEFT: Metadata.Entry("robot/cup/applejuice/left.png"),
                    Character.DIRECTION_RIGHT: Metadata.Entry("robot/cup/applejuice/right.png")

                }

            }

        }

    def __getitem__(self, entity):

        if entity is None:
            return self.ground

        elif isinstance(entity, Wall):
            return self.wall

        elif isinstance(entity, Apple):
            return self.apple

        elif isinstance(entity, Orange):
            return self.orange

        elif isinstance(entity, Cup):
            return self.cup[entity.filling]

        elif isinstance(entity, Table) and entity.filling is None:
            return self.table["default"]

        elif isinstance(entity, Table) and isinstance(entity.filling, Apple):
            return self.table["apple"]

        elif isinstance(entity, Table) and isinstance(entity.filling, Orange):
            return self.table["orange"]

        elif isinstance(entity, Table) and isinstance(entity.filling, Cup):
            return self.table["cup"][entity.filling.filling]

        elif isinstance(entity, Juicer):
            return self.juicer[entity.filling]

        elif isinstance(entity, AppleStorage):
            return self.apple_storage[entity.is_open]

        elif isinstance(entity, OrangeStorage):
            return self.orange_storage[entity.is_open]

        elif isinstance(entity, StorageButton):
            return self.storage_button[type(entity.storage)]

        elif isinstance(entity, Chicken):
            return self.chicken

        elif isinstance(entity, Gorilla):
            return self.gorilla

        elif isinstance(entity, Human) and entity.carriage is None:
            return self.human["default"][entity.direction]

        elif isinstance(entity, Human) and isinstance(entity.carriage, Apple):
            return self.human["apple"][entity.direction]

        elif isinstance(entity, Human) and isinstance(entity.carriage, Orange):
            return self.human["orange"][entity.direction]

        elif isinstance(entity, Human) and isinstance(entity.carriage, Cup):
            return self.human["cup"][entity.carriage.filling][entity.direction]

        elif isinstance(entity, Robot) and entity.carriage is None:
            return self.robot["default"][entity.direction]

        elif isinstance(entity, Robot) and isinstance(entity.carriage, Apple):
            return self.robot["apple"][entity.direction]

        elif isinstance(entity, Robot) and isinstance(entity.carriage, Orange):
            return self.robot["orange"][entity.direction]

        elif isinstance(entity, Robot) and isinstance(entity.carriage, Cup):
            return self.robot["cup"][entity.carriage.filling][entity.direction]
