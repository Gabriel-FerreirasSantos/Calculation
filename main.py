#import's
from calculadora import calculadora_main
from exercicios import exercicios_main

from replit import clear
from time import sleep

#Programa principal
Variavel_while1 = False
Variavel_while2 = False
variavel_whileql = False

while Variavel_while1 == False:
    clear()
    print('-=' * 25)
    print(' ' * 10, 'Bem vindo ao painel da Takern')
    print('-=' * 25)
    print('Você deseja:')
    print('[1] Calculadora')
    print('[2] Fazer exercicios')
    print('[3] Fechar o programa')

    
    escolha = str(input('R:'))
    escolha = escolha.strip()
    Variavel_while2 = False
    variavel_whileql = False

    #verificar se o numero não é numerico
    if not escolha.isnumeric():
        print('Você não digitou um número')
        print('Você precisa digitar um número!')
        break
        
        
        
    escolha = int(escolha) #Transformo a escolha que esta em string para numero inteiro


    #verificação de qual numero foi escolhido
    while Variavel_while2 == False:
        if escolha == 1:
            while True:
                clear()
                print('-=' * 25)
                print(' ' * 10, 'Bem vindo a calculadora')
                print('-=' * 25)
                print('[1]Adição')
                print('[2]Subtração')
                print('[3]Divisão')
                print('[4]Mutiplicação')
                print('[5]Raiz quadrada')
                print('[6]Potenciação')
                print('[7]Voltar')
                escolha2 = input('R:')
                if escolha2 == '1':
                    while True:
                        clear()
                        calculadora_main.contademais()
                        print('Aperte qualquer botão para voltar')
                        botao = input('')
                        break

                elif escolha2 == '2':
                    while True:
                        clear()
                        calculadora_main.contademenos()
                        print('Aperte qualquer botão para voltar')
                        botao = input('')
                        break

                elif escolha2 == '3':
                    while True:
                        clear()
                        calculadora_main.contadedividir()
                        print('Aperte qualquer botão para voltar')
                        botao = input('')
                        break

                elif escolha2 == '4':
                    while True:
                        clear()
                        calculadora_main.contademutiplicação() 
                        print('Aperte qualquer botão para voltar')
                        botao = input('')
                        break

                elif escolha2 == '5':
                    while True:
                        clear()
                        calculadora_main.contaderaiz()
                        print('Aperte qualquer botão para voltar')
                        botao = input('')
                        break

                elif escolha2 == '6':
                    while True:
                        clear()
                        calculadora_main.contadepotenciação() 
                        print('Aperte qualquer botão para voltar')
                        botao = input('')
                        break
                    
                elif escolha2 == '7':
                    Variavel_while2 = True
                    break

                else:
                    while variavel_whileql == False:
                        print('Você não digitou um número da lista')
                        print('Você precisa digitar um número que esta na lista!')
                        print('Deseja voltar? (s/n)')
                        voltar = str(input('R:')).strip().lower()
                        if voltar == 's':
                            break
                        elif voltar == 'n':
                            print('Volte sempre!')
                            Variavel_while2 = True
                            Variavel_whileql = True
                            break
                        else:
                            print('Escreva direito!')
                            Variavel_while2 = True
                            Variavel_whileql = True
                            break


        elif escolha == 2:
            while True:
                clear()
                print('-=' * 25)
                print(' ' * 5, 'Bem vindo ao painel de exercicio da Takern')
                print('-=' * 25)
                print('[1]Adição')
                print('[2]Subtração')
                print('[3]Divisão')
                print('[4]Mutiplicação')
                print('[5]Raiz quadrada')
                print('[6]Potenciação')
                print('[7]Voltar')
                escolha2 = input('R:')
                if escolha2 == '1':
                    while True:
                        clear()
                        
                        print('Aperte qualquer botão para voltar')
                        botao = input('')
                        break

                elif escolha2 == '2':
                    while True:
                        clear()
                        
                        print('Aperte qualquer botão para voltar')
                        botao = input('')
                        break

                elif escolha2 == '3':
                    while True:
                        clear()
                        
                        print('Aperte qualquer botão para voltar')
                        botao = input('')
                        break

                elif escolha2 == '4':
                    while True:
                        clear()
                        
                        print('Aperte qualquer botão para voltar')
                        botao = input('')
                        break

                elif escolha2 == '5':
                    while True:
                        clear()
                        
                        print('Aperte qualquer botão para voltar')
                        botao = input('')
                        break

                elif escolha2 == '6':
                    while True:
                        clear()
                        
                        print('Aperte qualquer botão para voltar')
                        botao = input('')
                        break
                    
                elif escolha2 == '7':
                    Variavel_while2 = True
                    break

                else:
                    while variavel_whileql == False:
                        print('Você não digitou um número da lista')
                        print('Você precisa digitar um número que esta na lista!')
                        print('Deseja voltar? (s/n)')
                        voltar = str(input('R:')).strip().lower()
                        if voltar == 's':
                            break
                        elif voltar == 'n':
                            print('Volte sempre!')
                            Variavel_while2 = True
                            Variavel_whileql = True
                            break
                        else:
                            print('Escreva direito!')
                            Variavel_while2 = True
                            Variavel_whileql = True
                            break



        elif escolha == 3:
            Variavel_while1 = True
            break


        else:
            while True:
                print('Você não digitou um número da lista')
                print('Você precisa digitar um número que esta na lista!')
                print('Deseja voltar? (s/n)')
                voltar = str(input('R:')).strip().lower()
                if voltar == 's':
                    Variavel_while2 = True
                    break
                elif voltar == 'n':
                    print('Volte sempre!')
                    Variavel_while1 = True
                    Variavel_while2 = True
                    break
                else:
                    print('Escreva direito!')
                    Variavel_while1 = True
                    Variavel_while2 = True
                    break
        

