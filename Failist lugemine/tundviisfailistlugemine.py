import os #lisab operatsiooni süsteemi ET KUSTUTADA SAAKS
'''if os.path.exists("teginfaili.txt"):
    print("Olemas fail")
    os.remove("teginfaili.txt")
    print("Fail kustutatud")
else:
    print("Faili ei ole")'''






#f = open("demo.txt", "r")
#print(f.read(20))
#print(f.readline())

#tekstisisu = f.read(100)
#print(tekstisisu)
#testilist = []

'''for x in f:
    print(x)
    testilist.append(x)
print(testilist)

f.close'''

#x = open("isetehtud.txt", "x") - SELLEGA TEEB UUE FAILI
'''f = open("teginfaili.txt", "a")
f.write("minu kirjutatud tekst")
f.close
f = open("teginfaili.txt", "w")
f.write("Kirjutasin üle")
f.close'''

'''if os.path.exists("test1.txt")==False:
    f = open("test1.txt", "x")
    f.write("andmed selles failis")
    f.close'''
'''f = open("test1.txt", "r")
print(f.read())'''

'''for x in range(10):
    f = open("test1.txt", "a")
    if x==1:
        f.write("\n uus lisatud rida")
    if x==2:
        f.write("\n teine lisatud rida")
    else:
        f.write("\n lisarida")'''

#os.mkdir("teginkausta") #- TEEB KAUSTA
#os.rmdir("teginkausta") - KUSTUTAB KAUSTA
os.chdir("./teginkausta/") #LÄHEB PATHIGA SINNA KAUSTA
