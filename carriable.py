class Carriable: pass


class Fruit(Carriable): pass


class Apple(Fruit): pass


class Orange(Fruit): pass


class Cup(Carriable):

    FILLING_EMPTY = 0
    FILLING_APPLEJUICE = 1
    FILLING_ORANGEJUICE = 2

    def __init__(self):

        self.filling = Cup.FILLING_EMPTY
