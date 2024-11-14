#aqui o sistema pede o nome do usuario
nome = input("Escreva seu nome:")
#aqui o sistema pede o nome do usuario
idade = int(input("Qual a sua idade?"))
#aqui mostra o nome e idade do usuario
print(f"Bem vindo {nome}, voçê tem {idade} anos.")

#aqui é uma função chamada "menu"
def menu():
    print("Como posso ter ajudar?")
    print("1 - Bebidas")
    print("2 - Salgados")
    print("3 - Doces")
    #aqui grava a opção que o usuario decidiu
    opc_user = int(input('Digite o número da opção desejada:'))

    if opc_user == 1:
        print("Temos coca, guarana")
    elif opc_user == 2:
        print("Temos coxinha")
    elif opc_user == 3:
        print("Temos bala")
    else:
        print("Escolha um número de 1 a 3")
menu()