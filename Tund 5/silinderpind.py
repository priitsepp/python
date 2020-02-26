def silinder_pind():
    pohjapind = int(input("Anna külgpindala? - "))
    pohitahk = int(input("Anna põhitahu pindala? - "))
    x = pohjapind+2*pohitahk
    return x

def silinder_ruumala():
    pohjapind = int(input("Anna põhjapindala? - "))
    korgus = int(input("Anna kõrgus? - "))
    x = pohjapind*korgus
    return x