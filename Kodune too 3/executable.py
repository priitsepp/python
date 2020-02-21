from functions import *

#Muutujad
mangija = "X"
arvuti = "O"
mangKaib = True
kaiguVaartus = 0
mangulaud = [".",".",".",".",".",".",".",".",".","."]
sygavus = 0

#Mänguprotsess
while mangKaib:
    if sygavus<9:
        joonista(mangulaud)
        kaiguVaartus = int(input("Sisesta käik - "))
        if mangulaud[kaiguVaartus] == ".":
            if sygavus%2:
                teeKaik(mangulaud, kaiguVaartus, arvuti)
                if winning(mangulaud, arvuti):
                    joonista.mangulaud
                    print("Võit!!!")
                    mangKaib = False
            else:
                teeKaik(mangulaud, kaiguVaartus, mangija)
                if winning(mangulaud, mangija):
                    joonista.mangulaud
                    print("Võit!!!")
                    mangKaib = False
        else:
            continue
        sygavus=sygavus+1
    else:
        joonista(mangulaud)
        print("Viik!")
        mangKaib = False


