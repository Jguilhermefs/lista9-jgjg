def analise_pares_impares():
    pares = 0
    impares = 0
    for i in range(10):
        numero = int(input("Digite o primeiro número: "))
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
    print("Quantidade de números pares: ", pares)
    print("Quantidade de números ímpares: ", impares)

analise_pares_impares()