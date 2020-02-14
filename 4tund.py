muutuja = 0
teinekoht = 0
koigevaiksem = 3000
thislist = [1990, 1996, 2007, 2013, 2018, 2004]
for x in thislist:
    if muutuja<x:
        teinekoht = muutuja
        muutuja = x
    if x<koigevaiksem:
        koigevaiksem = x

'''print(muutuja)
print(teinekoht)
print(koigevaiksem)'''

print(max(thislist))
print(min(thislist))