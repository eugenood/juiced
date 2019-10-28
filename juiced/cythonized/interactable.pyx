from carriable cimport Apple, Cup, Orange
import random


cdef class Interactable: pass


cdef class Rewardable(Interactable): pass


cdef class Wall(Interactable):

    def interact(self, interactor): pass


cdef class Table(Interactable):

    def __init__(self):

        self.filling = None

    def interact(self, interactor):

        if self.filling is None and interactor.carriage is not None:

            self.filling = interactor.carriage
            interactor.carriage = None

        elif self.filling is not None and interactor.carriage is None:

            interactor.carriage = self.filling
            self.filling = None



cdef class AppleStorage(Interactable):

    def __init__(self):

        self.is_open = False

    def interact(self, interactor):

        if self.is_open and interactor.carriage is None:
            interactor.carriage = Apple()


cdef class OrangeStorage(Interactable):

    def __init__(self):

        self.is_open = False

    def interact(self, interactor):

        if self.is_open and interactor.carriage is None:
            interactor.carriage = Orange()


cdef class StorageButton(Interactable):

    def __init__(self, storage):

        self.storage = storage

    def interact(self, interactor):

        self.storage.is_open = not self.storage.is_open


cdef class Juicer(Interactable):

    FILLING_EMPTY = 0
    FILLING_APPLEJUICE = 1
    FILLING_ORANGEJUICE = 2

    def __init__(self):

        self.filling = Juicer.FILLING_EMPTY

    def interact(self, interactor):

        if isinstance(interactor.carriage, Apple):

            if self.filling == Juicer.FILLING_EMPTY:
                self.filling = Juicer.FILLING_APPLEJUICE
                interactor.carriage = None

        elif isinstance(interactor.carriage, Orange):

            if self.filling == Juicer.FILLING_EMPTY:
                self.filling = Juicer.FILLING_ORANGEJUICE
                interactor.carriage = None

        elif isinstance(interactor.carriage, Cup):

            if self.filling == Juicer.FILLING_APPLEJUICE and interactor.carriage.filling == Cup.FILLING_EMPTY:

                self.filling = Juicer.FILLING_EMPTY
                interactor.carriage.filling = Cup.FILLING_APPLEJUICE

            elif self.filling == Juicer.FILLING_ORANGEJUICE and interactor.carriage.filling == Cup.FILLING_EMPTY:

                self.filling = Juicer.FILLING_EMPTY
                interactor.carriage.filling = Cup.FILLING_ORANGEJUICE

            elif self.filling == Juicer.FILLING_EMPTY and interactor.carriage.filling == Cup.FILLING_APPLEJUICE:

                self.filling = Juicer.FILLING_APPLEJUICE
                interactor.carriage.filling = Cup.FILLING_EMPTY

            elif self.filling == Juicer.FILLING_EMPTY and interactor.carriage.filling == Cup.FILLING_ORANGEJUICE:

                self.filling = Juicer.FILLING_ORANGEJUICE
                interactor.carriage.filling = Cup.FILLING_EMPTY

cdef class Customer(Rewardable):

    def __init__(self, reward_distribution):

        self.reward_distribution = reward_distribution
        self.reward = 0

    def interact(self, interactor):

        if isinstance(interactor.carriage, Apple):

            self.reward = self.reward + self.reward_distribution[0]
            interactor.carriage = None

        elif isinstance(interactor.carriage, Orange):

            self.reward = self.reward + self.reward_distribution[1]
            interactor.carriage = None

        elif isinstance(interactor.carriage, Cup) and interactor.carriage.filling == Cup.FILLING_APPLEJUICE:

            self.reward = self.reward + self.reward_distribution[2]
            interactor.carriage.filling = Cup.FILLING_EMPTY

        elif isinstance(interactor.carriage, Cup) and interactor.carriage.filling == Cup.FILLING_ORANGEJUICE:

            self.reward = self.reward + self.reward_distribution[3]
            interactor.carriage.filling = Cup.FILLING_EMPTY


cdef class Chicken(Customer):

    def __init__(self):

        super().__init__((1, 0, 20, 5))


cdef class Gorilla(Customer):

    def __init__(self):

        super().__init__((0, 1, 5, 20))
