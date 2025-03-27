menu = '''
\nBem vindo ao Banco do Python!\n
Selecione uma opção:\n
[d] Depositar
[s] Sacar 
[e] Extrato
[q] Sair 

=> '''

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)
    
    if opcao == 'd':
        print('\nDeposito\n')
        valor = float(input('\nQual valor você deseja depositar? R$:'))
        
        if valor > 0:
            saldo += valor
            extrato += f'Depósito de R$ {valor:.2f}\n'
        else:
            print('Valor inserido inválido. Tente novamente.')
        
    elif opcao == 's':
        print('\nSaque\n')
        saque = float(input('\nQual valor você deseja sacar? R$:'))
        
        saldo_excedido = saque > saldo
        
        limite_excedido = saque > limite
        
        saque_excedido = numero_saques >= LIMITE_SAQUES
        
        if saque_excedido:
            print(f'\nVocê excedeu o limite de saques diários.\nConsulte seu extrato.\nTente novamente amanhã.')
        
        elif limite_excedido:
            print(f'\nVocê excedeu o limite de saque diário.\nLimite disponível para saque: R$', limite)
       
        elif saldo_excedido:
            print('\nVocê não tem saldo suficiente, realize um depósito para validar a operação.')
        
        elif saque > 0:
            saldo -= saque
            limite -= saque
            extrato += f'Saque de: R$ {saque:.2f}\n'
            numero_saques += 1
       
        else:
            print('Valor inserido inválido. Tente novamente.')
    
    elif opcao == 'e':
        print('\nExtrato\n')
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'Saldo: R$ {saldo:.2f}')
        print(f'Saques disponíveis hoje: {LIMITE_SAQUES - numero_saques}')
        print(f'Limite de saque diário: R$ {limite}')
    
    elif opcao == 'q':
        break
    
    else:
        print('Opção invalida, por favor selecione uma opção válida')