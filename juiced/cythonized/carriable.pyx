cdef class Carriable: pass


cdef class Apple(Carriable): pass


cdef class Orange(Carriable): pass


cdef class Cup(Carriable):

    FILLING_EMPTY = 0
    FILLING_APPLEJUICE = 1
    FILLING_ORANGEJUICE = 2

    def __init__(self):

        self.filling = Cup.FILLING_EMPTY
