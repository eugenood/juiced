from gym cimport Env

cdef class JuicedEnv(Env):
  cdef str level_id
  cdef object stage
  cdef int reward_previous
  cdef int n_steps
  cdef object metadata
  cdef object observation_space
  cdef object action_space
  cpdef step(self, (int, int) action)
  cpdef reset(self)
  cpdef render(self, str mode = *, bint close = *)
