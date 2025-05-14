from Card import Card
from helper import add_dict, make_regions
from random import randint
import copy

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
        self.nb_sanc = 0

    def copy(self) -> object:
        '''renvoie une copie de ce plateau'''
        cp = Board(copy.deepcopy(self.sanctuaire_dispo))
        cp.cards = copy.deepcopy(self.cards)
        cp.sanctuaries = copy.deepcopy(self.sanctuaries)
        cp.couleurs = self.couleurs
        cp.nuits = self.nuits
        cp.indices = self.indices
        cp.merveilles = copy.deepcopy(self.merveilles)
        cp.score = self.score
        cp.pos = self.pos
        cp.nb_sanc = self.nb_sanc
        return cp
    
    def place_card(self, card, sanc = None):
        '''place une carte sur le plateau et vérifie si l'on peut prendre un sanctuaire'''
        self.cards.append(card)
        self.pos += 1
        if self.pos != -1 and card.value > self.cards[self.pos - 1].value:
            self.nb_sanc += 1
    
    def place_all(self, lst):
        lst = make_regions(lst)
        for card in lst:
            self.place_card(card)

    def reveal_all(self):
        for card in self.cards:
            self.reveal_card()

    def add_card_args(self, card):
        '''ajoue les attributs des cartes au plateau'''
        self.merveilles = add_dict(self.merveilles, card.merveilles)
        self.nuits += card.nuit
        self.indices += card.indice
        if not card.couleur is None:
            self.couleurs[card.couleur] += 1

    def reveal_card(self):
        '''revele les cartes et compte leurs scores'''
        self.add_card_args(self.cards[self.pos])
        self.score += self.cards[self.pos].calc_score(self)
        self.pos -= 1

    def calc_sanctuary_score(self):
        '''calcule le score des sanctuaires'''
        for sanc in self.sanctuaries:
            self.score += sanc.calc_score(self)

    def clear_sanc(self):
        for sanc in self.sanctuaries:
            self.score -= sanc.calc_score(self)
        for i in range(len(self.sanctuaries)):
            self.sanctuaire_dispo.append(self.sanctuaries.pop(i))

    def clear_last_sanctuary(self):
        if self.sanctuaries == []:
            return None
        
        for sanc in self.sanctuaries:
            self.score -= sanc.calc_score(self)
        self.sanctuaire_dispo = [(self.sanctuaries.pop(len(self.sanctuaries) - 1))] + self.sanctuaire_dispo
        o = self.sanctuaire_dispo[-1]
        self.calc_sanctuary_score()
        return o

    def add_sanctuary(self, sanctuary):
        '''ajoute un sanctuaire au plateau'''
        self.sanctuaries.append(sanctuary)
        self.add_card_args(sanctuary)
        self.sanctuaire_dispo.remove(sanctuary)

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