from Board import Board
from Card import Card
from helper import make_regions, make_sanctuaries, make_value_lists
from functions import *

if __name__ == '__main__':

    lst_regions, lst_sanctuaries = make_value_lists("../Sujet/Instances_hors_compétition/8_7_a.txt")

    cards = make_regions(lst_regions)
    sanctuaries = make_sanctuaries(lst_sanctuaries)

    test = Board()

    for i in cards:
        test.place_card(i)

    test.reveal_card()
    test.reveal_card()
    test.reveal_card()

    print(test.nuits, test.indices, test.couleurs, test.merveilles)