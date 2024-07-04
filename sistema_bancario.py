"""
Crie um sistema bancario com as operações: saque , deposito e visualizar extrato
1 - Depositar valores positivos 
2 - Trabalhar com apenas 1 usuario
3 - Dados devem ser armazenados e exibidos no extrato
4 - Limite de saque diario de 3 com maximo 500
"""

def menu():
    menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Nova Conta
    [nu] Novo Usuário
    [q] Sair
    
    => """
    return input(menu)

def depositar (saldo, valor, extrato,/):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R${valor:.2f}\n"
    else:
        print("\nOperação falhou ! O valor informado é inválido, Por favor insira um valor valido")
    return saldo,extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques
    
    if excedeu_saldo:
        print("\nOperação falhou ! O valor informado é inválido, Por favor insira um valor valido")
    
    elif excedeu_limite:
        print("\nOperação falhou ! O valor informado é inválido, Por favor insira um valor valido")
    
    elif excedeu_saques:
        print("\nOperação falhou ! O valor informado é inválido, Por favor insira um valor valido")
    
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("\n Saque realizado com sucesso !")
    
    else:
        print("\nOperação falhou ! O valor informado é inválido, Por favor insira um valor valido")
    
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n===== EXTRATO =====")
    print("Não foram realizadas as movvimentações." if not extrato else extrato)
    print(f"\nSaldo: R${saldo:.2f}")
    print("=====================")
    
def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("\n Já existe usuário com esse CPF ! Por favor insira um valido")
        return

    nome = input ("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento(dd-mm-aaaa): ")
    endereco = input ("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    
    print("Usuário criado com sucesso ! Seja muito bem vindo(a)!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("\n Conta criada com sucesso ! Seja muito bem vindo(a)!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\n Usuario não encontrado, criação de conta encerrado! Por favor insira um usuario valido!")
    
def main():
    AGENCIA = "0001"
    LIMITE_SAQUES = 3
    
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    
    

    while True:
        opcao = menu()
        
        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
        
            saldo, extrato = depositar(saldo, valor, extrato)
        
                
        elif opcao == "s":
            valor = float(input("Informe um valor do saque: "))

            saldo, extrato = sacar (
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )
        

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
        
        elif opcao == "nu":
            criar_usuario(usuarios)
        
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            
            if conta:
                contas.append(conta)
            
        elif opcao == "q":
            break
    
        else:
            print("Operação invalida, por favor selecione novamente a operação desejada.")
            
main()