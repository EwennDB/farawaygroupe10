from Board import Board
from helper import make_regions, make_sanctuaries, make_value_lists, combinations
import copy

def brute_force(path_instance) :
    '''brute_force toutes les possibilités d'une instance,
    ça marche pas, à cause de l'ordre des sanctuaires'''
    max = 0
    lst_regions, lst_sanctuaries = make_value_lists("../Sujet/Instances_hors_compétition/8_7_a.txt")

    regions = make_regions(lst_regions)
    regions2 = copy.deepcopy(regions)
    sanctuaries = make_sanctuaries(lst_sanctuaries)

    lst = []
    best = Board(sanctuaries)
    a = 0

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
                                    a += 1
                                    lst[i][j][k][l][m][n][o] = [Board(copy.deepcopy(sanctuaries))]
                                    lst[i][j][k][l][m][n][o][0].place_card(regions2.pop(i))
                                    lst[i][j][k][l][m][n][o][0].place_card(regions2.pop(j))
                                    lst[i][j][k][l][m][n][o][0].place_card(regions2.pop(k))
                                    lst[i][j][k][l][m][n][o][0].place_card(regions2.pop(l))
                                    lst[i][j][k][l][m][n][o][0].place_card(regions2.pop(m))
                                    lst[i][j][k][l][m][n][o][0].place_card(regions2.pop(n))
                                    lst[i][j][k][l][m][n][o][0].place_card(regions2.pop(o))
                                    lst[i][j][k][l][m][n][o][0].place_card(regions2.pop(p))
                                    lst[i][j][k][l][m][n][o].append(lst[i][j][k][l][m][n][o][0].copy())
                                    regions2 = copy.deepcopy(regions)
                                    cmb = combinations(len(sanctuaries), lst[i][j][k][l][m][n][o][0].nb_sanc)
                                    print(a/40320)

                                    for current_cmb in cmb:
                                        for q in range(len(current_cmb)):
                                            lst[i][j][k][l][m][n][o][0].add_sanctuary(lst[i][j][k][l][m][n][o][0].sanctuaire_dispo[current_cmb[q]-q])

                                        lst[i][j][k][l][m][n][o][0].reveal_all()

                                        lst[i][j][k][l][m][n][o][0].calc_sanctuary_score()

                                        print(lst[i][j][k][l][m][n][o][0].score)
                                        if lst[i][j][k][l][m][n][o][0].score > best.score:
                                            best = lst[i][j][k][l][m][n][o][0]
                                            print(best)

                                        lst[i][j][k][l][m][n][o][0] = lst[i][j][k][l][m][n][o][1].copy()
                            exit()
                                        
    print(best)

def virer_inutile(filepath):
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

virer_inutile("../Sujet/Instances_hors_compétition/test.txt")