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
                                    regions2 = copy.deepcopy(regions)

                                    for q in range(len(sanctuaries)):
                                        if lst[i][j][k][l][m][n][o].nb_sanc > 0:
                                            lst[i][j][k][l][m][n][o].add_sanctuary(lst[i][j][k][l][m][n][o].sanctuaire_dispo[q])
                                        
                                        for r in range(len(sanctuaries)-1):
                                            if lst[i][j][k][l][m][n][o].nb_sanc > 1:
                                                lst[i][j][k][l][m][n][o].add_sanctuary(lst[i][j][k][l][m][n][o].sanctuaire_dispo[r])
                                            
                                            for s in range(len(sanctuaries)-2):
                                                if lst[i][j][k][l][m][n][o].nb_sanc > 2:
                                                    lst[i][j][k][l][m][n][o].add_sanctuary(lst[i][j][k][l][m][n][o].sanctuaire_dispo[s])
                                                
                                                for t in range(len(sanctuaries)-3):
                                                    if lst[i][j][k][l][m][n][o].nb_sanc > 3:
                                                        lst[i][j][k][l][m][n][o].add_sanctuary(lst[i][j][k][l][m][n][o].sanctuaire_dispo[t])
                                                    
                                                    for u in range(len(sanctuaries)-4):
                                                        if lst[i][j][k][l][m][n][o].nb_sanc > 4:
                                                            lst[i][j][k][l][m][n][o].add_sanctuary(lst[i][j][k][l][m][n][o].sanctuaire_dispo[u])
                                                        
                                                        for v in range(len(sanctuaries)-5):
                                                            if lst[i][j][k][l][m][n][o].nb_sanc > 5:
                                                                lst[i][j][k][l][m][n][o].add_sanctuary(lst[i][j][k][l][m][n][o].sanctuaire_dispo[v])
                                                            
                                                            for w in range(len(sanctuaries)-6):
                                                                if lst[i][j][k][l][m][n][o].nb_sanc > 6:
                                                                    lst[i][j][k][l][m][n][o].add_sanctuary(lst[i][j][k][l][m][n][o].sanctuaire_dispo[w])

                                                                print
                                                                lst[i][j][k][l][m][n][o].reveal_all()

                                                                for _ in range(lst[i][j][k][l][m][n][o].nb_sanc):
                                                                    lst[i][j][k][l][m][n][o].calc_sanctuary_score()

                                                                if lst[i][j][k][l][m][n][o].score > best.score:
                                                                    best = lst[i][j][k][l][m][n][o]
                                                                    print(best)
                                                                
                                                                lst[i][j][k][l][m][n][o].couleurs = {"r" : 0, "b" : 0, "v" : 0, "j" : 0}
                                                                lst[i][j][k][l][m][n][o].nuits = 0
                                                                lst[i][j][k][l][m][n][o].indices = 0
                                                                lst[i][j][k][l][m][n][o].merveilles = {"p" : 0, "cha" : 0, "chi" : 0}
                                                                lst[i][j][k][l][m][n][o].score = 0
                                                                lst[i][j][k][l][m][n][o].pos = 7

                                                                val = lst[i][j][k][l][m][n][o].clear_last_sanctuary()
                                                                if not val is None:
                                                                    sanctuaries2.append(val)
                                                            val = lst[i][j][k][l][m][n][o].clear_last_sanctuary()
                                                            if not val is None:
                                                                sanctuaries2.append(val)
                                                        val = lst[i][j][k][l][m][n][o].clear_last_sanctuary()
                                                        if not val is None:
                                                            sanctuaries2.append(val)
                                                    val = lst[i][j][k][l][m][n][o].clear_last_sanctuary()
                                                    if not val is None:
                                                        sanctuaries2.append(val)
                                                val = lst[i][j][k][l][m][n][o].clear_last_sanctuary()
                                                if not val is None:
                                                    sanctuaries2.append(val)
                                            val = lst[i][j][k][l][m][n][o].clear_last_sanctuary()
                                            if not val is None:
                                                sanctuaries2.append(val)
                                        val = lst[i][j][k][l][m][n][o].clear_last_sanctuary()
                                        if not val is None:
                                            sanctuaries2.append(val)
 
                                        
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