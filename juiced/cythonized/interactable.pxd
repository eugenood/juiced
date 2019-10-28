cdef class Interactable: pass

cdef class Rewardable(Interactable): pass

cdef class Wall(Interactable): pass

cdef class Table(Interactable):
  cdef public object filling

cdef class AppleStorage(Interactable):
  cdef public bint is_open

cdef class OrangeStorage(Interactable):
  cdef public bint is_open

cdef class StorageButton(Interactable):
  cdef readonly Interactable storage

cdef class Juicer(Interactable):
  cdef public int filling

cdef class Customer(Rewardable):
  cdef readonly tuple reward_distribution
  cdef public int reward

cdef class Chicken(Customer): pass

cdef class Gorilla(Customer): pass
