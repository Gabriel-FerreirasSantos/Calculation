import math

def contademais():
    while True:
        a = input('Digite um numero: ')
        b = input('Digite outro: ')
        if not a.isnumeric() or not b.isnumeric():
            print('Você não digitou um número')
            print('Você precisa digitar um número!')
            break
        s = float(a) + float(b)
        print('Resultado = {:.2f}'.format(s))
        break

def contademenos():
    while True:
        a = input('Digite um numero: ')
        b = input('Digite outro: ')
        if not a.isnumeric() or not b.isnumeric():
            print('Você não digitou um número')
            print('Você precisa digitar um número!')
            break
        s = float(a) - float(b)
        print('Resultado = {:.2f}'.format(s))
        break   

def contadedividir():
    while True:
        a = input('Digite um numero: ')
        b = input('Digite outro: ')
        if not a.isnumeric() or not b.isnumeric():
            print('Você não digitou um número')
            print('Você precisa digitar um número!')
            break
        s3 = float(a) /  float(b)
        print('Resultado = {:.2f}'.format(s3))
        break

def contademutiplicação():
    while True:
        a = input('Digite um numero: ')
        b = input('Digite outro: ')
        if not a.isnumeric() or not b.isnumeric():
            print('Você não digitou um número')
            print('Você precisa digitar um número!')
            break
        s4 = float(a) * float(b)
        print('Resultado = {:.2f}'.format(s4))  
        break

def contaderaiz():
    while True:
        num = input("Digite um numero:\n")
        if not num.isnumeric():
            print('Você não digitou um número')
            print('Você precisa digitar um número!')
            break
        raiz = math.pow(float(num), 1/2)
        print('Resultado =','{:.2f}'.format(raiz))
        break

def contadepotenciação():
    while True:
        a = input('Digite um numero: ')
        b = input('Digite outro: ')
        if not a.isnumeric() or not b.isnumeric():
            print('Você não digitou um número')
            print('Você precisa digitar um número!')
            break
        s6 = float(a) ** float(b)
        print('Resultado =','{:.2f}'.format(s6))     
        break                