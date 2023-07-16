menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

Saldo = 0
Sacar = 500
Extrato = ""
Numero_saques = 0
Limite_saques = 3

while True:

    opcao = input(menu)
    
    if opcao == "d":
        valor = float(input("Quanto você quer depositar?: "))

        if valor > 0:
            Saldo += valor
            Extrato += f"Depósito: R$ {valor:.2f}\n"
        
        else:
            print("Ops! a operação falhou. O valor informado não é válido.")
    
    elif opcao == "s":
        valor = float(input("Quanto você quer sacar? "))
        
        excedeu_saldo = valor > Saldo
        excedeu_limite = Numero_saques >= Limite_saques

        if excedeu_saldo:
            print("Ops! você não tem saldo suficiente.")
        
        elif excedeu_limite:
            print("Ops! O valor do saque é maior que o limite.")
            
        elif valor > 0:  
            Saldo -= valor
            Extrato += f"Saque: R$ {valor:.2f}\n"
            Numero_saques += 1
        
        else:
            print("Ops! O valor informado não é válido.")

    elif opcao == "e":
        print("\n=====================EXTRATO=====================")
        print("Não foram realizadas movimentações." if not Extrato else Extrato)
        print(f"\nsaldo: R$ {Saldo:.2f}")
        print("===================================================")
    
    elif opcao == "q":
        break

    else:
        print("Ops! A operação não é válida. Selecione novamente a operação desejada.")
