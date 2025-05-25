from solver import get_best_score
from helper import add_sol
from time import time
from tqdm import tqdm

if __name__ == '__main__':
    
    filepath = input("Entrez le nom du fichier :")
    filepath = "../Sujet/Instances_compétition/" + filepath
    best = get_best_score(filepath)
    print(best, best.evaluate())

    # for i in range(3,10):
    #     filepath = f"../Sujet/Instances_compétition/competition_0{str(i)}.txt"

    #     print(f"compétition n°{str(i)} :")

    #     t = time()
    #     best = get_best_score(filepath)
    #     print(f"temps : {time()-t}")
    #     print(f"score : {best.evaluate()}")

    # #     add_sol(filepath, best)
    
    # for i in range(0,6):
    #     filepath = f"../Sujet/Instances_compétition/competition_1{str(i)}.txt"

    #     print(f"compétition n°1{str(i)} :")
    #     t = time()
    #     best = get_best_score(filepath)
    #     print(f"temps : {time()-t}")
    #     print(f"score : {best.evaluate()}")

    #     add_sol(filepath, best)