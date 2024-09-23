def main():
    print("Bem-vindo ao calculador de calorias queimadas!")

    atividade = input("Digite o tipo de atividade (caminhada, corrida ou ciclismo): ").lower()
    tempo = int(input("Digite o tempo em minutos: "))

    if atividade == "caminhada":
        calorias = 5 * tempo
    elif atividade == "corrida":
        calorias = 10 * tempo
    elif atividade == "ciclismo":
        calorias = 8 * tempo
    else:
        print("Atividade inválida.")
        return

    print(f"Você queimou {calorias} calorias fazendo {atividade} por {tempo} minutos.")

if __name__ == "__main__":
    main()
