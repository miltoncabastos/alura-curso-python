import forca
import adivinhacao

print("**************************************")
print("** Bem vindo ao programa de jogos! **")
print("**************************************")

nome = input("Primeiro, digite o seu nome: ")

print("Agora escolha o seu jogo")
print("(1) Jogo de Adivinhação")
print("(2) Jogo da Força")
jogo = int(input("Escolha o jogo: "))

if(jogo == 1):
    print("Jogando Adivinhação")
    adivinhacao.jogar(nome)
elif(jogo == 2):
    print("Jogando Forca")
    forca.jogar(nome)

print()
print("Fim do jogo")