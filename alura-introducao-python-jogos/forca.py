import random

def jogar(nome=''):
    imprimir_cabecalho(nome)
    palavra_secreta = carregar_palavra_secreta()
    letras_certas = inicializar_letras_acertadas(palavra_secreta)

    enforcou = False
    acertou = False
    limite_de_erros = 7
    erros_cometidos = 0

    print(" ".join(letras_certas))

    while not enforcou and not acertou:
        chute = obter_chute()

        if chute in palavra_secreta:
            preencher_chute_correto(chute, palavra_secreta, letras_certas)
        else:
            erros_cometidos += 1
            mostrar_erro_ao_chute(erros_cometidos, limite_de_erros)

        enforcou = erros_cometidos >= 7
        acertou = "_" not in letras_certas

        imprimir_letras_certas(letras_certas)

    if acertou:
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)

def imprimir_cabecalho(nome):
    print("**************************************")
    print(" Olá {0}, bem vindo ao jogo de forca! ".format(nome))
    print("**************************************")

def carregar_palavra_secreta():
    with open("palavras.txt", "r") as arquivo:
        palavras = [palavra.strip().upper() for palavra in arquivo]
    return palavras[random.randrange(0, len(palavras))]

def inicializar_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def obter_chute():
    chute = input("Escolha uma letra: ")
    return chute.strip().upper()

def preencher_chute_correto(chute, palavra_secreta, letras_certas):
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_certas[index] = letra
        index += 1

def mostrar_erro_ao_chute(erros_cometidos, limite_de_erros):
    if erros_cometidos < limite_de_erros:
        desenha_forca(erros_cometidos)
        print("Ops, você errou! Faltam {} tentativas".format(limite_de_erros - erros_cometidos))

def imprimir_letras_certas(letras_certas):
    print(" ".join(letras_certas))

def imprime_mensagem_perdedor(palavra_secreta):
    print("")
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def imprime_mensagem_vencedor():
    print("")
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if __name__ == "__main__":
    jogar()