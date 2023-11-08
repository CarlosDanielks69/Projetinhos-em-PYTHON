import random
from os import system

lista = ["PEDRA", "PAPEL", "TESOURA"]

placar_1 = 0
placar_2 = 0

while True:
    print(f"\nO Placar está como {placar_1} para jogador e {placar_2} para maquina.")
    a = input("Pedra Papel ou Tesoura? ").upper()

    computador = random.choice(lista)

    if a not in lista:
        print("Escolha Pedra, Papel ou Tesoura.")
    elif a == computador:
        print(f"Você: {a}\nComputador: {computador}\nDRAW")
        input("Pressione enter para continar...")
        system("cls")
    elif (a == "PEDRA" and computador == "TESOURA") or \
            (a == "PAPEL" and computador == "PEDRA") or \
            (a == "TESOURA" and computador == "PAPEL"):
        print(f"Você: {a}\nComputador {computador}\nYOU WIN!")
        placar_1 = placar_1 + 1
        input("Pressione enter para continar...")
        system("cls")
    else:
        print(f"Você: {a}\nComputador {computador}\nYOU LOSE!")
        placar_2 = placar_2 + 1
        input("Pressione enter para continar...")
        system("cls")

