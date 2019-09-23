from carriable import Apple, Cup, Fruit, Orange


class Interactable:

    def interact(self, interactor): pass


class Wall(Interactable): pass


class Storage(Interactable): pass


class AppleStorage(Storage):

    def __init__(self):

        self.is_open = False

    def interact(self, interactor):

        if self.is_open and interactor.carriage is None:
            interactor.carriage = Apple()


class OrangeStorage(Storage):

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
    FILLING_APPLE_JUICE = 1
    FILLING_ORANGE_JUICE = 2

    def __init__(self):

        self.filling = Juicer.FILLING_EMPTY

    def interact(self, interactor):

        if isinstance(interactor.carriage, Fruit):
            self._interact_with_fruit(interactor, interactor.carriage)

        elif isinstance(interactor.carriage, Cup):
            self._interact_with_cup(interactor.carriage)

    def _interact_with_fruit(self, interactor, fruit):

        if self.filling == Juicer.FILLING_EMPTY and isinstance(fruit, Apple):

            self.filling = Juicer.FILLING_APPLE_JUICE
            interactor.carriage = None

        elif self.filling == Juicer.FILLING_EMPTY and isinstance(fruit, Orange):

            self.filling = Juicer.FILLING_ORANGE_JUICE
            interactor.carriage = None

    def _interact_with_cup(self, cup):

        if self.filling == Juicer.FILLING_APPLE_JUICE and cup.filling == Cup.FILLING_EMPTY:

            self.filling = Juicer.FILLING_EMPTY
            cup.filling = Cup.FILLING_APPLEJUICE

        elif self.filling == Juicer.FILLING_ORANGE_JUICE and cup.filling == Cup.FILLING_EMPTY:

            self.filling = Juicer.FILLING_EMPTY
            cup.filling = Cup.FILLING_ORANGEJUICE

        elif self.filling == Juicer.FILLING_EMPTY and cup.filling == Cup.FILLING_APPLEJUICE:

            self.filling = Juicer.FILLING_APPLE_JUICE
            cup.filling = Cup.FILLING_EMPTY

        elif self.filling == Juicer.FILLING_EMPTY and cup.filling == Cup.FILLING_ORANGEJUICE:

            self.filling = Juicer.FILLING_ORANGE_JUICE
            cup.filling = Cup.FILLING_EMPTY
