#lista and variaveis
lista_numero = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)



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
            pass

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

        
        
