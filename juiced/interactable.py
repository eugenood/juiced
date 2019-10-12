from juiced.carriable import Apple, Cup, Orange
import random


class Interactable: pass


class Rewardable(Interactable): pass


class Wall(Interactable):

    def interact(self, interactor): pass


class Table(Interactable):

    def __init__(self):

        self.filling = None

    def interact(self, interactor):

        if self.filling is None and interactor.carriage is not None:

            self.filling = interactor.carriage
            interactor.carriage = None

        elif self.filling is not None and interactor.carriage is None:

            interactor.carriage = self.filling
            self.filling = None


class AppleStorage(Interactable):

    def __init__(self):

        self.is_open = False

    def interact(self, interactor):

        if self.is_open and interactor.carriage is None:
            interactor.carriage = Apple()


class OrangeStorage(Interactable):

    def __init__(self):

        self.is_open = False

    def interact(self, interactor):

        if self.is_open and interactor.carriage is None:
            interactor.carriage = Orange()


class StorageButton(Interactable):

    def __init__(self, storage):

        self.storage = storage

    def interact(self, interactor):

        self.storage.is_open = not self.storage.is_open


class Juicer(Interactable):

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


class Counter(Rewardable):

    CUSTOMER_CHICKEN = 0
    CUSTOMER_GORILLA = 1

    def __init__(self, reward_chicken=(1, 0), reward_gorilla=(0, 1)):

        self.customer = random.choice([Counter.CUSTOMER_CHICKEN, Counter.CUSTOMER_GORILLA])

        self.reward_chicken = reward_chicken
        self.reward_gorilla = reward_gorilla

        self.reward = 0

    def interact(self, interactor):

        if isinstance(interactor.carriage, Cup) and interactor.carriage.filling != Cup.FILLING_EMPTY:

            if self.customer == self.CUSTOMER_CHICKEN and interactor.carriage.filling == Cup.FILLING_APPLEJUICE:
                self.reward = self.reward + self.reward_chicken[0]

            elif self.customer == self.CUSTOMER_CHICKEN and interactor.carriage.filling == Cup.FILLING_ORANGEJUICE:
                self.reward = self.reward + self.reward_chicken[1]

            elif self.customer == self.CUSTOMER_GORILLA and interactor.carriage.filling == Cup.FILLING_APPLEJUICE:
                self.reward = self.reward + self.reward_gorilla[0]

            elif self.customer == self.CUSTOMER_GORILLA and interactor.carriage.filling == Cup.FILLING_ORANGEJUICE:
                self.reward = self.reward + self.reward_gorilla[1]

            self.customer = random.choice([Counter.CUSTOMER_CHICKEN, Counter.CUSTOMER_GORILLA])
            interactor.carriage.filling = Cup.FILLING_EMPTY
