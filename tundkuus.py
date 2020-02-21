import os
muutuja=True
if os.path.exists("uusfail.txt"):
    print("Hakkame siis siia teksti lisama")
    x=open("uusfail.txt", "a")
else:

    x=open("uusfail.txt", "x")
    

while muutuja==True:
    sisend = input("Lisa tekst - ")
    if sisend=="x":
        muutuja=False
    else: x.write(sisend + "\n")
    
x.close





