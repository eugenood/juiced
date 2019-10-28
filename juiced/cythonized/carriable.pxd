cdef class Carriable: pass


cdef class Apple(Carriable):
   pass


cdef class Orange(Carriable):
   pass


cdef class Cup(Carriable):

    cdef:
       public int filling
