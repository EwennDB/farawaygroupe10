from Card import Card
from helper import add_dict
from random import randint

class Board:
    def __init__(self, sanctuaire_dispo):
        self.cards = []
        self.sanctuaries = []
        self.sanctuaire_dispo = sanctuaire_dispo
    
        self.couleurs = {"r" : 0, "b" : 0, "v" : 0, "j" : 0}
        self.nuits = 0
        self.indices = 0
        self.merveilles = {"p" : 0, "cha" : 0, "chi" : 0}
        self.score = 0
        self.pos = -1
    
    def place_card(self, card):
        '''place une carte sur le plateau et vérifie si l'on peut prendre un sanctuaire'''
        self.cards.append(card)
        self.pos += 1
        print(card.value, self.cards[self.pos - 1].value)
        if self.pos != -1 and card.value > self.cards[self.pos - 1].value:
            self.add_sanctuary()
    
    def add_card_args(self, card):
        '''ajoue les attributs des cartes au plateau'''
        self.merveilles = add_dict(self.merveilles, card.merveilles)
        self.nuits += card.nuit
        self.indices += card.indice
        if not card.couleur is None:
            self.couleurs[card.couleur] += 1

    def reveal_card(self):
        '''revele les cartes et compte leurs scores'''
        self.score += self.cards[self.pos].calc_score(self)
        self.add_card_args(self.cards[self.pos])
        self.pos -= 1

    def add_sanctuary(self):
        '''ajoute un sanctuaire au hasard au plateau'''
        id = randint(0, len(self.sanctuaire_dispo) - 1)
        self.sanctuaries.append(self.sanctuaire_dispo[id])
        self.add_card_args(self.sanctuaries[len(self.sanctuaries) - 1])
        self.sanctuaire_dispo.pop(id)

    def __repr__(self):
        '''représente le board'''
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