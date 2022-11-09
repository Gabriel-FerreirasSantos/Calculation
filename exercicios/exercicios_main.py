from replit import clear
import random


def exercicio_adiçãoleve1():
    clear()
    print('Resolva essa conta:')
    x = random.randint(0, 100)
    y = random.randint(0, 100)
    resultado = int(x) + int(y)
    resposta = input(f'{x} + {y} =').replace('', ' ')
    while True:
        if not resposta.isnumeric():
            print('Você não digitou um número')
            print('Você precisa digitar um número!')
            break

    resposta = int(resposta)
    while True:
        if resposta == resultado:
            print('Acertou!')
            print(f'{x} + {y} = {resultado}')
            
        elif resposta != resultado:
            print('Respota errada!')
            voltar = input('Deseja tentar novamente? (s/n)')
            if voltar == 's':
                break
           


def exercicio_adiçãoleve2():
    x = random.randint(0, 1000)
    y = random.randint(0, 1000)
    r = x + y
    print(f'{x} + {y} = {r}')

def exercicio_adiçãoleve3():
    x = random.randint(0, 100000)
    y = random.randint(0, 100000)
    r = x + y
    print(f'{x} + {y} = {r}')

def exercicio_adiçãoleve4():
    x = random.randint(0, 10000000)
    y = random.randint(0, 10000000)
    r = x + y
    print(f'{x} + {y} = {r}')









def exercicio_subtração():
    x = random.randint(0, 1000000)
    y = random.randint(0, 1000000)
    r = x - y
    print(f'{x} - {y} = {r}')

