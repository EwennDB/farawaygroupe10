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

                                        current_plc[0].reveal_all_regions()

                                        current_plc[0].calc_all_sanctuary_score()

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
    nb_iter = 10
    #stocke le meilleur board pour pouvoir revenir en arrière
    best = board.copy()
    current_score = board.evaluate()
    print(f"base score is : {current_score}")

    for i in range(nb_iter):
        print(board)
        board.repr_ressources()
        # fait un swap random nb_iter fois
        d_score, swap_1, swap_2 = swap_random(board)
        print(f"swapped cards nb {swap_1} and {swap_2} and improved of {d_score}")

        # si le swap s'avère défavorable, on repart en arrière
        if d_score <= 0:
            board = best.copy()
            print("reversed")

        # si il s'avère bénéfique, on le garde
        else:
            best = board.copy()
            print(board)
            current_score += d_score

        print(f"new score : {current_score}")
    print(f"score : {board.evaluate()}")
    print(best)


def swap_random(board):
    '''swap 2 cartes au hasard
    renvoie le taux d'amélioration et les indices des deux cartes échangées'''
    o_score = board.evaluate()

    swap_1 = randint(0,7)
    swap_2 = randint(0,7)

    while swap_1 == swap_2:
        swap_2 = randint(0,7)

    d_nb_sanc = swap(board, swap_1, swap_2)
    print(f"d_nb_anc : {d_nb_sanc}")
    adjust_nb_sanc(board, d_nb_sanc)

    d_score = board.evaluate() - o_score

    return d_score, swap_1, swap_2

def swap(board, swap_1, swap_2):
    '''swap 2 cartes
    renvoie le nb de sanctuaires perdus/gagnés'''
    o_nb_sanc = board.nb_sanc

    tmp = board.cards[swap_1].copy()
    board.cards[swap_1] = board.cards[swap_2]
    board.cards[swap_2] = tmp

    board.count_nb_sanc()

    return board.nb_sanc - o_nb_sanc

def adjust_nb_sanc(board, d_nb_sanc):
    '''ajoute nb_sanc au board'''
    if d_nb_sanc > 0:
        for _ in range(d_nb_sanc):
            board.sanctuaries.append(board.sanctuaire_dispo.pop(0))

    elif d_nb_sanc < 0:
        for _ in range(-d_nb_sanc):
            board.sanctuaire_dispo.append(board.sanctuaries.pop(0))