import copy

def add_dict(dict1, dict2):
    dict3 = copy.deepcopy(dict2)
    for i, j in dict1.items():
        if i in dict3.keys():
            dict3[i] += j
        else:
            dict3[i] = j

    return dict3