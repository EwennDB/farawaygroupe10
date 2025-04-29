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
            print("aaaaa")

            if self.condition is None:
                print("aaaaa")
                return self.func(board)
            
            elif self.condition(board):
                return self.func(board)

        print("aaaaa")
        return 0
    
    def __repr__(self):
        return f'value : {self.value} couleur : {self.couleur} nuit : {self.nuit} indice : {self.indice} merveilles : {self.merveilles}'