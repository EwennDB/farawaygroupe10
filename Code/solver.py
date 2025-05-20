from Board import Board
from helper import make_regions, make_sanctuaries, make_value_lists, combinations
import copy
from random import randint
from time import sleep, time

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
    regions = make_regions(lst_regions)
    sanctuaries = make_sanctuaries(lst_sanctuaries)
    b = Board(sanctuaries)
    b.place_all(lst_regions)

    for i in range(len(b.sanctuaire_dispo)):
        b.add_sanctuary(b.sanctuaire_dispo[0])

    b.reveal_all_regions()

    for i in regions:
        if i.condition is not None:
            if not i.condition(b) and len(regions) > 8:
                regions.remove(i)

    return regions

def change_sanctuaries(best, current_score, nb_iter):
    board = best.copy()
    for i in range(nb_iter):

        #change les sanctuaires
        a = randint(0, len(board.sanctuaries) - 1)
        b = randint(0, len(board.sanctuaire_dispo) - 1)
        board.sanctuaries[a], board.sanctuaire_dispo[b] = board.sanctuaire_dispo[b], board.sanctuaries[a]

        score = board.evaluate()
        if score > current_score:
            current_score = score
            best = board.copy()
    
    return best, current_score

def gradient_descent(board):
    '''trouve le meilleur arrangement des cartes régions et place les bons sanctuaires
    Nécessite un board'''
    startTime = time()
    timeToRun = 1
    endTime = startTime + timeToRun

    nb_iter = 10
    #stocke le meilleur board pour pouvoir revenir en arrière
    best = board.copy()
    current_score = board.evaluate()
    while(time() <= endTime):
        for _ in range(nb_iter):
            # fait un swap random nb_iter fois
            d_score = swap_random(board)

            # si le swap s'avère défavorable, on repart en arrière
            if d_score <= current_score:
                board = best.copy()
                # print("reversed")

            # si il s'avère bénéfique, on le garde
            else:
                best = board.copy()
                current_score = d_score

                if len(board.sanctuaire_dispo) > 1:
                    for _ in range(nb_iter):

                        #change les sanctuaires
                        a = randint(0, len(board.sanctuaries) - 1)
                        b = randint(0, len(board.sanctuaire_dispo) - 1)
                        board.sanctuaries[a], board.sanctuaire_dispo[b] = board.sanctuaire_dispo[b], board.sanctuaries[a]

                        score = board.evaluate()
                        if score > current_score:
                            current_score = score
                            best = board.copy()

    return best

def gradient_descent_regions(board, regions):
    '''essaie d'échanger des régions'''
    startTime = time()
    timeToRun = 5
    endTime = startTime + timeToRun

    nb_iter = 10
    #stocke le meilleur board pour pouvoir revenir en arrière
    best = board.copy()
    current_score = board.evaluate()

    regions_available = copy.deepcopy(regions)

    for i in board.cards:
        regions_available.remove(i)
    
    best_region = copy.deepcopy(regions_available)

    while(time() <= endTime):
        for i in range(nb_iter):

            # fait un swap random nb_iter fois
            new_score = swap_regions(board, regions_available)

            # si le swap s'avère défavorable, on repart en arrière
            if new_score <= current_score:
                board = best.copy()
                regions_available = copy.deepcopy(best_region)

            # si il s'avère bénéfique, on le garde
            else:
                best = board.copy()
                best_region = copy.deepcopy(regions_available)
                current_score = new_score

                if len(board.sanctuaire_dispo) > 1:
                    best, current_score = change_sanctuaries(best, current_score, nb_iter)

    return best

def swap_regions(board, regions):
    '''swap 1 cartes au hasard du board avec une carte de la lst
    renvoie le taux d'amélioration'''
    swap_1 = randint(0,7)
    swap_2 = randint(0,len(regions)-1)

    o_nb_sanc = board.nb_sanc

    tmp = copy.deepcopy(board.cards[swap_1])
    board.cards[swap_1] = regions[swap_2]
    regions.pop(swap_2)
    regions.append(tmp)

    board.count_nb_sanc()

    adjust_nb_sanc(board, board.nb_sanc - o_nb_sanc)

    new_score = board.evaluate()

    return new_score

def swap_random(board):
    '''swap 2 cartes au hasard dans le board
    renvoie le taux d'amélioration'''
    swap_1 = randint(0,7)
    swap_2 = randint(0,7)

    while swap_1 == swap_2:
        swap_2 = randint(0,7)

    d_nb_sanc = swap(board, swap_1, swap_2)
    adjust_nb_sanc(board, d_nb_sanc)

    new_score = board.evaluate()

    return new_score

def swap(board, swap_1, swap_2):
    '''swap 2 cartes du board
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