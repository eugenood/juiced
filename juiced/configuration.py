from random import randint


config_smallworld = {

    "stage": (4, 4),
    "human": (0, 0),
    "robot": (3, 3),
    "walls": [],
    "cups": [],
    "juicers": [],
    "apple_storages": [((1, 1), (2, 2))],
    "orange_storages": [((1, 2), (2, 1))]

}


config_bigworld = {

    "stage": (10, 10),
    "human": (randint(0, 9), randint(0, 9)),
    "robot": (randint(0, 9), randint(0, 9)),
    "walls": [(2, 7), (2, 6), (2, 5), (2, 4), (2, 3), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2)],
    "cups": [(2, 0), (4, 0), (6, 0)],
    "juicers": [(2, 9), (4, 9), (6, 9)],
    "apple_storages": [((3, 0), (5, 0)), ((3, 3), (5, 3))],
    "orange_storages": [((3, 9), (5, 9)), ((5, 6), (3, 6))]

}
