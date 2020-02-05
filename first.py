from math import*

#print("hello world")
#print("Ti \nme", end=" ")
#print("did it?")
#print(6-3)
#pindala=20.04889
#print(pindala)
#print(pindala,"midagi muud")
#kala=30
#print(pindala+kala)
#kokku=pindala*kala
#print(kokku)
#print("Pindala on %0.2f." % (pindala))

#kasutaja=input("Mis on su nimi? - ")
#print(kasutaja)

#arvEsimene= int(input("Esimene arv? - "))
#arvTeine= int(input("Teine arv? - "))

#print(arvEsimene + arvTeine)

#meieEsimene=["politsei","tuletõrje","kiirabi"]

#print(meieEsimene[1])

#meieTeine=["kala","koer","ahv"]

#print(meieEsimene + meieTeine)
#print(meieEsimene[1]+meieTeine[0])

#ruut=int(input("Ruudu külg? - "))
#print(ruut*ruut)

#ristkülik1=int(input("Ristküliku külg 1? -"))
#ristkülik2=int(input("Ristküliku külg 2? -"))
#print(ristkülik1*ristkülik2)
#print(ristkülik1+ristkülik1+ristkülik2+ristkülik2)

#külgEsi=int(input("Kolmnurga külg 1? - "))
#külgTei=int(input("Kolmnurga külg 2? - "))
#külgKol=int(input("Kolmnurga külg 3? - "))
#print(külgEsi*külgTei/2)
#print(külgEsi+külgKol+külgTei)

#print(abs(-3))
#print(round(2.67443, 2))
#print(5**3)
#print(5//3)

#tester = False
#topelt = True

#if 5+1==6:
    #print(topelt)
#if 78+54==100:
    #print(topelt)

#värv=input("Mis värv on? - ")

#if värv=="sinine":
   # print(1)
#if värv=="punane":
   # print(2)
#if värv=="must":
   # print(3)

nimi = "tester"
print(len(nimi))
if len(nimi)>8:
    print("Liiga pikk")

kasutajanimi=input("Kes sa oled? - ")
if len(kasutajanimi)>20:
    print("Error")
if len(kasutajanimi)<8:
    print("Error")
elif len(nimi)<3:
    print("Toene!")
else:
    print("Nojah")
if 3>2: print("shorthand")