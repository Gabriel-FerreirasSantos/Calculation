import math

def contademais():
    a = int(input('Digite um numero: '))
    b = int(input('Digite outro: '))
    s = (a + b)
    print('Resultado =',s)

def contademenos():
    a = int(input('Digite um numero: '))
    b = int(input('Digite outro: '))
    s = (a - b)
    print('Resultado =',s)    

def contadedividir():
    a = float(input('Digite um numero: '))
    b = float(input('Digite outro: '))
    s3 = (a / b)
    print('Resultado =',s3)

def contademutiplicação():
    a = int(input('Digite um numero: '))
    b = int(input('Digite outro: '))
    s4 = (a * b)
    print('Resultado =',s4)  

def contaderaiz():
    num = float(input("Digite um numero:\n"))
    raiz = math.pow(num, 1/2)
    print('Resultado =','{:.1f}'.format(raiz))

def contadepotenciação():
    a = float(input('Digite um numero: '))
    b = float(input('Digite outro: '))
    s6 = (a ** b)
    print('Resultado =','{:.1f}'.format(s6))                     