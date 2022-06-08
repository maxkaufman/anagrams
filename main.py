with open("wordbank.txt", "r") as myfile:
    masterlist = []
    for i in myfile:
        masterlist.append(i[:-1])

from itertools import product
from string import ascii_lowercase
keywords = [''.join(i) for i in product(ascii_lowercase, repeat = 3)]

bestana = ""
bestscore = 0
for currana in keywords:
    currscore = 0
    for dicword in masterlist:
        check = True
        for currdiclet in dicword:
            if dicword.count(currdiclet) > currana.count(currdiclet):
                check = False
        if check == True:
            if len(dicword) == 3:
                currscore += 100
            if len(dicword) == 4:
                currscore += 400
            if len(dicword) == 5:
                currscore += 1200
            if len(dicword) == 6:
                currscore += 2000
    if currscore > bestscore:
        bestscore = currscore
        bestana = currana

print(bestscore, bestana)
