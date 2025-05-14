from Board import Board
from Card import Card
from helper import make_regions, make_sanctuaries, make_value_lists, add_with_order
from functions import *
from random import randint
from solver import gradient_descent
import copy


if __name__ == '__main__':

    lst_regions = [19,66,68,39,51,16,32,38]
    lst_sanctuaries = [102,104,107,117,121]
    
    test = Board(make_sanctuaries(lst_sanctuaries))
    cards = make_regions(lst_regions)

    for i in range(8):
        test.place_card(cards.pop(0))

    for i in range(test.nb_sanc):
        test.add_sanctuary(test.sanctuaire_dispo[0])

    gradient_descent(test)