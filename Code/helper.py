import copy
import json
from Card import Card
from functions import functions

def add_dict(dict1, dict2):
    dict3 = copy.deepcopy(dict2)
    for i, j in dict1.items():
        if i in dict3.keys():
            dict3[i] += j
        else:
            dict3[i] = j

    return dict3

def make_regions(lst) -> list:
    '''créé une liste d'object Carte régions avec les valeurs données dans la liste'''

    lst_cards = []

    with open("Data/cards.json", "r") as file:
        data = json.load(file)
        for i in lst:
            args = data[int(i)]

            lst_cards.append(Card(args[0], args[1], args[2], args[3], args[4], functions[args[5]]))

    return lst_cards

def make_sanctuaries(lst) -> list:
    '''créé une liste d'object Carte sanctuaires avec les valeurs données dans la liste'''

    lst_sanctuaries= []

    with open("Data/sanctuaire.json", "r") as file:
        data = json.load(file)
        for i in lst:
            args = data[int(i)-100]

            lst_sanctuaries.append(Card(args[0], args[1], args[2], args[3], args[4], args[5]))

    return lst_sanctuaries

def make_value_lists(filepath : str) -> tuple:
    '''lecture de fichier,
    retourne la liste des valeurs des cartes et celle des sanctuaires (dans cet ordre)'''

    with open(filepath, 'r') as file:
        for i in file:
            lst_card = i.strip().split(" ")
        
        c = 0

        while int(lst_card[c]) < 101:
            c += 1
        
        return lst_card[:c], lst_card[c:]

def nnnnnnnnn():
    pass