from Board import Board
from Card import Card
from helper import make_regions, make_sanctuaries, make_value_lists, add_with_order
from functions import *
from random import randint
from solver import gradient_descent, swap
import copy


if __name__ == '__main__':


    lst_regions = [68,17,59,28,14,23,8,25]
    lst_sanctuaries = [108, 116, 121]

    #créé les cartes régions et sanctuaires
    test = Board(make_sanctuaries(lst_sanctuaries))
    cards = make_regions(lst_regions)

    #révèle les régions
    for i in range(8):
        test.place_card(cards.pop(0))

    #révèle les sanctuaires
    for i in range(test.nb_sanc):
        test.add_sanctuary(test.sanctuaire_dispo[0])

    test.count_all()
    print(test.score)

    lst_regions = [68,17,59,28,14,23,8,25]
    lst_sanctuaries = [108, 116, 121, 123, 125, 130, 131]

    #créé les cartes régions et sanctuaires
    test = Board(make_sanctuaries(lst_sanctuaries))
    cards = make_regions(lst_regions)

    #révèle les régions
    for i in range(8):
        test.place_card(cards.pop(0))

    # print(test)

    gradient_descent(test)