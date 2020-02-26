import random()

def joonista(mangulaud):
    print(mangulaud[7] + "|" + mangulaud[8] + "|" + mangulaud[9])
    print(mangulaud[4] + "|" + mangulaud[5] + "|" + mangulaud[6])
    print(mangulaud[1] + "|" + mangulaud[2] + "|" + mangulaud[3])

def joonistateine(mangulaud):
    lauaDublikaat = []

    for i in mangulaud:
        lauaDublikaat.append(i)

    return lauaDublikaat


def teeKaik(mangulaud, kaik, kelle):
    if kaik < 10:
        mangulaud[kaik] = kelle

def winning(ad, mangija):
    return((ad[1] == mangija and ad[2] == mangija and ad[3] == mangija) or
    (ad[1] == mangija and ad[4] == mangija and ad[7] == mangija) or
    (ad[1] == mangija and ad[5] == mangija and ad[9] == mangija) or
    (ad[3] == mangija and ad[6] == mangija and ad[9] == mangija) or
    (ad[2] == mangija and ad[5] == mangija and ad[8] == mangija) or
    (ad[4] == mangija and ad[5] == mangija and ad[6] == mangija) or
    (ad[7] == mangija and ad[8] == mangija and ad[9] == mangija) or
    (ad[7] == mangija and ad[5] == mangija and ad[3] == mangija))

def kontrollikasvaba(mangulaud, kaik):
    return mangulaud[kaik] == "."

def kaigugenereerija(mangulaud, kaigud):

      voimalikudKaigud = []

      for i in kaigud:

          if kontrollikasvaba(mangulaud, i):

              voimalikudKaigud.append(i)

 

      if len(voimalikudKaigud) != 0:

          return random.choice(voimalikudKaigud)

      else:

          return None

def arvutiKaik(mangulaud, arvuti):

    for z in range(1, 10):
         kopeerimine = joonistateine(mangulaud)
         if kontrollikasvaba(kopeerimine, z):
            teeKaik(kopeerimine, z, "O")
            if winning(kopeerimine, "O"):
                 return z

    for y in range(1,10):
        kopeerime = joonistateine(mangulaud)
        if kontrollikasvaba(kopeerime, y):
            teeKaik(kopeerime, y, "X")
            if winning(kopeerime, "X"):
                return y



