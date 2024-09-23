import time

# Solicita o número de segundos para a contagem regressiva
segundos = int(input("Digite o número de segundos: "))

# Realiza a contagem regressiva
for i in range(segundos, 0, -1):
    print(i)
    time.sleep(1)  # Pausa de 1 segundo

# Mensagem ao final da contagem
print("Tempo esgotado!")