import random

def jogo_adivinhacao():
    numero = random.randint(1, 100)
    while True:
        palpite = int(input("Advinhe o número (entre 1 e 100): "))
        if palpite < numero:
            print("Muito baixo!")
        elif palpite > numero:
            print("Muito alto!")
        else:
            print("Parabéns! Você acertou!")
            break

jogo_adivinhacao()
