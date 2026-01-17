funcionarios = [
    {"nome": "Rafael", "cargo": "Desenvolvedor Frontend", "salario": 6000.0},
    {"nome": "Ana", "cargo": "Designer UX", "salario": 5200.0},
    {"nome": "Pedro", "cargo": "Gerente de TI", "salario": 8500.0},
    {"nome": "Maria", "cargo": "Desenvolvedora Frontend", "salario": 5800.0},
    {"nome": "Lucas", "cargo": "Estagiário", "salario": 1800.0},
    {"nome": "Carla", "cargo": "Analista de Dados", "salario": 6200.0},
    {"nome": "Bruno", "cargo": "Desenvolvedor Mobile", "salario": 5900.0},
    {"nome": "Beatriz", "cargo": "Product Owner", "salario": 7500.0},
    {"nome": "Ricardo", "cargo": "Suporte Técnico", "salario": 3200.0},
    {"nome": "Julia", "cargo": "Recursos Humanos", "salario": 4500.0}
]

while True:
    print("buscar funcionario:")
    buscar = input("")  
    encontrado = False
    for n in funcionarios:
        if buscar == n["nome"].lower():
            print(f"Nome: {n['nome']} | Cargo: {n['cargo']} | Salário: R$ {n['salario']:.2f}")
            encontrado = True
            break
    else:
        print("nao")