from helper import add_dict

class Board:
    def __init__(self):
        self.cards = []
        self.sanctuaries = []
    
        self.couleurs = {"r" : 0, "b" : 0, "v" : 0, "j" : 0}
        self.nuits = 0
        self.indices = 0
        self.merveilles = {"p" : 0, "cha" : 0, "chi" : 0}
        self.score = 0
        self.pos = 0
    
    def place_card(self, card):
        '''place une carte sur le plateau'''
        self.cards.append(card)
        self.pos += 1
    
    def add_card_args(self, card):
        '''not fait'''
        pass

    def reveal_card(self):
        '''revele les cartes et compte leurs scores'''
        self.cards[self.pos].calc_score(self)
        self.pos -= 1

    def __repr__(self):

        chaine = "score : "
        chaine += str(self.score)

        chaine += " pos : " + str(self.pos)

        chaine += " cards : "

        for i in self.cards:
            chaine += str(i.value)
            chaine += "-"
        
        chaine += " sanctuaries : "

        for i in self.sanctuaries:
            chaine += str(i.value)
            chaine += "-"
        
        return chaine