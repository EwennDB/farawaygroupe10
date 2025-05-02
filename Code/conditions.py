## CONDITIONS SIMPLES
def si_1_pierre(board):
    '''renvoie vrai si plus de 1 pierre'''
    return board.merveilles["p"] >= 1

def si_2_pierre(board):
    '''renvoie vrai si plus de 2 pierres'''
    return board.merveilles["p"] >= 2

def si_3_pierre(board):
    '''renvoie vrai si plus de 3 pierres'''
    return board.merveilles["p"] >= 3

def si_4_pierre(board):
    '''renvoie vrai si plus de 4 pierres'''
    return board.merveilles["p"] >= 4

def si_5_pierre(board):
    '''renvoie vrai si plus de 5 pierres'''
    return board.merveilles["p"] >= 5

def si_1_chimere(board):
    '''renvoie vrai si plus de 1 chimère'''
    return board.merveilles["chi"] >= 1

def si_2_chimere(board):
    '''renvoie vrai si plus de 2 chimères'''
    return board.merveilles["chi"] >= 2

def si_3_chimere(board):
    '''renvoie vrai si plus de 3 chimères'''
    return board.merveilles["chi"] >= 3

def si_4_chimere(board):
    '''renvoie vrai si plus de 2 chimères'''
    return board.merveilles["chi"] >= 4

def si_1_chardon(board):
    '''renvoie vrai si plus de 1 chardon'''
    return board.merveilles["cha"] >= 1

def si_2_chardon(board):
    '''renvoie vrai si plus de 2 chardons'''
    return board.merveilles["cha"] >= 2

def si_3_chardon(board):
    '''renvoie vrai si plus de 3 chardons'''
    return board.merveilles["cha"] >= 3

## CONDITIONS DOUBLES
#1-1
def si_1_chimere_et_1_chardon(board):
    '''renvoie vrai si plus de 1 chimere et plus de 1 chardon'''
    return (board.merveilles["chi"] >= 1 and board.merveilles["cha"] >= 1)

def si_1_pierre_et_1_chimere(board):
    '''renvoie vrai si plus de 1 pierre et plus de 1 chimere'''
    return (board.merveilles["p"] >= 1 and board.merveilles["chi"] >= 1)

def si_1_pierre_et_1_chardon(board):
    '''renvoie vrai si plus de 1 pierre et plus de 1 chardon'''
    return (board.merveilles["p"] >= 1 and board.merveilles["cha"] >= 1)

#2-1
def si_2_pierre_et_1_chimere(board):
    '''renvoie vrai si plus de 2 pierres et plus de 1 chimere'''
    return (board.merveilles["p"] >= 2 and board.merveilles["chi"] >= 1)

def si_2_pierre_et_1_chardon(board):
    '''renvoie vrai si plus de 2 pierres et plus de 1 chardon'''
    return (board.merveilles["p"] >= 2 and board.merveilles["cha"] >= 1)

def si_2_chimere_et_1_chardon(board):
    '''renvoie vrai si plus de 2 chimere et plus de 1 chardon'''
    return (board.merveilles["chi"] >= 2 and board.merveilles["cha"] >= 1)

#1-2
def si_1_chimere_et_2_chardon(board):
    '''renvoie vrai si plus de 1 chimere et plus de 2 chardons'''
    return (board.merveilles["chi"] >= 1 and board.merveilles["cha"] >= 2)

def si_1_pierre_et_2_chimere(board):
    '''renvoie vrai si plus de 1 pierre et plus de 2 chimeres'''
    return (board.merveilles["p"] >= 1 and board.merveilles["chi"] >= 2)

#2-2
def si_2_pierre_et_2_chimere(board):
    '''renvoie vrai si plus de 2 pierres et plus de 2 chimeres'''
    return (board.merveilles["p"] >= 2 and board.merveilles["chi"] >= 2)

def si_2_pierre_et_2_chardon(board):
    '''renvoie vrai si plus de 2 pierres et plus de 2 chardons'''
    return (board.merveilles["p"] >= 2 and board.merveilles["cha"] >= 2)

def si_2_chimere_et_2_chardon(board):
    '''renvoie vrai si plus de 2 chimeres et plus de 2 chardons'''
    return (board.merveilles["chi"] >= 2 and board.merveilles["cha"] >= 2)

#1-3
def si_1_pierre_et_3_chimere(board):
    '''renvoie vrai si plus de 1 pierre et plus de 3 chimeres'''
    return (board.merveilles["p"] >= 1 and board.merveilles["chi"] >= 3)

## CONDITION(S) TRIPLES
def si_1_pierre_et_1_chimere_et_1_chardon(board):
    '''renvoie vrai si plus de 1 de chaque'''
    return (board.merveilles["p"] >= 1 and board.merveilles["chi"] >= 1 and board.merveilles["cha"] >= 1)

## ÉQUIVALENT DE FONCTION
conditions = {
    "si_1_pierre" : si_1_pierre,
    "si_2_pierre" : si_2_pierre,
    "si_3_pierre" : si_3_pierre,
    "si_4_pierre" : si_4_pierre,
    "si_5_pierre" : si_5_pierre,

    "si_1_chimere" : si_1_chimere,
    "si_2_chimere" : si_2_chimere,
    "si_3_chimere" : si_3_chimere,
    "si_4_chimere" : si_4_chimere,

    "si_1_chardon" : si_1_chardon,
    "si_2_chardon" : si_2_chardon,
    "si_3_chardon" : si_3_chardon,

    "si_1_pierre_et_1_chimere" : si_1_pierre_et_1_chimere,
    "si_1_pierre_et_1_chardon" : si_1_pierre_et_1_chardon,
    "si_1_chimere_et_1_chardon" : si_1_chimere_et_1_chardon,

    "si_2_pierre_et_1_chimere" : si_2_pierre_et_1_chimere,
    "si_2_pierre_et_1_chardon" : si_2_pierre_et_1_chardon,
    "si_2_chimere_et_1_chardon" : si_2_chimere_et_1_chardon,

    "si_1_chimere_et_2_chardon" : si_1_chimere_et_2_chardon,
    "si_1_pierre_et_2_chimere" : si_1_pierre_et_2_chimere,

    "si_2_pierre_et_2_chimere" : si_2_pierre_et_2_chimere,
    "si_2_pierre_et_2_chardon" : si_2_pierre_et_2_chardon,
    "si_2_chimere_et_2_chardon" : si_2_chimere_et_2_chardon,

    "si_1_pierre_et_3_chimere" : si_1_pierre_et_3_chimere,

    "si_1_pierre_et_1_chimere_et_1_chardon" : si_1_pierre_et_1_chimere_et_1_chardon
}