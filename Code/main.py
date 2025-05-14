from Board import Board
from Card import Card
from helper import make_regions, make_sanctuaries, make_value_lists, add_with_order
from functions import *
from random import randint
from solver import gradient_descent
import copy


if __name__ == '__main__':

    lst_regions = [16,19,32,38,39,51,66,38]
    lst_sanctuaries = [102,103,104,105,106,107,108]
    
    test = Board(make_sanctuaries(lst_sanctuaries))
    cards = make_regions(lst_regions)

    for i in range(8):
        test.place_card(cards.pop(0))

    for i in range(test.nb_sanc):
        test.add_sanctuary(test.sanctuaire_dispo[0])

    print(test)

    gradient_descent(test)