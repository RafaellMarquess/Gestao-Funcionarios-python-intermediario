nomes = []
salarios = []
pessoas = []
cargos = []

print("\nBem-vindo ao gestor de funcionários")
print("\nO que deseja fazer?\n\n1 - Excluir funcionário\n2 - Adicionar funcionário\n3 - Listar funcionários\n4 - Sair")

while True:
    resposta = input("")

    if resposta == "1":
        if len(nomes) == 0:
            print("Ninguém cadastrado.")
        else:
            excluir = int(input("Digite o número do funcionário para excluir (0, 1, 2...): "))
            if excluir < len(nomes):
                removido = nomes.pop(excluir)
                cargos.pop(excluir)
                salarios.pop(excluir)
                print(f"{removido} foi removido com sucesso.")
            else:
                print("Erro.")

    elif resposta == "2":
        nome_novo = input("Nome do novo funcionário: ")
        cargo_novo = input("Cargo do novo funcionário: ")
        salario_novo = input("Salário do novo funcionário: ")
        nomes.append(nome_novo)
        cargos.append(cargo_novo)
        salarios.append(salario_novo)
        print(f"{nome_novo} adicionado com sucesso.")

    elif resposta == "3":
        if len(nomes) == 0:
            print("Não há ninguém cadastrado.")
        else:
            for i in range(len(nomes)):
                print(f"Nome: {nomes[i]} | Cargo: {cargos[i]} | Salário: {salarios[i]}")

    elif resposta == "4":
        print("Saindo...")
        exit()

    else:
        print("Erro de digitação.")

    print("\nO que deseja fazer?\n1 - Excluir funcionário\n2 - Adicionar funcionário\n3 - Listar funcionários\n4 - Sair")
