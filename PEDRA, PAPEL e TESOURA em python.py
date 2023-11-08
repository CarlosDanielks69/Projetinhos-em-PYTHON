import random

a = input("Pedra Papel ou Tesoura? ").upper()

lista = ["PEDRA", "PAPEL", "TESOURA"]

computador = random.choice(lista)

if a not in lista:
    print("Escolha Pedra, Papel ou Tesoura.")
elif a == computador:
    print(f"Você: {a}\nComputador: {computador}\nDRAW")
elif (a == "PEDRA" and computador == "TEROURA") or \
        (a == "PAPEL" and computador == "PEDRA") or \
        (a == "TESOURA" and computador == "PAPEL"):
    print(f"Você: {a}\nComputador {computador}\nYOU WIN!")
else:
    print(f"Você: {a}\nComputador {computador}\nYOU LOSE!")
