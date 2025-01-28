def calculadora_desconto():
    valor=float(input('Digite o valor do produto: '))
    desconto=float(input('Digite o desconto (%): '))
    preco_final = valor-(valor*desconto/100)
    print('Seu valor final com desconto será de: R$', preco_final)

calculadora_desconto()