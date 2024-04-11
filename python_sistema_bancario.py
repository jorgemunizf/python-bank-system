menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input('Informe o valor do depósito: '))

        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n'
            print('Depósito realizado com sucesso!')

        else:
            print('Operação cancelada! O valor informado é inválido.')

    elif opcao == "s":
        valor = float(input('Informe o valor do saque: '))

        if valor > saldo:
            print('Operação cancelada! Saldo insuficiente.')
        elif valor > limite:
            print('Operação cancelada! Limite de saque exedido.')
        elif numero_saques >= LIMITE_SAQUES:
            print('Operação cancelada! Limite de saque exedido.')
        elif valor > 0:
            saldo -= valor
            extrato += f'Saque: R$ {valor:.2f}\n'
            numero_saques += 1
            print('Saque realizado com sucesso!')
        else:
            print('Operação cancelada! Valor informado inválido.')

    elif opcao == "e":
        print('\n====================EXTRATO====================')
        print('Não foram realizadas movimentações na conta.' if not extrato else extrato)
        print(f'\nSaldo: R$ {saldo:.2f}')
        print('=================================================')
    elif opcao == "q":
        break



    else:
        print("Operação inválida, por favor selecione novamente a opção desejada.")