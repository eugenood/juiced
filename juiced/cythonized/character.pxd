cdef class Character:
  cdef:
    public object stage
    public int direction
    public object carriage
    readonly dict movement_mapping
  cpdef void act(self, int action)
  cpdef void _move(self, int action)
  cpdef void _turn(self, int action)
  cpdef void _interact(self)

cdef class Human(Character):
  pass

cdef class Robot(Character):
  pass
