## FONCTION SIMPLES
def get_2(board):
    return 2

def get_4(board):
    return 4

def get_5(board):
    return 5

def get_7(board):
    return 7

def get_8(board):
    return 8

def get_9(board):
    return 9

def get_10(board):
    return 10

def get_12(board):
    return 12

def get_13(board):
    return 13

def get_14(board):
    return 14

def get_15(board):
    return 15

def get_16(board):
    return 16

def get_17(board):
    return 17

def get_18(board):
    return 18

def get_19(board):
    return 19

def get_20(board):
    return 20

def get_24(board):
    return 24

## FONCTION SCALAIRES
# Nuits
def get_1_par_nuit(board):
    '''1 point par cartes nuits'''
    return board.nuits

def get_2_par_nuit(board):
    '''2 points par cartes nuits'''
    return board.nuits*2

def get_3_par_nuit(board):
    '''3 points par cartes nuits'''
    return board.nuits*3

def get_4_par_nuit(board):
    '''3 points par cartes nuits'''
    return board.nuits*4

# Indices
def get_1_par_indice(board):
    '''1 point par indices'''
    return board.indices

def get_2_par_indice(board):
    '''2 points par indices'''
    return board.indices*2

def get_3_par_indice(board):
    '''3 points par indices'''
    return board.indices*3

def get_4_par_indice(board):
    '''4 points par indices'''
    return board.indices*4

# Merveilles
def get_1_par_pierre(board):
    '''1 points par pierres'''
    return board.merveilles["p"]

def get_2_par_pierre(board):
    '''2 points par pierres'''
    return board.merveilles["p"]*2

def get_3_par_pierre(board):
    '''3 points par pierres'''
    return board.merveilles["p"]*3

def get_4_par_pierre(board):
    '''4 points par pierres'''
    return board.merveilles["p"]*4

def get_1_par_chimere(board):
    '''1 points par chimere'''
    return board.merveilles["chi"]

def get_2_par_chimere(board):
    '''2 points par pierres'''
    return board.merveilles["chi"]*2

def get_3_par_chimere(board):
    '''3 points par pierres'''
    return board.merveilles["chi"]*3

def get_4_par_chimere(board):
    '''4 points par pierres'''
    return board.merveilles["chi"]*4

def get_1_par_chardon(board):
    '''1 point par chardon'''
    return board.merveilles["cha"]

def get_2_par_chardon(board):
    '''2 points par chardon'''
    return board.merveilles["cha"]*2

def get_3_par_chardon(board):
    '''3 points par chardon'''
    return board.merveilles["cha"]*3

def get_4_par_chardon(board):
    '''4 points par chardon'''
    return board.merveilles["cha"]*4

# Couleurs
def get_1_par_rouge(board):
    '''1 points par carte rouge'''
    return board.couleurs["r"]

def get_2_par_rouge(board):
    '''2 points par carte rouge'''
    return board.couleurs["r"]*2

def get_3_par_rouge(board):
    '''3 points par carte rouge'''
    return board.couleurs["r"]*3

def get_4_par_rouge(board):
    '''4 points par carte rouge'''
    return board.couleurs["r"]*4

def get_1_par_vert(board):
    '''1 points par carte verte'''
    return board.couleurs["v"]

def get_2_par_vert(board):
    '''2 points par carte verte'''
    return board.couleurs["v"]*2

def get_3_par_vert(board):
    '''3 points par carte verte'''
    return board.couleurs["v"]*3

def get_4_par_vert(board):
    '''4 points par carte verte'''
    return board.couleurs["v"]*4

def get_1_par_bleu(board):
    '''1 points par carte bleue'''
    return board.couleurs["b"]

def get_2_par_bleu(board):
    '''2 points par carte bleue'''
    return board.couleurs["b"]*2

def get_3_par_bleu(board):
    '''3 points par carte bleue'''
    return board.couleurs["b"]*3

def get_4_par_bleu(board):
    '''4 points par carte bleue'''
    return board.couleurs["b"]*4

def get_1_par_jaune(board):
    '''1 points par carte jaune'''
    return board.couleurs["j"]

def get_2_par_jaune(board):
    '''2 points par carte jaune'''
    return board.couleurs["j"]*2

def get_3_par_jaune(board):
    '''3 points par carte jaune'''
    return board.couleurs["j"]*3

## FONCTIONS bicolores
def get_1_par_jaune_ou_vert(board):
    '''1 point par carte jaune ou verte'''
    return board.couleurs["j"] + board.couleurs["v"]

def get_2_par_jaune_ou_vert(board):
    '''2 points par carte jaune ou verte'''
    return (board.couleurs["j"] + board.couleurs["v"])*2

def get_3_par_jaune_ou_vert(board):
    '''3 points par carte jaune ou verte'''
    return (board.couleurs["j"] + board.couleurs["v"])*3

def get_1_par_jaune_ou_bleu(board):
    '''1 point par carte jaune ou bleue'''
    return board.couleurs["j"] + board.couleurs["b"]

def get_2_par_jaune_ou_bleu(board):
    '''2 points par carte jaune ou bleue'''
    return (board.couleurs["j"] + board.couleurs["b"])*2

def get_3_par_jaune_ou_bleu(board):
    '''3 points par carte jaune ou bleue'''
    return (board.couleurs["j"] + board.couleurs["b"])*3

def get_1_par_jaune_ou_rouge(board):
    '''1 point par carte jaune ou rouge'''
    return board.couleurs["j"] + board.couleurs["r"]

def get_2_par_jaune_ou_rouge(board):
    '''2 points par carte jaune ou rouge'''
    return (board.couleurs["j"] + board.couleurs["r"])*2

def get_3_par_jaune_ou_rouge(board):
    '''3 points par carte jaune ou rouge'''
    return (board.couleurs["j"] + board.couleurs["r"])*3

def get_1_par_rouge_ou_bleu(board):
    '''1 point par carte rouge ou bleu'''
    return board.couleurs["r"] + board.couleurs["b"]

def get_1_par_rouge_ou_jaune(board):
    '''1 point par carte rouge ou jaune'''
    return board.couleurs["r"] + board.couleurs["j"]

def get_1_par_vert_ou_rouge(board):
    '''1 point par carte verte ou rouge'''
    return board.couleurs["v"] + board.couleurs["r"]

def get_1_par_vert_ou_bleu(board):
    '''1 point par carte verte ou bleue'''
    return board.couleurs["v"] + board.couleurs["b"]

def get_1_par_bleu_ou_jaune(board):
    '''1 point par carte bleue ou jaune'''
    return board.couleurs["b"] + board.couleurs["j"]

def get_1_par_jaune_ou_vert(board):
    '''1 point par carte jaune ou verte'''
    return board.couleurs["j"] + board.couleurs["v"]

## FONCTIONS spéciales
def get_4_par_ensemble(board):
    '''4 points par ensemble de carte
    (ensemble = 1 carte de chaque couleur)'''
    min = 4
    for i in board.couleurs.values():
        if i < min:
            min = i

    return 4*min

def get_10_par_ensemble(board):
    '''4 points par ensemble de carte
    (ensemble = 1 carte de chaque couleur)'''
    min = 4
    for i in board.couleurs.values():
        if i < min:
            min = i

    return 10*min

## ÉQUIVALENT DE FONCTION
functions = {
    "" : None,
    "get_2" : get_2,
    "get_4" : get_4,
    "get_5" : get_5,
    "get_7" : get_7,
    "get_8" : get_8,
    "get_9" : get_9,
    "get_10" : get_10,
    "get_12" : get_12,
    "get_13" : get_13,
    "get_14" : get_14,
    "get_15" : get_15,
    "get_16" : get_16,
    "get_17" : get_17,
    "get_18" : get_18,
    "get_19" : get_19,
    "get_20" : get_20,
    "get_24" : get_24,

    "get_1_par_nuit" : get_1_par_nuit,
    "get_2_par_nuit" : get_2_par_nuit,
    "get_3_par_nuit" : get_3_par_nuit,
    "get_4_par_nuit" : get_4_par_nuit,

    "get_1_par_indice" : get_1_par_indice,
    "get_2_par_indice" : get_2_par_indice,
    "get_3_par_indice" : get_3_par_indice,
    "get_4_par_indice" : get_4_par_indice,

    "get_1_par_pierre" : get_1_par_pierre,
    "get_2_par_pierre" : get_2_par_pierre,
    "get_3_par_pierre" : get_3_par_pierre,
    "get_4_par_pierre" : get_4_par_pierre,

    "get_1_par_chimere" : get_1_par_chimere,
    "get_2_par_chimere" : get_2_par_chimere,
    "get_3_par_chimere" : get_3_par_chimere,
    "get_4_par_chimere" : get_4_par_chimere,

    "get_1_par_chardon" : get_1_par_chardon,
    "get_2_par_chardon" : get_2_par_chardon,
    "get_3_par_chardon" : get_3_par_chardon,
    "get_4_par_chardon" : get_4_par_chardon,

    "get_1_par_rouge" : get_1_par_rouge,
    "get_2_par_rouge" : get_2_par_rouge,
    "get_3_par_rouge" : get_3_par_rouge,
    "get_4_par_rouge" : get_4_par_rouge,

    "get_1_par_vert" : get_1_par_vert,
    "get_2_par_vert" : get_2_par_vert,
    "get_3_par_vert" : get_3_par_vert,
    "get_4_par_vert" : get_4_par_vert,

    "get_1_par_bleu" : get_1_par_bleu,
    "get_2_par_bleu" : get_2_par_bleu,
    "get_3_par_bleu" : get_3_par_bleu,
    "get_4_par_bleu" : get_4_par_bleu,

    "get_1_par_jaune" : get_1_par_jaune,
    "get_2_par_jaune" : get_2_par_jaune,
    "get_3_par_jaune" : get_3_par_jaune,

    "get_1_par_jaune_ou_rouge" : get_1_par_jaune_ou_rouge,
    "get_2_par_jaune_ou_rouge" : get_2_par_jaune_ou_rouge,
    "get_3_par_jaune_ou_rouge" : get_3_par_jaune_ou_rouge,

    "get_1_par_jaune_ou_vert" : get_1_par_jaune_ou_vert,
    "get_2_par_jaune_ou_vert" : get_2_par_jaune_ou_vert,
    "get_3_par_jaune_ou_vert" : get_3_par_jaune_ou_vert,

    "get_1_par_jaune_ou_bleu" : get_1_par_jaune_ou_bleu,
    "get_2_par_jaune_ou_bleu" : get_2_par_jaune_ou_bleu,
    "get_3_par_jaune_ou_bleu" : get_3_par_jaune_ou_bleu,

    "get_1_par_rouge_ou_bleu" : get_1_par_rouge_ou_bleu,
    "get_1_par_vert_ou_rouge" : get_1_par_vert_ou_rouge,
    "get_1_par_rouge_ou_jaune" : get_1_par_rouge_ou_jaune,
    "get_1_par_vert_ou_bleu" : get_1_par_vert_ou_bleu,
    "get_1_par_bleu_ou_jaune" : get_1_par_bleu_ou_jaune,
    "get_1_par_jaune_ou_vert" : get_1_par_jaune_ou_vert,

    "get_4_par_ensemble" : get_4_par_ensemble,
    "get_10_par_ensemble" : get_10_par_ensemble
}