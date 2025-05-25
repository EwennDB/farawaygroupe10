from solver import get_best_score
from helper import add_sol
from time import time
from tqdm import tqdm

if __name__ == '__main__':
    
    filepath = input("Entrez le nom du fichier :")
    filepath = "../Sujet/Instances_compétition/" + filepath
    best = get_best_score(filepath)
    print(best, best.evaluate())
