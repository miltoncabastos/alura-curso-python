import random

def jogar(nome=''):
    print("**************************************")
    print("Olá {0}, bem vindo ao jogo de adivinhação!".format(nome))
    print("**************************************")

    print("Primeiro, escolha a dificuldade")
    print("(1) Fácil, (2) Médio, (3) Difícil")
    nivel = int(input("Escolha o nível: "))

    total_de_tentativas_possiveis = 0
    if(nivel == 1): total_de_tentativas_possiveis = 20
    elif(nivel == 2): total_de_tentativas_possiveis = 10
    else: total_de_tentativas_possiveis = 5

    pontos = 1000

    numero_secreto = random.randint(1, 100)
    rodada = 1

    for rodada in range(1, total_de_tentativas_possiveis + 1):
        print()
        print("Tentativa {} de {} tentativas".format(rodada, total_de_tentativas_possiveis))
        chute_str = input("Digite o seu número entre 1 e 100: ")
        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 10!")
            continue

        chute_correto = chute == numero_secreto
        chute_foi_maior = chute > numero_secreto
        chute_foi_menor = chute < numero_secreto

        if (chute_correto):
            print("você acertou!")
            break
        else:
            pontos_perdidos = abs(numero_secreto - chute)
            pontos -= pontos_perdidos
            if (chute_foi_maior):
                print("você errou! o seu chute foi maior que o número secreto")
            elif (chute_foi_menor):
                print("você errou! o seu chute foi menor que o número secreto")

    print()
    print("Você fez {} pontos".format(pontos))
    print()
    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()