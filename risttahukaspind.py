def risttahukas_pind():
    kulga = int(input("Anna esimene külg? - "))
    kulgb = int(input("Anna teine külg? - "))
    kulgc = int(input("Anna kolmas külg? - "))
    x = 2*(kulga*kulgb+kulgb*kulgc+kulga*kulgc)
    return x

def risttahukas_ruumala():
    kulga = int(input("Anna esimene külg? - "))
    kulgb = int(input("Anna teine külg? - "))
    kulgc = int(input("Anna kolmas külg? - "))
    x = kulga*kulgb*kulgc
    return x