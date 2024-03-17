# Menu de opções para o usuário
menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """

# Variáveis de estado da conta
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 2

# Loop principal da aplicação
while True:
    # Exibir o menu e solicitar uma opção ao usuário
    opcao = input(menu)

    # Opção para depositar dinheiro na conta
    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n'
        else:
            print("Operação falhou! O valor informado é inválido. Tente novamente!")

    # Opção para sacar dinheiro da conta
    elif opcao == 's':
        valor = float(input("Informe o valor do saque: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não possui saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excedeu o limite.")
        elif excedeu_saques:
            print("Operação falhou! Número de saques foi excedido.")
        elif valor > 0:
            saldo -= valor
            extrato += f'Saque: R$ {valor:.2f}\n'
            numero_saques += 1
        else:
            print("Operação falhou! O valor informado é inválido.")

    # Opção para exibir o extrato da conta
    elif opcao == "e":
        print("\n============= EXTRATO =============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===================================")

    # Opção para sair do programa
    elif opcao == "q":
        break
    # Caso a opção selecionada não seja válida
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
