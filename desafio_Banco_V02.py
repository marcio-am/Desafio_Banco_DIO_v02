verificacao_cliente = """
[s] Já sou cliente
[n] Não sou cliente. Quero abrir uma conta.
[q] Sair
->"""
menu = """

[d] Depositar  [s] Sacar   [e] Extrato
[c] Quero abrir outra conta.     [q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
clientes = list()
contas = list()
numero_saques = 0
LIMITE_SAQUES = 3
conts = 1

# Definindo as funções 
def depositarFN(valor):
    saldo_deposito = saldo
    saldo_deposito += valor
    return saldo_deposito    

def sacarFN(valor_fn = "valor"):
    saldo_sacar = saldo
    saldo_sacar -= valor_fn
    return saldo_sacar

def extratoFN(valor, tipo = ""):
    if tipo == "sacar":
        extrato_func = extrato
        extrato_func += f"Saque: R$ {valor:.2f}\n" 
    elif tipo == "depositar":
        extrato_func = extrato
        extrato_func += f"Depósito: R$ {valor:.2f}\n"

    return extrato_func

def cadastroFN(cpf,nascimento,endereco):
    clientes_fn = clientes
    clientes_fn.append([cpf,nascimento,endereco])
    return clientes_fn

def contadorFN(const_fn):
     const_fn += 1
     return const_fn
     
def contasFN(conts):
     cpf_fn = input(str("Digite seu CPF sem pontos e traço (Somente números):"))
     conta_fn = contas
     conta_fn += [cpf_fn, "0001", f"{conts}"]
     conts = contadorFN(conts)
     return conta_fn, cpf_fn, conts

     
while True:
    entrada = input(verificacao_cliente)
    
    

    if entrada == "n":
                # cpf = input(str("Digite seu CPF sem pontos e traço (Somente números):"))
                contas, cpf, conts = contasFN(conts)
                nascimento = input("Digite a sua data de nascimento:")
                endereco = input(str("Digite seu endereço:"))
                clientes.append([cadastroFN(cpf,nascimento,endereco)], )
                print(f"Sua conta foi criada.")
                print(contas)
    
    if entrada == "s":
        opcao = input(menu)
        if opcao == "d":

            valor = float(input("Informe o valor do depósito: "))
                

            if valor>0:

                saldo = depositarFN(valor)
                extrato = extratoFN(valor,tipo="depositar")
                    
                print("Depósito realizado com sucesso.")

            else:
                print("Operação falhou! O valor informado é inválido.")

        elif opcao == "s":
                
            if (numero_saques < LIMITE_SAQUES) and (valor <= limite) and (valor <= saldo):
                valor = float(input("Informe o valor do saque: "))

                saldo = sacarFN(valor_fn=valor)
                extrato = extratoFN(valor,tipo="sacar")

                print("Saque efetuado com sucesso!")
                numero_saques += 1
                    
                    
            elif numero_saques >= LIMITE_SAQUES:

                print("Operação falhou! Número máximo de saques diários excedido!")
            elif valor >= saldo:
                print("Operação falhou! Seu saldo é insuficiente!")

            elif valor >= limite:
                print("Operação falhou! O valor excede o limite máximo permitido!")

            else:
                print("Operação falhou! O valor informado é inválido.")
                
                

        elif opcao == "e":
            print("\n================ EXTRATO ================")
            print("Não foram realizadas movimentações." if not extrato else extrato)
            print(f"\nSaldo: R$ {saldo:.2f}")
            print("==========================================")

        elif opcao == "c":
                contas, cpf, conts = contasFN(conts)
                print(f"Sua conta foi criada.")
                print(contas)
        
        elif opcao == "q":
             break
             
    elif entrada == "q":
        break
print(clientes)
        # else:
        #     print("Operação inválida, por favor selecione novamente a operação desejada.")
                


