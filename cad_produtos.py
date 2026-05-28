
produtos = []

print("--- SISTEMA DE CADASTRO ---")

while True:
    print("\n1. Cadastrar | 2. Listar | 3. Sair")
    opcao = input("Escolha: ")

    if opcao == "1":
        
        print("------------------------------------------------------------")
        codigo = input("Código: ")
        nome = input("Nome: ")
        preco = input("Preço: ")
        qtd = input("Quantidade: ")
        print("------------------------------------------------------------")

        item = f"{codigo} • {nome} • R$ {preco} • {qtd} unidades"
        produtos.append(item)
        print(" Cadastrado")

    elif opcao == "2":
        print("\n--- LISTA DE PRODUTOS ---")
        if not produtos:
            print("Nada cadastrado ainda.")
        else:
           
            for p in produtos:
                print(p)
    
    elif opcao == "3":
        print("Saindo..")
        break