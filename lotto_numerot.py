##pip install numpy
##pip3 install numpy
from random import randrange
import random

LOTTONUMEROTLISTA =[]
for LOTTONUMEROT in range(1,41):
    LOTTONUMEROTLISTA.append(LOTTONUMEROT)
#print(LOTTONUMEROTLISTA)

def LOTTORIVI_LUOJA():
    global LOTTORIVI
    LOTTORIVI = []
    o = 7
    i = 0
    while i < o:
        x = randrange(len(LOTTONUMEROTLISTA))
        numero = LOTTONUMEROTLISTA[x]
        if numero in LOTTORIVI :
            o += 1
            
            
        else:
            if len(LOTTORIVI) < 7:
                LOTTORIVI.append(numero)
                i += 1
                
            else:
                #print(len(LOTTORIVI))
                break

    #print(LOTTORIVI)

lottorivi_numeroiden_lista6 = []
def LOTTORIVI_arpoja():
    b= 0
    #109999
    while b < 109999 :
        lottorivi_numeroiden_lista = []
        lottorivi_numeroiden_lista2 = []
        lottorivi_numeroiden_lista3 = []
        lottorivi_numeroiden_lista4 = []
        lottorivi_numeroiden_lista5 = []
        
        i= 0
        while i < 3:
            LOTTORIVI_LUOJA()
            #print(LOTTORIVI)
            lottorivi_numeroiden_lista.append(LOTTORIVI)
            
            i+= 1
        #print(lottorivi_numeroiden_lista)
        x = random.choice(lottorivi_numeroiden_lista)
        lottorivi_numeroiden_lista2.append(x)
        o= 0
        while o < 3:
            LOTTORIVI_LUOJA()
            #print(LOTTORIVI)
            lottorivi_numeroiden_lista2.append(LOTTORIVI)
            
            o+= 1
        u = random.choice(lottorivi_numeroiden_lista2)
        lottorivi_numeroiden_lista3.append(u)
        n= 0
        while n < 3:
            LOTTORIVI_LUOJA()
            #print(LOTTORIVI)
            lottorivi_numeroiden_lista3.append(LOTTORIVI)
            
            n+= 1
        u = random.choice(lottorivi_numeroiden_lista3)
        lottorivi_numeroiden_lista4.append(u)
        n= 0
        while n < 3:
            LOTTORIVI_LUOJA()
            #print(LOTTORIVI)
            lottorivi_numeroiden_lista4.append(LOTTORIVI)
            
            n+= 1
        u = random.choice(lottorivi_numeroiden_lista4)
        lottorivi_numeroiden_lista5.append(u)
        n= 0
        while n < 3:
            LOTTORIVI_LUOJA()
            #print(LOTTORIVI)
            lottorivi_numeroiden_lista5.append(LOTTORIVI)
            
            n+= 1
        u = random.choice(lottorivi_numeroiden_lista4)
        lottorivi_numeroiden_lista6.append(u)
        b+= 1
        #print(lottorivi_numeroiden_lista6)
    #print(lottorivi_numeroiden_lista6)
    
LOTTONUMERO_LISTA =[]
LISANUMERO_LISTA =[]
LISANUMERO_LISTA2 =[]
LISANUMERO=""
def LOTTORIVI_lisanumero():
    
    global LISANUMERO
    LOTTONUMERO_LISTA.append(LOTTONUMEROTLISTA)
    for LOTTONUMERO_LISTA2 in LOTTONUMERO_LISTA:
        #print(LOTTONUMERO_LISTA2)
        
                  
            ##print(LOTTONUMERO_LISTA2)
            #for y in x:
                #print(x)   
                #LOTTONUMERO_LISTA2.remove(x)
        LOTTONUMERO_LISTA2= [numeron for numeron in LOTTONUMERO_LISTA2 if numeron not in lottorivi_numeroiden_lista6]
    #print(x)         
    #print(LOTTONUMERO_LISTA2)
  
    n= 0
    while n < random.randrange(1,1+len(LOTTONUMERO_LISTA2)):
            u = random.choice(LOTTONUMERO_LISTA2)
            LISANUMERO_LISTA.append(u)
            
            n+= 1
    n= 0
    try:
        while n < random.randrange(1,1+len(LISANUMERO_LISTA)):
                u = random.choice(LISANUMERO_LISTA)
                LISANUMERO_LISTA2.append(u)
                
                n+= 1
        #print(LISANUMERO_LISTA2)
        LISANUMERO = random.choice(LISANUMERO_LISTA2)
        #print(lisanumero)
    except:
        #print("loppi")
        LISANUMERO = random.choice(LISANUMERO_LISTA)
        #print(lisanumero)
LOTTORIVI_arpoja()
LOTTORIVI_lisanumero()



for lottoumero in lottorivi_numeroiden_lista6:
    lottoumero.sort()
    #print(lottoumero)
res = '. '.join(map(str, lottoumero))
#print(res)

print("Lotto numerosi tänään: "+res+". lisänumero: "+ str(LISANUMERO)+".")