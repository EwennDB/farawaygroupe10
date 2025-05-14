from Board import Board
from helper import make_regions, make_sanctuaries, make_value_lists, combinations
import copy
from random import randint

def brute_force(path_instance) :
    '''brute_force toutes les possibilités d'une instance,
    pas opti'''
    lst_regions, lst_sanctuaries = make_value_lists(path_instance)

    regions = make_regions(lst_regions)
    regions2 = copy.deepcopy(regions)
    sanctuaries = make_sanctuaries(lst_sanctuaries)

    lst = []
    best = Board(sanctuaries)

    cmb_lst = []

    for i in range(len(sanctuaries)+1):
        cmb_lst.append(combinations(len(sanctuaries), i))

    #create a board list
    for i in range(len(regions)):
        lst.append([])
        for j in range(len(regions)-1):
            lst[i].append([])
            for k in range(len(regions)-2):
                lst[i][j].append([])
                for l in range(len(regions)-3):
                    lst[i][j][k].append([])
                    for m in range(len(regions)-4):
                        lst[i][j][k][l].append([])
                        for n in range(len(regions)-5):
                            lst[i][j][k][l][m].append([])
                            for o in range(len(regions)-6):
                                lst[i][j][k][l][m][n].append([])
                                for p in range(len(regions)-7):
                                    current_plc = lst[i][j][k][l][m][n][o]
                                    current_plc = [Board(copy.deepcopy(sanctuaries))]
                                    current_plc[0].place_card(regions2.pop(i))
                                    current_plc[0].place_card(regions2.pop(j))
                                    current_plc[0].place_card(regions2.pop(k))
                                    current_plc[0].place_card(regions2.pop(l))
                                    current_plc[0].place_card(regions2.pop(m))
                                    current_plc[0].place_card(regions2.pop(n))
                                    current_plc[0].place_card(regions2.pop(o))
                                    current_plc[0].place_card(regions2.pop(p))
                                    current_plc.append(current_plc[0].copy())
                                    regions2 = copy.deepcopy(regions)

                                    for current_cmb in cmb_lst[current_plc[0].nb_sanc]:
                                        for q in range(len(current_cmb)):
                                            current_plc[0].add_sanctuary(current_plc[0].sanctuaire_dispo[current_cmb[q]-q])

                                        current_plc[0].reveal_all()

                                        current_plc[0].calc_sanctuary_score()

                                        if current_plc[0].score > best.score:
                                            best = current_plc[0]
                                            print(best)

                                        current_plc[0] = current_plc[1].copy()

    print(best)

def virer_inutile(filepath):
    '''vire les cartes inutiles (condition inatteignable)'''
    lst_regions, lst_sanctuaries = make_value_lists(filepath)
    print(lst_regions)
    regions = make_regions(lst_regions)
    sanctuaries = make_sanctuaries(lst_sanctuaries)
    b = Board(sanctuaries)
    b.place_all(lst_regions)
    for i in range(len(b.sanctuaire_dispo)):
        b.add_sanctuary(b.sanctuaire_dispo[0])
    b.reveal_all()
    for i in regions:
        if i.condition is not None:
            if not i.condition(b) and len(regions) > 8:
                regions.remove(i)
    for i in regions:
        print(i.value)
    return regions

def gradient_descent(board):
    '''trouve le meilleur arrangement des cartes régions et place les bons sanctuaires
    Nécessite un board'''
    d_score = 0
    swap_1 = randint(0,8)
    swap_2 = randint(0,8)

    o_score = board.evaluate()

    while swap_1 == swap_2:
        swap_2 = randint(0,8)

    tmp = board.cards[swap_1].copy()
    board.cards[swap_1] = board.cards[swap_2]
    board.cards[swap_2] = tmp

    if board.evaluate() > o_score:
        print(f"swapped cards nb {swap_1} and {swap_2}")
