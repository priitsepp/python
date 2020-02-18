def pyramiid_pind():
    pohjapind = int(input("Anna põhjapindala? - "))
    kuljepind = int(input("Anna kuljepind? - "))
    x = pohjaping + kuljepind
    return x

def pyramiid_ruumala():
    pohjapind = int(input("Anna põhjapindala? - "))
    korgus = int(input("Anna kõrgus? - "))
    x = 1/3*pohjapind*korgus
    return x