from Board import Board
from Card import Card
from helper import make_regions, make_sanctuaries, make_value_lists, add_with_order
from functions import *
from random import randint
from solver import gradient_descent, swap, brute_force
import copy


if __name__ == '__main__':


    lst_regions = [1,27,22,33,47,53,66,67,68]
    lst_sanctuaries = [103,108,109,111,118,120,122]

    #créé les cartes régions et sanctuaires
    test = Board(make_sanctuaries(lst_sanctuaries))
    cards = make_regions(lst_regions)

    # #révèle les régions
    # for i in range(8):
    #     test.place_card(cards.pop(0))

    # #révèle les sanctuaires
    # for i in range(test.nb_sanc):
    #     test.add_sanctuary(test.sanctuaire_dispo[0])

    # test.count_all()
    # print(test.score)

    lst_regions = [8,14,17,23,25,28,59,68]
    lst_sanctuaries = [108, 116, 121, 123, 125, 130, 131]

    #créé les cartes régions et sanctuaires
    test = Board(make_sanctuaries(lst_sanctuaries))
    cards = make_regions(lst_regions)

    #révèle les régions
    for i in range(8):
        test.place_card(cards.pop(0))

    for i in range(test.nb_sanc):
        test.sanctuaries.append(test.sanctuaire_dispo.pop(0))

    # print(test)

    brute_force("../Sujet/Instances_hors_compétition/test2.txt")

    