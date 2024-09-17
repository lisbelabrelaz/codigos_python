
# Solicitar 10 números inteiros ao usuário
for i in range(10):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    lista_usuario.append(numero)

# Verificando as posições onde o número 3 aparece
posicoes_usuario = [i for i, num in range(lista_usuario) if num == 3]

print("Lista:", lista_usuario)
print("Posições do número 3:", posicoes_usuario)



