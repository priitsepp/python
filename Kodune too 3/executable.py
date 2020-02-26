from functions import *

#Muutujad
mangija = "X"
arvuti = "O"
mangKaib = True
kaiguVaartus = 0
mangulaud = [".",".",".",".",".",".",".",".",".","."]
sygavus = 2

#Mänguprotsess
while mangKaib:
    if sygavus<9:
        joonista(mangulaud)
        kaiguVaartus = int(input("Sisesta käik - "))
        if sygavus==2:
            muutuja = arvutiKaik(mangulaud, arvuti)
            print(muutuja)
            teeKaik(mangulaud, muutuja, arvuti)
            if winning(mangulaud, arvuti):
                print("Võit!!!")
                mangKaib = False
            
        teeKaik(mangulaud, kaiguVaartus, mangija)
        if winning(mangulaud, mangija):
            print("Võit!!!")
            mangKaib = False
        else:
            continue
        sygavus=sygavus+1
        print(sygavus)
  
  
  
  
  
  
  
  
  
  
  
  
  
  
    else:
        joonista(mangulaud)
        print("Viik!")
        mangKaib = False


