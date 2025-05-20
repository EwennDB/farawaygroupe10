from Board import Board
from helper import make_regions, make_sanctuaries, make_value_lists
from functions import *
from random import randint
from solver import gradient_descent
import copy


if __name__ == '__main__':

    lst_regions, lst_sanctuaries = make_value_lists("../Sujet/Instances_compétition/competition_10.txt")

    #créé les cartes régions et sanctuaires
    sanctuaries = make_sanctuaries(lst_sanctuaries)
    cards = make_regions(lst_regions)
    cards2 = copy.deepcopy(cards)
    best = Board(sanctuaries)

    lst_boards = []
    for i in range(60):
        cards2 = copy.deepcopy(cards)
        lst_boards.append(Board(copy.deepcopy(sanctuaries)))

        for j in range(8):
            a = randint(0, len(cards2)-1)
            lst_boards[i].place_card(cards2.pop(a))

        for j in range(lst_boards[i].nb_sanc):
            lst_boards[i].sanctuaries.append(lst_boards[i].sanctuaire_dispo.pop(0))

        tmp = gradient_descent(lst_boards[i], cards)
        if best.evaluate() < tmp.evaluate():
            best = tmp
            print(f"new best : {best.evaluate()}")

    print(f"best : {best}")
    print(f"best score : {best.evaluate()}")

