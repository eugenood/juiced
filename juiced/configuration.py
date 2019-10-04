from random import randint


config_smallworld = {

    "stage": (4, 4),
    "human": (0, 0),
    "robot": (3, 3),
    "walls": [],
    "tables": [],
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
    "tables": [],
    "cups": [(2, 0), (4, 0), (6, 0)],
    "juicers": [(2, 9), (4, 9), (6, 9)],
    "apple_storages": [((3, 0), (5, 0)), ((3, 3), (5, 3))],
    "orange_storages": [((3, 9), (5, 9)), ((5, 6), (3, 6))]

}

config_coopworld = {

    "stage": (9, 9),
    "human": (2, 5),
    "robot": (7, 5),
    "walls": [(4, 0), (4, 1), (4, 2), (4, 6), (4, 7), (4, 8),],
    "tables": [(4, 3), (4, 4), (4, 5)],
    "cups": [(0, 0), (1, 0), (2, 0)],
    "juicers": [(7, 0), (8, 0), (9, 0)],
    "apple_storages": [((0, 8), (1, 8))],
    "orange_storages": [((0, 5), (1, 5))]

}