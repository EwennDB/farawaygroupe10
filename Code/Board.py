from "helper.py" import 

class Board:
    def __init__(self):
        self.cards = []
    
        self.couleurs = {"r" : 0, "b" : 0, "v" : 0, "j" : 0}
        self.nuits = 0
        self.indices = 0
        self.merveilles = {"p" : 0, "cha" : 0, "chi" : 0}
        self.score = 0
        self.pos = 0
    
    def place_card(self, card):
        '''place une carte sur le plateau'''
        self.cards.append(card)
    
    def add_card_args(self, card):
        self.couleurs = add

    def reveal_card(self):
        '''revele les cartes et compte leurs scores'''
        self.cards[self.pos].calc_score(self)