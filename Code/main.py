from Board import Board
from Card import Card
from helper import make_regions, make_sanctuaries, make_value_lists
from functions import *
from random import randint

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

    test = Board(make_sanctuaries(lst_sanctuaries))
    cards = make_regions(lst_regions)
    for i in range(8):
        nb = randint(0, len(cards) - 1)
        test.place_card(cards.pop(nb))

    print(test)

    while(test.pos != -1):
        test.reveal_card()
        print(test.score)
    test.calc_sanctuary_score()
    
    print(test.merveilles, test.score)