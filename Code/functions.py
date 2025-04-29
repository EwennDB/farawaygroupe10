## FONCTION SIMPLES
def get_2(board):
    return 2

def get_4(board):
    return 4

def get_5(board):
    return 5

## FONCTION SCALAIRES
def get_2_par_nuit(board):
    '''2 points par cartes nuits'''
    return board.nuit*2

def get_3_par_nuit(board):
    '''3 points par cartes nuits'''
    return board.nuit*3

def get_2_par_indice(board):
    '''2 points par indices'''
    val = 0
    for i in board[pos:]:
        if i.indice:
            val += 2
    
    return val

def get_2_par_pierre(board):
    '''2 points par pierres'''
    val = 0
    for i in board[pos:]:
        val += 2*i.merveilles["p"]
    
    return val

def get_2_par_chimere(board):
    '''2 points par pierres'''
    val = 0
    for i in board[pos:]:
        val += 2*i.merveilles["p"]
    
    return val


## FONCTIONS SCALAIRES AVEC CONDITIONS
def get_3_par_pierre_si_2_chimeres(board):
    '''2 points par pierres'''
    val = 0
    for i in board[pos:]:
        val += 2*i.merveilles["p"]
    
    return val