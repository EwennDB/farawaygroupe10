from solver import get_best_score

if __name__ == '__main__':
    
    filepath = input("Entrez le nom du fichier :")
    filepath = "../Sujet/Instances_compétition/" + filepath
    best = get_best_score(filepath)
    print(best, best.evaluate())
