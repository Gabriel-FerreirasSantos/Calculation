from replit import clear
import random


def exercicio_adiçãoleve1():
    clear()
    print('Resolva essa conta:')
    x = random.randint(0, 100)
    y = random.randint(0, 100)
    a = True
    while a == True:
        a = True
        resposta = input(f'{x} + {y} =').strip()
        if not resposta.isnumeric():
            print('Você não digitou um número')
            print('Você precisa digitar um número!')
            break

        while True:
            resultado = int(x) + int(y)
            resposta = int(resposta)

            if resposta == resultado:
                clear()
                print('Acertou!')
                print(f'{x} + {y} = {resultado}')
                a = False
                break

            elif resposta != resultado:
                print('Respota errada!')
                voltar = input('Deseja tentar novamente? (s/n)')
                if voltar == 's':
                    clear()
                    break
                        
def exercicio_adiçãoleve2():
    clear()
    print('Resolva essa conta:')
    x = random.randint(100, 1000)
    y = random.randint(100, 1000)
    a = True
    while a == True:
        a = True
        resposta = input(f'{x} + {y} =').strip()
        if not resposta.isnumeric():
            print('Você não digitou um número')
            print('Você precisa digitar um número!')
            break

        while True:
            resultado = int(x) + int(y)
            resposta = int(resposta)

            if resposta == resultado:
                clear()
                print('Acertou!')
                print(f'{x} + {y} = {resultado}')
                a = False
                break

            elif resposta != resultado:
                print('Respota errada!')
                voltar = input('Deseja tentar novamente? (s/n)')
                if voltar == 's':
                    clear()
                    break

def exercicio_adiçãoleve3():
    clear()
    print('Resolva essa conta:')
    x = random.randint(1000, 10000)
    y = random.randint(1000, 10000)
    a = True
    while a == True:
        a = True
        resposta = input(f'{x} + {y} =').strip()
        if not resposta.isnumeric():
            print('Você não digitou um número')
            print('Você precisa digitar um número!')
            break

        while True:
            resultado = int(x) + int(y)
            resposta = int(resposta)

            if resposta == resultado:
                clear()
                print('Acertou!')
                print(f'{x} + {y} = {resultado}')
                a = False
                break

            elif resposta != resultado:
                print('Respota errada!')
                voltar = input('Deseja tentar novamente? (s/n)')
                if voltar == 's':
                    clear()
                    break

def exercicio_adiçãoleve4():
    clear()
    print('Resolva essa conta:')
    x = random.randint(10000, 1000000)
    y = random.randint(10000, 1000000)
    a = True
    while a == True:
        a = True
        resposta = input(f'{x} + {y} =').strip()
        if not resposta.isnumeric():
            print('Você não digitou um número')
            print('Você precisa digitar um número!')
            break

        while True:
            resultado = int(x) + int(y)
            resposta = int(resposta)

            if resposta == resultado:
                clear()
                print('Acertou!')
                print(f'{x} + {y} = {resultado}')
                a = False
                break

            elif resposta != resultado:
                print('Respota errada!')
                voltar = input('Deseja tentar novamente? (s/n)')
                if voltar == 's':
                    clear()
                    break









def exercicio_subtraçãolevel1():
    clear()
    print('Resolva essa conta:')
    x = random.randint(0, 100)
    y = random.randint(0, 100)
    if y > x:
        x +=  y
    a = True
    while a == True:
        a = True
        resposta = input(f'{x} - {y} =').strip()
        if not resposta.isnumeric():
            print('Você não digitou um número')
            print('Você precisa digitar um número!')
            break

        while True:
            resultado = int(x) - int(y)
            resposta = int(resposta)

            if resposta == resultado:
                clear()
                print('Acertou!')
                print(f'{x} - {y} = {resultado}')
                a = False
                break

            elif resposta != resultado:
                print('Respota errada!')
                voltar = input('Deseja tentar novamente? (s/n)')
                if voltar == 's':
                    clear()
                    break

def exercicio_subtraçãolevel2():
    clear()
    print('Resolva essa conta:')
    x = random.randint(0, 1000)
    y = random.randint(0, 1000)
    if y > x:
        x +=  y
    a = True
    while a == True:
        a = True
        resposta = input(f'{x} - {y} =').strip()
        if not resposta.isnumeric():
            print('Você não digitou um número')
            print('Você precisa digitar um número!')
            break

        while True:
            resultado = int(x) - int(y)
            resposta = int(resposta)

            if resposta == resultado:
                clear()
                print('Acertou!')
                print(f'{x} - {y} = {resultado}')
                a = False
                break

            elif resposta != resultado:
                print('Respota errada!')
                voltar = input('Deseja tentar novamente? (s/n)')
                if voltar == 's':
                    clear()
                    break

def exercicio_subtraçãolevel3():
    clear()
    print('Resolva essa conta:')
    x = random.randint(0, 10000)
    y = random.randint(0, 10000)
    if y > x:
        x +=  y
    a = True
    while a == True:
        a = True
        resposta = input(f'{x} - {y} =').strip()
        if not resposta.isnumeric():
            print('Você não digitou um número')
            print('Você precisa digitar um número!')
            break

        while True:
            resultado = int(x) - int(y)
            resposta = int(resposta)

            if resposta == resultado:
                clear()
                print('Acertou!')
                print(f'{x} - {y} = {resultado}')
                a = False
                break

            elif resposta != resultado:
                print('Respota errada!')
                voltar = input('Deseja tentar novamente? (s/n)')
                if voltar == 's':
                    clear()
                    break

def exercicio_subtraçãolevel4():
    clear()
    print('Resolva essa conta:')
    x = random.randint(0, 100000)
    y = random.randint(0, 100000)
    if y > x:
        x +=  y
    a = True
    while a == True:
        a = True
        resposta = input(f'{x} - {y} =').strip()
        if not resposta.isnumeric():
            print('Você não digitou um número')
            print('Você precisa digitar um número!')
            break

        while True:
            resultado = int(x) - int(y)
            resposta = int(resposta)

            if resposta == resultado:
                clear()
                print('Acertou!')
                print(f'{x} - {y} = {resultado}')
                a = False
                break

            elif resposta != resultado:
                print('Respota errada!')
                voltar = input('Deseja tentar novamente? (s/n)')
                if voltar == 's':
                    clear()
                    break








def exercicio_divisãoleve1():
    clear()
    print('Resolva essa conta:')
    x = random.randint(2, 100)
    y = random.randint(2, 100)
    if y > x:
        x +=  y
    a = True
    while a == True:
        a = True
        resposta = input(f'{x} / {y} =').strip()
        if not resposta.isnumeric():
            print('Você não digitou um número')
            print('Você precisa digitar um número!')
            break

        while True:
            resultado = float(x) / float(y)
            resposta = int(resposta)

            if resposta == resultado:
                clear()
                print('Acertou!')
                print(f'{x} / {y} = {resultado}')
                a = False
                break

            elif resposta != resultado:
                print('Respota errada!')
                voltar = input('Deseja tentar novamente? (s/n)')
                if voltar == 's':
                    clear()
                    break