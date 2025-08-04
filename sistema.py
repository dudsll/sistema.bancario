menu = ''''''

[d] depositar
[s] sacar
[e] extrato
[q] sair

=> = ''

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu).strip().lower()

    if opcao == 'd':
        valor = float(input('Informe o valor do depósito: '))
        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n'
            print(f'Depósito de R$ {valor:.2f} realizado com sucesso!')
        else:
            print('Valor inválido para depósito.')

    elif opcao == 's':
        valor = float(input('Informe o valor do saque: '))
        if 0 < valor <= saldo and numero_saques < LIMITE_SAQUES:
            saldo -= valor
            extrato += f'Saque: R$ {valor:.2f}\n'
            numero_saques += 1
            print(f'Saque de R$ {valor:.2f} realizado com sucesso!')
        else:
            print('Saque inválido. Verifique o valor ou limite de saques.')

    elif opcao == 'e':
        print('Extrato:')
        print(extrato if extrato else 'Nenhuma transação realizada.')
        print(f'Saldo atual: R$ {saldo:.2f}')

    elif opcao == 'q':
        print('Saindo do sistema...')
        break

    else:
        print('Opção inválida. Tente novamente.')