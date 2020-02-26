'''stopper = True
sygavus = 0
def recursive(x):
    while stopper:
        if x<10:
            print(x)
            x=x+1
            recursive(x)

recursive(sygavus)'''

'''stopper = True
muut = 0
def recursive(x):
    while stopper:
        if x<1000:
            print(x)
            x=x+12
            recursive(x)

recursive(muut)'''

#faktoriaal (6!=6x5x4x3x2x1)

'''def faktoriaal(x):
    if x == 1:
        return 1
    else:
        print(x)
        return (x * faktoriaal(x-1))

number = 6
print("Numbri", number , "faktoriaal on ", faktoriaal(number))'''

'''def summad(n) :              #fibonacci number
    if n==1:
        return 1
    return n+summad(n-1)

print(summad(16))'''

