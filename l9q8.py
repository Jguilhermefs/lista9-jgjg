nomes = []
for i in range(5):
    nome = input(f"Digite o {i+1}º nome: ")
    nomes.append(nome)
contador = 0
for nome in nomes:
    if nome[0].upper() == 'A':
        contador += 1
print(f"Quantidade de nomes que começam com a letra 'A': {contador}")
