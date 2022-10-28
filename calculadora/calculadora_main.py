import math

def contademais():
    while True:
        a = input('Digite um numero: ')
        b = input('Digite outro: ')
        if not a.isnumeric() and not b.isnumeric():
            print('Você não digitou um número')
            print('Você precisa digitar um número!')
            break
        s = int(a) + int(b)
        print('Resultado = {:.2f}'.format(s))
        break

def contademenos():
    a = int(input('Digite um numero: '))
    b = int(input('Digite outro: '))
    s = (a - b)
    print('Resultado = {:.2f}'.format(s))    

def contadedividir():
    a = float(input('Digite um numero: '))
    b = float(input('Digite outro: '))
    s3 = (a / b)
    print('Resultado =',s3)

def contademutiplicação():
    a = int(input('Digite um numero: '))
    b = int(input('Digite outro: '))
    s4 = (a * b)
    print('Resultado = {:.2f}'.format(s4))  

def contaderaiz():
    num = float(input("Digite um numero:\n"))
    raiz = math.pow(num, 1/2)
    print('Resultado =','{:.2f}'.format(raiz))

def contadepotenciação():
    a = float(input('Digite um numero: '))
    b = float(input('Digite outro: '))
    s6 = (a ** b)
    print('Resultado =','{:.2f}'.format(s6))                     