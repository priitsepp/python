def kolmnurga_pind():
    korg = int(input("Anna kolmnurga kõrgus? - "))
    alus = int(input("Anna kolmnurga alus? - "))
    x = korg*alus/2
    return x

def kolmnurga_ymber():
    kolma = int(input("Anna kolmnurga esimene külg? -"))
    kolmb = int(input("Anna kolmnurga teine külg? -"))
    kolmc = int(input("Anna kolmnurga kolmas külg? -"))
    x = kolma + kolmb + kolmc
    return x