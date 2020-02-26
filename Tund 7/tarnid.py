'''mituTarni = int(input("Kui pikk on äär? - "))
i=1

for x in range(mituTarni):
    for x in range(mituTarni):
        print(x+i, end = '')
    i = i + mituTarni
    print()'''


'''mituTarni = int(input("Kui pikk on äär? - "))         #NESTED LOOPS KORRUTUSTABEL
i=0

for x in range(mituTarni):
    for x in range(mituTarni):
        print(i*x, end = '')
    i = i + 1
    print()'''

for y in range(1,11):
    for x in range(1,11):
        print(y*x, end = '')
    print()