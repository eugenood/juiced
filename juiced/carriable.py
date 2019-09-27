class Carriable: pass


class Apple(Carriable): pass


class Orange(Carriable): pass


class Cup(Carriable):

    FILLING_EMPTY = 0
    FILLING_APPLEJUICE = 1
    FILLING_ORANGEJUICE = 2

    def __init__(self):

        self.filling = Cup.FILLING_EMPTY
