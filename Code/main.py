from Board import Board
from Card import Card
from helper import make_regions, make_sanctuaries, make_value_lists, add_with_order
from functions import *
from random import randint
from solver import gradient_descent, swap, brute_force
import copy


if __name__ == '__main__':


    # lst_regions = [1,27,22,33,47,53,66,67,68]
    # lst_sanctuaries = [103,108,109,111,118,120,122]

    # #créé les cartes régions et sanctuaires
    # test = Board(make_sanctuaries(lst_sanctuaries))
    # cards = make_regions(lst_regions)

    # #révèle les régions
    # for i in range(8):
    #     test.place_card(cards.pop(0))

    # #révèle les sanctuaires
    # for i in range(test.nb_sanc):
    #     test.add_sanctuary(test.sanctuaire_dispo[0])

    # test.count_all()
    # print(test.score)

    lst_regions, lst_sanctuaries = make_value_lists("../Sujet/Instances_hors_compétition/8_7_a.txt")

    #créé les cartes régions et sanctuaires
    test = Board(make_sanctuaries(lst_sanctuaries))
    cards = make_regions(lst_regions)

    #révèle les régions
    for i in range(8):
        test.place_card(cards.pop(0))

    for i in range(test.nb_sanc):
        test.sanctuaries.append(test.sanctuaire_dispo.pop(0))

    # print(test)

    gradient_descent(test, cards)

    