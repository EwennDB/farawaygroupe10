from Board import Board
from Card import Card
from helper import make_regions, make_sanctuaries, make_value_lists, add_with_order
from functions import *
from random import randint
import copy


if __name__ == '__main__':

    lst_regions, lst_sanctuaries = make_value_lists("../Sujet/Instances_hors_compétition/8_7_a.txt")

    lst = [i for i in range(1, 69)]

    cards = make_regions(lst)
    
    test = Board(make_sanctuaries(lst_sanctuaries))
    cards = make_regions(lst_regions)
    for i in range(8):
        nb = randint(0, len(cards) - 1)
        test.place_card(cards.pop(nb))

    for i in range(test.nb_sanc):
        test.add_sanctuary(test.sanctuaire_dispo[0])

    print(test)

    while(test.pos != -1):
        test.reveal_card()

    test.calc_sanctuary_score()
    
    print(test)