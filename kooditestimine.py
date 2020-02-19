try:                   #ÜLEJÄÄNUD KOODI JOOKSUTAB AINULT TRY JÄTAB VÄLJA
    print(jama)
except NameError:       #MUUTUJAT POLE OLEMAS
    print("Muutujat pole olemas")
    mingiArv = 10
    print(mingiArv)
except:
    print("On muu viga")
else:
    print("Vigu pole")
finally:       #jookseb kui on viga või kui ei ole viga!
    print("Nüüd saan teha seda")


try:
    f = open("kooditestimine.py")
    f.write(
        "Ei saa kirjutada"
    )
except:
    print("faili avamisel tekkis probleem")
finally:
    f.close

number = 20
if number > 10:
    raise Exception("Sorry see number ei sobi")   #ANNAB VEALE INFORMATSIOONI JUURDE

