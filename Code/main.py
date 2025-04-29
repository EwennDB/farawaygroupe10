from Board import Board
from Card import Card
from helper import make_cards, make_sanctuaries

if __name__ == '__main__':

    with open("../Sujet/Instances_hors_compétition/8_7_a.txt", 'r') as file:
        for i in file:
            lst_card = i.strip().split(" ")
        
        lst_sanctuary = []

        c = 0

        while int(lst_card[c]) < 101:
            c += 1
        
        lst_sanctuaries = lst_card[c:]
        lst_cards = lst_card[:c]

    cards = make_cards(lst_cards)
    sanctuaries = make_sanctuaries(lst_sanctuaries)

    test = Board()

    test.place_card(cards[1])

    print(test.cards[0].calc_score(test))