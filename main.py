#import's
from calculadora import calculadora_main


#Programa principal
Variavel_while1 = False

while Variavel_while1 == False:
    print('-=' * 25)
    print(' ' * 10, 'Bem vindo ao painel da Takern')
    print('-=' * 25)
    print('Você deseja:')
    print('[1] Calculadora')
    print('[2] Fazer exercicios')
    print('[3] Fechar o programa')

    escolha = str(input(''))
    escolha = escolha.replace('', ' ').strip()


    #verificar se o numero não é numerico
    if escolha.isalpha():
        print('Você não digitou um número')
        print('Você precisa digitar um número!')
        print('Esse numero não existe deseja voltar? (s/n)')
        voltar = input('').upper()
        voltar = voltar.replace('', ' ') 
        if voltar == 'S':
            continue
        elif voltar == 'N':
            print('Volte sempre!')
            break
        
        
        
    escolha = int(escolha) #Transformo a escolha que esta em string para numero inteiro

    
    if escolha == 3:
        break

    #verificação de qual numero foi escolhido
    while True:
        if escolha == 1:
            print('[1]Adição')
            print('[2]Subtração')
            print('[3]Divisão')
            print('[4]Mutiplicação')
            print('[5]Raiz quadrada')
            print('[6]Potenciação')
            escolha2 = input('')
            if escolha2 == '1':
                calculadora_main.contademais()

            elif escolha2 == '2':
                calculadora_main.contademenos()

            elif escolha2 == '3':
                calculadora_main.contadedividir()

            elif escolha2 == '4':
                calculadora_main.contademutiplicação() 

            elif escolha2 == '5':
                calculadora_main.contaderaiz()
                
            elif escolha2 == '6':
                calculadora_main.contadepotenciação() 

        elif escolha == 2:
            pass

        else:
            print('Você não digitou um número da lista')
            print('Você precisa digitar um número que esta na lista!')
            print('Deseja voltar? (s/n)')
            voltar = str(input('')).strip().lower().replace('', ' ') 
            if voltar == 's':
                pass
            elif voltar == 'n':
                print('Volte sempre!')
                Variavel_while1 = True
            else:
                print('Escreva direito!')
                Variavel_while1 = True

        
        
