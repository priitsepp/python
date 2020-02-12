def hello(sisend, sisendkaks):
    print(sisend + sisendkaks)
    
#hello(10,10)

def hallo(**sisse):
    print(sisse["aasta"])
    
#hallo(mudel = "Kala", aasta = 1990)
    
def vastus(x):
    return 20*x

tester = vastus(30)
#print(tester)

def ruudupindala(külg):
    print(külg*külg)
#ruudupindala(4)

def loekümneni():
    for x in range(1,11):              #range on vahemik
        print(x)
loekümneni()
        
#anname numbri ja ta loeb sealt edasi sajani
sisend=int(input("Anna number?-"))

def loesajani(algus):
    for x in range(algus,101):
           print(x)
loesajani(sisend)

#teeme tühja nimekirja, küsime kasutajalt 10 sisendit ja siis prindime selle välja

list=[]

def ülesanne():
    for x in range(1,11):
        word=input("Ütle midagi?-")
        list.append(word)
    print(list)
ülesanne()
    