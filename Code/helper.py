import copy
import json
from Card import Card

def add_dict(dict1, dict2):
    dict3 = copy.deepcopy(dict2)
    for i, j in dict1.items():
        if i in dict3.keys():
            dict3[i] += j
        else:
            dict3[i] = j

    return dict3

def make_cards(lst) -> list:

    lst_cards = []

    with open("Data/cards.json", "r") as file:
        data = json.load(file)
        for i in lst:
            args = data[int(i)]

            lst_cards.append(Card(args[0], args[1], args[2], args[3], args[4], args[5]))

    return lst_cards

def make_sanctuaries(lst) -> list:

    lst_sanctuaries= []

    with open("Data/sanctuaire.json", "r") as file:
        data = json.load(file)
        for i in lst:
            args = data[int(i)-100]

            lst_sanctuaries.append(Card(args[0], args[1], args[2], args[3], args[4], args[5]))

    return lst_sanctuaries