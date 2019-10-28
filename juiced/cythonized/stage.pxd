cdef class Stage:
  cdef:
    readonly dict level
    readonly int height, width
    public list grid, rewardables
    readonly object metadata
    public object human
    public object robot
  cpdef object get(self, int x, int y)
  cpdef bint add(self, object entity, int x, int y)
  cpdef object remove(self, int x, int y)
  cpdef bint move(self, int old_x, int old_y, int new_x, int new_y)
  cpdef (int, int) find(self, object entity)
  cpdef get_state(self)
  cpdef int get_reward(self)
  cpdef void _initialize_entities(self)
