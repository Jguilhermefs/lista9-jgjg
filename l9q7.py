def validar_cpf(cpf):
    if len(cpf) == 11 and cpf.isdigit():
        print("CPF válido")
    else:
        print("CPF inválido")
cpf = input("Digite o CPF (apenas números): ")
validar_cpf(cpf)
