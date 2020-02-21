def joonista(mangulaud):
    print(mangulaud[7] + "|" + mangulaud[8] + "|" + mangulaud[9])
    print(mangulaud[4] + "|" + mangulaud[5] + "|" + mangulaud[6])
    print(mangulaud[1] + "|" + mangulaud[2] + "|" + mangulaud[3])

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
