'''Construção de um sistema bancário. Desafio de projeto da dio.me'''

menu = """
[d] Deposito
[s] Saldo
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
num_saque = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou !    O valor informado é inválido.")
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saque = num_saque >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou ! você não tem limete suficiênte.")

        elif excedeu_limite:
            print("Operação falhou ! O valor do saque excedeu o limite.")
            
        elif excedeu_saque:
            print("Operação falhou ! Número máximo de saques excedeu.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"

        else:
            print("Operação falhou ! O valor informado é inválido.")

    elif opcao == "e":
        print("\n*********EXTRATO*********")
        print("Não foram realizados movimentações." if not extrato else extrato)  
        print(f"\nSaldo: R$ {saldo:.2f}")
        print(("**********************************"))

    elif opcao == "q":
        break

    else: 
        print("Operação inválida, por favor selecione novamente a operação desejada.")    



