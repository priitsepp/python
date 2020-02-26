'''import random #vaja alati kui tahame randomit kasutada
nimekiri = ["kivi" , "paber" , "käärid"]
vordleja = True

def mang():
    arvutiotsib = random.randint(0,2)  #random.randint - et ta otsiks randomi funktsioonist mitte meie enda funktsiooni
    sisend = input("kivi, paber või käärid? - ")
    if sisend in nimekiri:
        arvutivastus = nimekiri[arvutiotsib]
        if sisend==arvutivastus:
            print("Viik")
        if sisend=="kivi" and arvutivastus=="käärid":
            print("Võitsid :)")
        if sisend=="kivi" and arvutivastus=="paber":
            print("Kaotasid :(")
        if sisend=="paber" and arvutivastus=="kivi":
            print("Võitsid :)")
        if sisend=="paber" and arvutivastus=="käärid":
            print("Kaotasid :(")
        if sisend=="käärid" and arvutivastus=="kivi":
            print("Kaotasid :(")
        if sisend=="käärid" and arvutivastus=="paber":
            print("Võitsid :)")
    else:
        raise TypeError("Sisend tuleb valida nimekirjast! Sa ei oska mängida!")

while vordleja:      #loop peab olema allpool sest ta muidu pole veel funktsiooni lugenud ega teaks mida kutsuda
    mang()
    break'''


import random #vaja alati kui tahame randomit kasutada
nimekiri = ["kivi" , "paber" , "käärid"]
vordleja = True

try:
    def mang():
        arvutiotsib = random.randint(0,2)  #random.randint - et ta otsiks randomi funktsioonist mitte meie enda funktsiooni
        sisend = input("kivi, paber või käärid? - ")
        if sisend not in nimekiri:
            sisend()
        else:
            arvutivastus = nimekiri[arvutiotsib]
            if sisend==arvutivastus:
                print("Viik")
            if sisend=="kivi" and arvutivastus=="käärid":
                print("Võitsid :)")
            if sisend=="kivi" and arvutivastus=="paber":
                print("Kaotasid :(")
            if sisend=="paber" and arvutivastus=="kivi":
                print("Võitsid :)")
            if sisend=="paber" and arvutivastus=="käärid":
                print("Kaotasid :(")
            if sisend=="käärid" and arvutivastus=="kivi":
                print("Kaotasid :(")
            if sisend=="käärid" and arvutivastus=="paber":
                print("Võitsid :)")


    while vordleja:      #loop peab olema allpool sest ta muidu pole veel funktsiooni lugenud ega teaks mida kutsuda
        mang()
        break
except:
    print("Vale sisend")