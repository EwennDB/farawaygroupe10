from Board import Board
from helper import make_regions, make_sanctuaries, make_value_lists, add_sol, nnnnnnnnn
from functions import *
from random import randint
from solver import gradient_descent, gradient_descent_regions
import copy
from time import time


if __name__ == '__main__':
    for i in range(3, 4):
        filepath = f"../Sujet/Instances_compétition/competition_0{str(i)}.txt"

    # filepath = f"../Sujet/Instances_compétition/competition_10.txt"
        lst_regions, lst_sanctuaries = make_value_lists(filepath)

        print(lst_sanctuaries)
        #créé les cartes régions et sanctuaires
        sanctuaries = make_sanctuaries(lst_sanctuaries)
        regions = make_regions(lst_regions)
        regions2 = copy.deepcopy(regions)
        best = Board(sanctuaries)
        floor = 0

        startTime = time()
        timeToRun = 600
        endTime = startTime + timeToRun

        lst_boards = []
        while time() <= endTime:
            regions2 = copy.deepcopy(regions)
            current = Board(copy.deepcopy(sanctuaries))

            for j in range(8):
                a = randint(0, len(regions2)-1)
                current.place_card(regions2.pop(a))

            for j in range(current.nb_sanc):
                current.sanctuaries.append(current.sanctuaire_dispo.pop(0))

            tmp = gradient_descent(current)
            score = tmp.evaluate()
            if floor < score:
                print(f"try with : {score}")
                tmp = gradient_descent_regions(tmp, regions)
                if best.evaluate() < tmp.evaluate():
                    best = copy.deepcopy(tmp)
                    floor = best.evaluate()-5
                    print(f"new floor : {floor}")
                    print(f"NEW NEW best : {best.evaluate()}")


        add_sol(filepath, best)

        nnnnnnnnn()

        print(f"best : {best}")
        print(f"best score : {best.evaluate()}")