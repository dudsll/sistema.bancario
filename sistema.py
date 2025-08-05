import textwrap


def menu():
    menu_text = """
    ==================== MENU ====================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário 
    [q]\tSair
    => """
    return input(textwrap.dedent(menu_text))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f'Depósito: R$ {valor:.2f}\n'
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print('Valor inválido para depósito.')
    return saldo, extrato

def sacar(saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print('\n Operação falhou! Você não tem saldo suficiente.')

    elif excedeu_limite:
        print('\n Operação falhou! O valor do saque excede o limite.')

    elif excedeu_saques:
        print('\n Operação falhou! Número máximo de saques excedido.')
    
    elif valor > 0:
        saldo -= valor
        extrato += f'Saque: R$ {valor:.2f}\n'
        numero_saques += 1
        print('\n=== Saque realizado com sucesso! ===')
    else:
        print('Valor inválido para saque.')
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print('\n=================== EXTRATO ===================')
    print('Não foram realizadas movimentações.' if not extrato else extrato)
    print(f'\nSaldo: R$ {saldo:.2f}')
    print('=================================================')

def criar_usuario(usuarios):
    cpf = input('Informe o CPF (somente números): ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('Já existe um usuário cadastrado com esse CPF.')
        return
    
    nome = input('Informe o nome completo: ')
    data_nascimento = input('Informe a data de nascimento (DD/MM/AAAA): ')
    endereco = input('Informe o endereço (logradouro, número - bairro - cidade/UF):')

    usuarios.append({
        'nome': nome,
        'data_nascimento': data_nascimento,
        'cpf': cpf,
        'endereco': endereco
    })

    print("=== Usuário cadastrado com sucesso! ===")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None   

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('Informe o CPF do usuário: ')
    usuario = next((usuario for usuario in usuarios if usuario['cpf'] == cpf), None)

    if not usuario:
        print('Usuário não encontrado. Cadastro de conta não realizado.')
        return None

    conta = {
        'agencia': agencia,
        'numero_conta': numero_conta,
        'usuario': usuario
    }
    return conta

def listar_contas(contas):
    print('\n=================== CONTAS ===================')
    if not contas:
        print('Nenhuma conta cadastrada.')
    else:
        for conta in contas:
            usuario = conta['usuario']
            print(f"Agência: {conta['agencia']} | Conta: {conta['numero_conta']} | Titular: {usuario['nome']} | CPF: {usuario['cpf']}")
    print('==============================================')

def main():
    LIMITE_SAQUES = 3
    AGENCIA = '0001'

    saldo = 0
    limite = 500
    extrato = ''
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opção = menu()

        if opcao == 'd':
         valor = float(input('Informe o valor do depósito: '))

         saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == 's':
            valor = float(input('Informe o valor do saque: '))

            saldo, extrato = sacar(
               saldo=saldo,
               valor=valor,
               extrato=extrato,
               limite=limite,
               numero_saques=numero_saques,
               limite_saques=LIMITE_SAQUES
            )

        elif opcao == 'e':
         exibir_extrato(saldo, extrato=extrato)
    
        elif opcao == 'nu':
         criar_usuario(usuarios)

        elif opcao == 'nc':
         numero_conta = len(contas) + 1

        elif opcao == 'lc':
         listar_contas(contas)

        elif opcao == 'q':
         print('Saindo do sistema...')
        break

    else:
        print('Opção inválida. Tente novamente.')
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