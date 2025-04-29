from Board import Board
from Card import Card

if __name__ == '__main__':

    with open("../Sujet/Instances_hors_compétition/8_7_a.txt", 'r') as file:
        for i in file:
            lst_card = i.strip().split(" ")
        
        lst_sanctuary = []

        c = 0

        while int(lst_card[c]) < 101:
            c += 1
        
        lst_sanctuary = lst_card[c:]
        lst_card = lst_card[:c]

    print(lst_card, lst_sanctuary)

    test = Board()

    for i in lst_card[:8]:
        test.place_card(i)
    
    print(test.cards)