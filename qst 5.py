# Inicializando a lista para armazenar os números
lista_numeros = []

# Solicitando ao usuário que insira 5 números
for i in range(5):
    numero = int(input(f"Digite o {i+1}º número: "))
    lista_numeros.append(numero)

# Filtrando os números que são divisíveis por 3
divisiveis_por_3_usuario = [num for num in lista_numeros if num % 3 == 0]

# Exibindo a lista completa e os números divisíveis por 3
print("Lista completa:", lista_numeros)
print("Números divisíveis por 3:", divisiveis_por_3_usuario)



