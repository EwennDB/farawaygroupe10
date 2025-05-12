from Board import Board
from helper import make_regions, make_sanctuaries, make_value_lists, add_with_order
import copy

def brute_force(path_instance) :
    '''brute_force toutes les possibilités d'une instance,
    ça marche pas, à cause de l'ordre des sanctuaires'''
    max = 0
    lst_regions, lst_sanctuaries = make_value_lists("../Sujet/Instances_hors_compétition/8_7_a.txt")

    regions = make_regions(lst_regions)
    regions2 = copy.deepcopy(regions)
    sanctuaries = make_sanctuaries(lst_sanctuaries)
    sanctuaries2 = copy.deepcopy(sanctuaries)

    lst = []
    sanc_scores = []
    best = Board(sanctuaries)

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
                                    lst[i][j][k][l][m][n][o] = Board(sanctuaries)
                                    lst[i][j][k][l][m][n][o].place_card(regions2.pop(i))
                                    lst[i][j][k][l][m][n][o].place_card(regions2.pop(j))
                                    lst[i][j][k][l][m][n][o].place_card(regions2.pop(k))
                                    lst[i][j][k][l][m][n][o].place_card(regions2.pop(l))
                                    lst[i][j][k][l][m][n][o].place_card(regions2.pop(m))
                                    lst[i][j][k][l][m][n][o].place_card(regions2.pop(n))
                                    lst[i][j][k][l][m][n][o].place_card(regions2.pop(o))
                                    lst[i][j][k][l][m][n][o].place_card(regions2.pop(p))
                                    lst[i][j][k][l][m][n][o].reveal_all()
                                    regions2 = copy.deepcopy(regions)
                                    for q in range(len(sanctuaries)):
                                        sanc_scores = add_with_order(sanc_scores, sanctuaries[q].calc_score(lst[i][j][k][l][m][n][o]))
                                    for _ in range(lst[i][j][k][l][m][n][o].nb_sanc):
                                        lst[i][j][k][l][m][n][o].score += sanc_scores.pop(-1)
                                    if lst[i][j][k][l][m][n][o].score > best.score:
                                        best = lst[i][j][k][l][m][n][o]
                                        print(sanc_scores)
                                    sanc_scores = []
    print(best)

