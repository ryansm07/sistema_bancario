# Trabalha com somente um usuário

# Operação de depósito
# Valores positivos para conta bancária
# Todos os depósitos devem ser armazenados para o extrato

# Operação de saque
# Permite somente 3 saques diários com limite de 500 reais cada
# Deve aparecer uma mensagem caso não tenha saldo em conta#
# Ttodos os saques devem ser armazenados para o extrato

# Operação de extrato
# Todas as operações de saques e depositos devem estar listados 
# Exibir o saldo da conta no final

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3
numero_operacao = 0


while True:

    print ("Favor escolher qual atividade bancária a ser feita")
    print ("[1] - Depósito")
    print ("[2] - Saque")
    print ("[3] - Extrato")
    print ("[4] - Sair")
    opcao = input("Ação: ")
    print ("\n")
    
    if opcao == "1":
        processo_depositoPositivo = 0
        while processo_depositoPositivo == 0:
            valor_deposito = int(input("Inserir o valor a ser depositado: "))
            if valor_deposito <= 0:
                print("O valor do deposito não pode ser negativo ou zero\n")
            else:
                 processo_depositoPositivo = 1
        
        print ("O deposito no valor de R$ ", valor_deposito, " foi efetivado com sucesso")
        saldo = saldo + valor_deposito
        print ("Saldo total: R$ ", saldo, " \n")
        numero_operacao += 1
        extrato = extrato + "Número da operação: º" + str(numero_operacao) + "\nTipo de operação: Depósito.\nValor do Depósito: R$ " + str(valor_deposito) + " \n---------------------------\n" 
    
    elif opcao == "2":
        if numero_saques == limite_saques:
            print("Já atingiu o limite de saques diário\n")
        else:
            processo_saquePositivo = 0
            while processo_saquePositivo == 0:
                valor_saque = int(input("Inserir o valor a ser sacado: "))
                if valor_saque <= 0:
                    print("O valor do saque não pode ser negativo ou zero\n")
                else:
                    processo_saquePositivo = 1
            
            if valor_saque >= 0  and valor_saque > saldo:
                print("O valor a ser sacado é maior que o saldo da conta\n")
            elif valor_saque >= 0 and valor_saque < saldo and valor_saque > limite:
                print("O valor a ser sacado é maior que o limite estabelecido do saque de R$ ", limite_saques,"\n")
            else:
                print ("O saque no valor de R$ ", valor_saque, " foi efetivado com sucesso")
                saldo = saldo - valor_saque
                print ("Saldo total: R$ ", saldo, " \n")
                numero_saques += 1
                numero_operacao += 1
                extrato = extrato + "Número da operação: º" + str(numero_operacao) + "\nTipo de operação: Saque.\nValor do Saque: R$ " + str(valor_saque) + " \n---------------------------\n" 
    

    elif opcao == "3":
        print(extrato)
        print("Saldo total: R$ ", saldo, "\n")
        

    elif opcao == "4":
        break

    else:
        print ("Operação invalida\n")
