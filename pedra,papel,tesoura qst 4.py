import random

def jogar():
    opcoes = ["Pedra", "Papel", "Tesoura"]
    
    while True:
        usuario = int(input("\nEscolha (1: Pedra, 2: Papel, 3: Tesoura): ")) - 1
        if usuario not in [0, 1, 2]:
            print("Escolha inválida.")
            continue
        
        computador = random.randint(0, 2)
        print(f"Computador escolheu: {opcoes[computador]}")
        
        if usuario == computador:
            print("Empate!")
        elif (usuario == 0 and computador == 2) or (usuario == 1 and computador == 0) or (usuario == 2 and computador == 1):
            print("Você ganhou!")
        else:
            print("Você perdeu!")
        
        jogar_novamente = input("Jogar novamente? (s/n): ")
        if jogar_novamente != 's':
            break

if __name__ == "__main__":
    jogar()

