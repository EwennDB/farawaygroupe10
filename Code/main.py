from Board import Board
from Card import Card
from helper import make_regions, make_sanctuaries, make_value_lists
from functions import *

if __name__ == '__main__':

    lst_regions, lst_sanctuaries = make_value_lists("../Sujet/Instances_hors_compétition/8_7_a.txt")

    lst = [i for i in range(1, 69)]

    cards = make_regions(lst)

    test = Board()

    for i in range(1, len(cards)+1):
        test.place_card(cards[-i])

    print(test)

    while(test.pos != -1):
        test.reveal_card()
    
    print(test.merveilles, test.score)
    