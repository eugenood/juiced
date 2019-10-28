from carriable cimport Apple, Cup, Orange
from character cimport Character, Human, Robot
from interactable cimport AppleStorage, Juicer, OrangeStorage, StorageButton, Wall, Table, Chicken, Gorilla


cdef class Entry:

    def __init__(self, url, meta):
        self.index = len(meta.urls)
        self.url = url


cdef class Metadata:

    urls = []

    def __init__(self):

        self.ground = self.create_Entry("misc/ground.png")
        self.wall = self.create_Entry("misc/wall.png")

        self.apple = self.create_Entry("fruit/apple.png")
        self.orange = self.create_Entry("fruit/orange.png")

        self.cup = {

            Cup.FILLING_EMPTY: self.create_Entry("cup/empty.png"),
            Cup.FILLING_APPLEJUICE: self.create_Entry("cup/applejuice.png"),
            Cup.FILLING_ORANGEJUICE: self.create_Entry("cup/orangejuice.png")

        }

        self.table = {

            "default": self.create_Entry("table/empty.png"),

            "apple": self.create_Entry("table/apple.png"),

            "orange": self.create_Entry("table/orange.png"),

            "cup": {

                Cup.FILLING_EMPTY: self.create_Entry("table/cup/empty.png"),
                Cup.FILLING_APPLEJUICE: self.create_Entry("table/cup/applejuice.png"),
                Cup.FILLING_ORANGEJUICE: self.create_Entry("table/cup/orangejuice.png")

            }

        }

        self.juicer = {

            Juicer.FILLING_EMPTY: self.create_Entry("juicer/empty.png"),
            Juicer.FILLING_APPLEJUICE: self.create_Entry("juicer/applejuice.png"),
            Juicer.FILLING_ORANGEJUICE: self.create_Entry("juicer/orangejuice.png")

        }

        self.apple_storage = {

            False: self.create_Entry("storage/apple/closed.png"),
            True: self.create_Entry("storage/apple/opened.png")

        }

        self.orange_storage = {

            False: self.create_Entry("storage/orange/closed.png"),
            True: self.create_Entry("storage/orange/opened.png")

        }

        self.storage_button = {

            AppleStorage: self.create_Entry("storage/apple/button.png"),
            OrangeStorage: self.create_Entry("storage/orange/button.png")

        }

        self.chicken = self.create_Entry("customer/chicken.png")
        self.gorilla = self.create_Entry("customer/gorilla.png")


        self.human = {

            "default": {

                Character.DIRECTION_UP: self.create_Entry("human/default/up.png"),
                Character.DIRECTION_DOWN: self.create_Entry("human/default/down.png"),
                Character.DIRECTION_LEFT: self.create_Entry("human/default/left.png"),
                Character.DIRECTION_RIGHT: self.create_Entry("human/default/right.png")

            },

            "apple": {

                Character.DIRECTION_UP: self.create_Entry("human/apple/up.png"),
                Character.DIRECTION_DOWN: self.create_Entry("human/apple/down.png"),
                Character.DIRECTION_LEFT: self.create_Entry("human/apple/left.png"),
                Character.DIRECTION_RIGHT: self.create_Entry("human/apple/right.png")

            },

            "orange": {

                Character.DIRECTION_UP: self.create_Entry("human/orange/up.png"),
                Character.DIRECTION_DOWN: self.create_Entry("human/orange/down.png"),
                Character.DIRECTION_LEFT: self.create_Entry("human/orange/left.png"),
                Character.DIRECTION_RIGHT: self.create_Entry("human/orange/right.png")

            },

            "cup": {

                Cup.FILLING_EMPTY: {

                    Character.DIRECTION_UP: self.create_Entry("human/cup/empty/up.png"),
                    Character.DIRECTION_DOWN: self.create_Entry("human/cup/empty/down.png"),
                    Character.DIRECTION_LEFT: self.create_Entry("human/cup/empty/left.png"),
                    Character.DIRECTION_RIGHT: self.create_Entry("human/cup/empty/right.png")

                },

                Cup.FILLING_ORANGEJUICE: {

                    Character.DIRECTION_UP: self.create_Entry("human/cup/orangejuice/up.png"),
                    Character.DIRECTION_DOWN: self.create_Entry("human/cup/orangejuice/down.png"),
                    Character.DIRECTION_LEFT: self.create_Entry("human/cup/orangejuice/left.png"),
                    Character.DIRECTION_RIGHT: self.create_Entry("human/cup/orangejuice/right.png")

                },

                Cup.FILLING_APPLEJUICE: {

                    Character.DIRECTION_UP: self.create_Entry("human/cup/applejuice/up.png"),
                    Character.DIRECTION_DOWN: self.create_Entry("human/cup/applejuice/down.png"),
                    Character.DIRECTION_LEFT: self.create_Entry("human/cup/applejuice/left.png"),
                    Character.DIRECTION_RIGHT: self.create_Entry("human/cup/applejuice/right.png")

                }

            }

        }

        self.robot = {

            "default": {

                Character.DIRECTION_UP: self.create_Entry("robot/default/up.png"),
                Character.DIRECTION_DOWN: self.create_Entry("robot/default/down.png"),
                Character.DIRECTION_LEFT: self.create_Entry("robot/default/left.png"),
                Character.DIRECTION_RIGHT: self.create_Entry("robot/default/right.png")

            },

            "apple": {

                Character.DIRECTION_UP: self.create_Entry("robot/apple/up.png"),
                Character.DIRECTION_DOWN: self.create_Entry("robot/apple/down.png"),
                Character.DIRECTION_LEFT: self.create_Entry("robot/apple/left.png"),
                Character.DIRECTION_RIGHT: self.create_Entry("robot/apple/right.png")

            },

            "orange": {

                Character.DIRECTION_UP: self.create_Entry("robot/orange/up.png"),
                Character.DIRECTION_DOWN: self.create_Entry("robot/orange/down.png"),
                Character.DIRECTION_LEFT: self.create_Entry("robot/orange/left.png"),
                Character.DIRECTION_RIGHT: self.create_Entry("robot/orange/right.png")

            },

            "cup": {

                Cup.FILLING_EMPTY: {

                    Character.DIRECTION_UP: self.create_Entry("robot/cup/empty/up.png"),
                    Character.DIRECTION_DOWN: self.create_Entry("robot/cup/empty/down.png"),
                    Character.DIRECTION_LEFT: self.create_Entry("robot/cup/empty/left.png"),
                    Character.DIRECTION_RIGHT: self.create_Entry("robot/cup/empty/right.png")

                },

                Cup.FILLING_ORANGEJUICE: {

                    Character.DIRECTION_UP: self.create_Entry("robot/cup/orangejuice/up.png"),
                    Character.DIRECTION_DOWN: self.create_Entry("robot/cup/orangejuice/down.png"),
                    Character.DIRECTION_LEFT: self.create_Entry("robot/cup/orangejuice/left.png"),
                    Character.DIRECTION_RIGHT: self.create_Entry("robot/cup/orangejuice/right.png")

                },

                Cup.FILLING_APPLEJUICE: {

                    Character.DIRECTION_UP: self.create_Entry("robot/cup/applejuice/up.png"),
                    Character.DIRECTION_DOWN: self.create_Entry("robot/cup/applejuice/down.png"),
                    Character.DIRECTION_LEFT: self.create_Entry("robot/cup/applejuice/left.png"),
                    Character.DIRECTION_RIGHT: self.create_Entry("robot/cup/applejuice/right.png")

                }

            }

        }

    def create_Entry(self, url):

        self.urls.append(url)

        return Entry(url, self)

    def __getitem__(self, entity):

        if entity is None:
            return self.ground

        elif isinstance(entity, Wall):
            return self.wall

        elif isinstance(entity, Apple):
            return self.apple

        elif isinstance(entity, Table) and entity.filling is None:
            return self.table["default"]

        elif isinstance(entity, Table) and isinstance(entity.filling, Apple):
            return self.table["apple"]

        elif isinstance(entity, Table) and isinstance(entity.filling, Orange):
            return self.table["orange"]

        elif isinstance(entity, Table) and isinstance(entity.filling, Cup):
            return self.table["cup"][entity.filling.filling]

        elif isinstance(entity, Orange):
            return self.orange

        elif isinstance(entity, Cup):
            return self.cup[entity.filling]

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
