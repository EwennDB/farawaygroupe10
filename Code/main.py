from Board import Board
from Card import Card
from helper import make_regions, make_sanctuaries, make_value_lists, add_with_order
from functions import *
from random import randint
import copy


if __name__ == '__main__':

    
    # lst_regions, lst_sanctuaries = make_value_lists("../Sujet/Instances_hors_compétition/8_7_a.txt")

    lst_regions = [19,66,68,39,51,16,32,38]
    lst_sanctuaries = [102,104,107,117,121]
    
    test = Board(make_sanctuaries(lst_sanctuaries))
    cards = make_regions(lst_regions)

    for i in range(8):
        test.place_card(cards.pop(0))

    for i in range(test.nb_sanc):
        test.add_sanctuary(test.sanctuaire_dispo[0])

    print(test)
    print(test.evaluate_board())
    while(test.pos != -1):
        test.reveal_card()
        print(test)

    test.calc_sanctuary_score()
    
    print(test)