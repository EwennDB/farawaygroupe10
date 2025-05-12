from Board import Board
from Card import Card
from helper import make_regions, make_sanctuaries, make_value_lists
from functions import *
from random import randint

def brute_force(path_instance) :
    '''brute_force toutes les possibilités d'une instance'''
    max = 0
    lst_regions, lst_sanctuaries = make_value_lists("../Sujet/Instances_hors_compétition/8_7_a.txt")

    regions = make_regions(lst_regions)
    sanctuaries = make_sanctuaries(lst_sanctuaries)

    lst = []

    for i in range(len(regions)):
        lst.append([])
        for j in range(len(regions)-1):
            lst[i].append([])
            for k in range(len(regions)-2):
                lst[i][j].append([])
                for l in range(len(regions)-3):
                    lst[i][j][k].append([])
                    for m in range(len(regions)-4):
                        lst[i][j][k][l].append([])
                        for n in range(len(regions)-5):
                            lst[i][j][k][l][m].append([])
                            for o in range(len(regions)-6):
                                lst[i][j][k][l][m][n].append([])
                                for p in range(len(regions)-7):
                                    lst[i][j][k][l][m][n][o] = Board(sanctuaries)


if __name__ == '__main__':

    lst_regions, lst_sanctuaries = make_value_lists("../Sujet/Instances_hors_compétition/8_7_a.txt")

    """lst = [i for i in range(1, 69)]

    cards = make_regions(lst)

    test = Board(lst_sanctuaries)

    for i in range(1, len(cards)+1):
        test.place_card(cards[-i])

    print(test)

    while(test.pos != -1):
        test.reveal_card()
    
    print(test.merveilles, test.score)"""

    brute_force("../Sujet/Instances_hors_compétition/8_7_a.txt")

    '''test = Board(make_sanctuaries(lst_sanctuaries))
    cards = make_regions(lst_regions)
    for i in range(8):
        nb = randint(0, len(cards) - 1)
        test.place_card(cards.pop(nb))

    print(test)

    while(test.pos != -1):
        test.reveal_card()
        print(test.score)
    test.calc_sanctuary_score()
    
    print(test.merveilles, test.score)'''