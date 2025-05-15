from Card import Card
from helper import add_dict, make_regions
from random import randint
from copy import deepcopy

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

    def repr_ressources(self):
        '''représente les ressources du tableau'''
        print("nuits : " + str(self.nuits) + " indices : " + str(self.nuits))
        print("\ncouleurs : "+str(self.couleurs) + " merveilles : "+str(self.merveilles))

    def copy(self) -> object:
        '''renvoie une copie de ce plateau'''
        return deepcopy(self)
    
    ##Placements Régions/Sanctuaires
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

    def add_card_args(self, card):
        '''ajoue les attributs des cartes au plateau'''
        self.merveilles = add_dict(self.merveilles, card.merveilles)
        self.nuits += card.nuit
        self.indices += card.indice
        if not card.couleur is None:
            self.couleurs[card.couleur] += 1

    def add_sanctuary(self, sanctuary):
        '''ajoute un sanctuaire au plateau
        ajoute ses ressources
        et l'enlève des sanctuaires dispo'''
        self.sanctuaries.append(sanctuary)
        self.add_card_args(sanctuary)
        self.sanctuaire_dispo.remove(sanctuary)


    ##Révèle/Compte
    def reveal_card(self):
        '''revele une carte région et fait les changements nécessaires'''
        self.add_card_args(self.cards[self.pos])
        self.score += self.cards[self.pos].calc_score(self)
        self.pos -= 1

    def reveal_all_regions(self):
        '''révèle toutes les cartes régions'''
        for _ in self.cards:
            self.reveal_card()

    def calc_all_sanctuary_score(self):
        '''calcule le score des sanctuaires'''
        for sanc in self.sanctuaries:
            self.score += sanc.calc_score(self)

    def count_all(self):
        '''compte tt (régions + sanctuaires)'''
        self.reveal_all_regions()
        self.calc_all_sanctuary_score()

    ##Vide
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
        self.calc_all_sanctuary_score()
        return o


    ## Autres
    def copy(self):
        return deepcopy(self)

    def evaluate(self):
        '''évalue le score SANS RÉVÉLER les cartes
        nécessite que les sanctuaires et régions soient placés
        '''
        b = self.copy()

        for i in range(self.nb_sanc):
            b.add_card_args(self.sanctuaries[i])

        b.reveal_all_regions()

        b.calc_all_sanctuary_score()

        return b.score

    def count_nb_sanc(self):
        '''actualise le nb de sanctuaire'''
        self.nb_sanc = 0
        for i in range(7):
            if self.cards[i].value < self.cards[i+1].value:
                self.nb_sanc += 1