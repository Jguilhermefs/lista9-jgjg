def contar_vogais():
    frase=input('Digite uma frase: ').lower()
    contador=sum(1 for char in frase if char in 'aeiou')
    print('Quantidade de vogais: ', contador)

contar_vogais()
