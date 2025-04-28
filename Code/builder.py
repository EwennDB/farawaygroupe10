import json
"""
with open("Data/sanctuaire.txt") as file:
    lines = [line.rstrip() for line in file]
    print(lines)
    with open("Data/sanctuaire.json", "w") as f2:
        data = []
        for i in lines:
            lst = []
            j = int(i[:3])
            lst.append(j)
            if i[3] == "-":
                lst.append(None)
            else:
                lst.append(i[3])
            if i[4] == "-":
                lst.append(False)
            else:
                lst.append(True)
            if i[5] == "-":
                lst.append(False)
            else:
                lst.append(True)
            if i[6] == "-":
                lst.append({"p":0, "cha":0, "chi":0})
            elif i[6] == "p":
                lst.append({"p":1, "cha":0, "chi":0})
            elif i[8] == "a":
                lst.append({"p":0, "cha":1, "chi":0})
            else:
                lst.append({"p":0, "cha":0, "chi":1})
            data.append(lst)
        json.dump(data, f2)
"""
"""
with open("Data/cards.txt") as file:
    lines = [line.rstrip() for line in file]
    print(lines)
    with open("Data/cards.json", "w") as f2:
        data = []
        k = 1
        for i in lines:
            lst = []
            if k <=9:
                j = int(i[:1])
                z = 0
            else:
                j = int(i[:2])
                z = 1
            lst.append(j)
            if i[z+1] == "-":
                lst.append(None)
            else:
                lst.append(i[z+1])
            if i[z+2] == "-":
                lst.append(False)
            else:
                lst.append(True)
            if i[z+3] == "-":
                lst.append(False)
            else:
                lst.append(True)
            if i[z+4] == "-":
                lst.append({"p":0, "cha":0, "chi":0})
            elif i[z+4] == "p":
                lst.append({"p":1, "cha":0, "chi":0})
                if i[z+5] == "c":
                    if i[z+7] == "a":
                        lst[4]["cha"]+=1
                    elif i[z+7] == "i":
                        lst[4]["chi"]+=1
                elif i[z+5] == "p":
                    lst[4]["p"]+=1
            elif i[z+4] == "c":
                if i[z+6] == "a":
                    lst.append({"p":0, "cha":1, "chi":0})
                else:
                    lst.append({"p":0, "cha":0, "chi":1})
                if i[z+7] == "c":
                    if i[z+9] == "a":
                        lst[4]["cha"]+=1
                    elif i[z+9] == "i":
                        lst[4]["chi"]+=1
                elif i[z+7] == "p":
                    lst[4]["p"]+=1
            data.append(lst)
            k+=1
        json.dump(data, f2)
"""
