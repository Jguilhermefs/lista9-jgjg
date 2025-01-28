def conversor_de_moeda():
    reais = float(input("Digite o valor em reais: R$ "))
    cotacao_dolar = float(input("Digite a cotação do dólar: "))
    dolares = reais / cotacao_dolar
    print(f"Você pode comprar ", dolares, 'dólares')

conversor_de_moeda()
