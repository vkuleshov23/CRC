from operator import mod
import re
import numpy as np
import numpy.random as rand
import matplotlib.pyplot as pl

#k - число информационных символоы передаемого сообщения m
# r = Максимальная степень многочлена - определяет кол-во бит контрольной суммы
# кодер хранит пораждающий многочлен g(x)
gx = np.array([1,0,1,1])
r = gx.size - 1 # кол-во бит в контрольной сумме
r_add = np.zeros(r, dtype=int) # добавочное ( для смещения )
eps = 0.01 # точность 
N = int(9/(4*eps**2))# кол-во необходимых модуляций 


def div(a, b):
    dividend = a.copy()  
    divider = b.copy()  
    quotient = []  
    if deg(dividend) < deg(divider):
        return dividend

    while True:
        j = deg(dividend)
        if j < deg(divider):
            break
        t = deg(dividend) - deg(divider)
        if t != 0:
            quotient = plus(quotient, mul([1], t))
            tmp = mul(divider, t)
        else:
            quotient = plus(quotient, [1])
            tmp = divider
        dividend = xor(dividend, tmp)
    return dividend

def mul(a, b):
    tmp = a.copy()
    for i in range(b):
        tmp.append(0)
    return tmp

def plus(a1, b1):
    tmp = []
    a = a1.copy()
    b = b1.copy()
    if len(a) > len(b):
        while len(a) > len(b):
            b.insert(0, 0)
    elif len(a) < len(b):
        while len(a) < len(b):
            a.insert(0, 0)
    for i in range(len(b) - 1, -1, -1):
        tmp.insert(0, b[i] ^ a[i])
    return tmp

def deg(m):
    if m[0] == 1:
        return len(m) - 1
    else:
        for i in range(len(m)):
            if m[i] == 1:
                return len(m) - 1 - i
    return 0

def xor(a, b):
    tmp = []
    if len(a) > len(b):
        while len(a) > len(b):
            b.insert(0, 0)
    elif len(a) < len(b):
        while len(a) < len(b):
            a.insert(0, 0)
    for i in range(len(a)):
        tmp.append(a[i] ^ b[i])
    if 1 not in tmp:
            return tmp
    while True:
        if tmp[0] == 1:
            break
        else:
            tmp.pop(0)
    return tmp


#КОДЕР 
def shift(m):
    return np.append(m,r_add)

def mod2(m):
    for i in range(len(m)):
        m[i] = (int)(m[i]%2)
    return m

def createWord(mess):
    mxr = shift(mess) # m(x)* x^r
    c = div(mxr,gx) # m(x)/g(x)
    # c = mod2(c) # C(x)
    return np.polyadd(mxr,c) #a(x) = m(x)*x^r + C(x)


# ДЕКОДЕР

def createE(p, n): 
    e = np.zeros(n)
    for i in range(n):
        tnprsnd = rand.random()
        #print("rand", tnprsnd)
        if tnprsnd < p:
            e[i] = 1
    return e

def isNull(c):
    return np.all(c==0)

def checkWord(b): # вычисляем синдром 
    c = div(b, gx)
    # c = mod2(c)
    return isNull(c)


def checkE(e):
    return isNull(e)

def checkDecodeError(b,e):
    return (checkWord(b) != checkE(e))



#НАХОДИМ ОШИБКИ
def findPropDecodError(mess, p):
    a = createWord(mess)
    l = len(a)
    error = 0
    for i in range(N):
        e = createE(p, l)
        b = mod2(np.polyadd(a,e)) # формируем принятое сообщение 
        if(checkDecodeError(b,e)):
            error += 1
    #print("erroк: ",error)
    return error/N # вероятность ошибк декодирования
    
    
def Plot(ernoP, p, l):

    pl.plot(p, ernoP)
    pl.title('l=' + str(l))
    myfile = 'l' + str(l) + '.png'
    pl.grid(True)
    pl.savefig(myfile)
   
    pl.grid(True)
    pl.show()

def printResult(ernoP, p, l):
    for i in range(len(p)):
        print("p: ", p[i],   " Err/N: ", ernoP[i])

def createNewWord( n): 
    mes = np.zeros(n)
    for i in range(n):
        tnprsnd = rand.random()
        #print("rand", tnprsnd)
        if tnprsnd < 0.5:
            mes[i] = 1
    return mes



ernoP = np.zeros(11)
p = np.array([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
for l in range(2, 3):
    print("__________________l = ", l ,"_________________________________")

    for i in range(len(p)):
        mess = createNewWord(l)
        #print("mess: ",mess )
        # for r in range(2**l):
        #     #mess = np.unpackbits(np.uint8(r)) # генерируем случайное сообщение
        #     #print("mess: ",np.array(mess[len(mess) - l:]) , "i: ", i)
        #     #ernoP[i] += findPropDecodError(np.array(mess[len(mess) - l:]), p[i])
           
             
        #     #print("p: ", p[i]," mess: ",np.array(mess[len(mess) - l:]),   " Err/N: ", ernoP[i]/2**l)
        ernoP[i] = findPropDecodError(mess, p[i])
        #ernoP[i] /= 2**l
        #print("p: ", p[i],   " Err/N: ", ernoP[i])
    Plot(ernoP,p, l)
    printResult(ernoP, p, l)

    #printResult(ernoP, p, l)

    



#arr = np.array([1,1,0,0])
#resTmp = createWord(arr)
#print("a(x): ",resTmp)
#print("size a(x)",resTmp.size)