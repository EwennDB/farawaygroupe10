class Card:
    def __init__(self, value, couleur, nuit, indice, merveilles, func=None, condition=None):
        self.value = value
        self.couleur = couleur
        self.nuit = nuit
        self.indice = indice
        self.merveilles = merveilles
        self.func = func
        self.condition = condition
    
    def calc_score(self, board):
        '''calcule le score de la carte
        appelle la fonction si elle existe
        0 sinon'''
        if not self.func is None:

            if self.condition is None:
                return self.func(board)
            
            elif self.condition(board):
                return self.func(board)

        return 0

v = Card(1, "r", False, False, {"p" : 1, "c" : 1})

v.calc_score(0, 0)