cdef class Entry:
  cdef:
    readonly int index
    readonly str url

cdef class Metadata:
  cdef:
    readonly Entry ground
    readonly Entry wall
    readonly Entry apple
    readonly Entry orange
    readonly dict cup, table, juicer, apple_storage, orange_storage
    readonly dict storage_button, counter, human, robot
    readonly Entry chicken, gorilla
