#import random as x

#suvaline = x.randint(1,20)
#print(suvaline)

import random as x
muutuja=True

vastus = x.randint(1,2)
misnumber=int(input("Mis numbri peale ma mõtlen vahemikus 1-2? -"))
print(misnumber)

while muutuja:
    if misnumber==vastus:
        print("Õige vastus!")
        muutuja=False
    else:
        if misnumber>vastus:
            print("Arv on väiksem")
            misnumber=int(input("Mis numbri peale ma mõtlen vahemikus 1-20? -"))
        else:
            print("Arv on suurem")
            misnumber=int(input("Mis numbri peale ma mõtlen vahemikus 1-20? -"))
            
#input()

'''thisdict = {
    "mark": "Audi",
    "mudel": "Quattro",
    "aasta": 1996
    }
print(thisdict)

x = thisdict["mudel"]
print(x)
y = thisdict.get("aasta")
print(y)

thisdict["varv"] = "punane"  #see lisab ühe rea dictionarysse
print(thisdict)

thisdict["aasta"] = 2018 # muudab väärtuse olemasolevas dictionarys
print(thisdict)

for x in thisdict:
    print(x)
thisdict.pop("mudel") #pop eemaldab (remove eemaldab väärtuse)
print(thisdict)

uusdict = {
    "kata": "Audi",
    "katb": "BMW"
    }'''
'''teinemuutuja=True
while teinemuutuja:   #range määrab mitu korda loop jookseb for jaoks
    kategooria = input("Kategooria")
    uusdict[kategooria] = input
    if kategooria == "ALL":
        teinemuutuja=False
print(uusdict)'''



'''testDict = {                    #harjutus kuidas muuta väärtust
    "liik":"Ahven",
    "vanus":12,
    "värv":"hall"
    }
print(testDict)
for x in testDict:
    inputVariable = input(" - ")
    if inputVariable == "ALL":
        break
    else:
        testDict[x] = inputVariable
print(testDict)'''



    