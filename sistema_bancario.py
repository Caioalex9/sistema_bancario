"""
Crie um sistema bancario com as operações: saque , deposito e visualizar extrato
1 - Depositar valores positivos 
2 - Trabalhar com apenas 1 usuario
3 - Dados devem ser armazenados e exibidos no extrato
4 - Limite de saque diario de 3 com maximo 500
"""
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
        valor = float(input("Informe o valor do depósito: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor: }\n"
            
        else:
            print("Operação falhou! O valor informao é inválido, Por favor insira um valor valido.")
            
    elif opcao == "s":
        valor = float(input("Informe um valor do saque: "))
        
        excedeu_saldo = valor > saldo
        
        excedeu_limite = valor > limite
        
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print("Operação Falhou ! Você não tem saldo suficiente. Por favor insira um valor valido.")
            
        elif excedeu_limite:
            print("Operação falhou ! o valor do saque excede o limite. Por favor insira um valor valido.")
        
        elif excedeu_saques:
            print("Operação falhou ! Número máximo de saques excedido. Aguarde 24 horas para nova realização.")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor: }\n"
            numero_saques += 1
            
        else:
            print("Operação falhou ! O valor informado é inválido. Por favor insira um valor valido.")
        
    elif opcao == "e":
        print("\n ========== EXTRATO ==========")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo: }")
        print("================================")
        
    elif opcao == "q":
        break
    
    else:
        print("Operação invalida, por favor selecione novamente a operação desejada.")