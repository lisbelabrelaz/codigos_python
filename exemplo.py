itens = []

while True:
    valor = int(input("Informe um valor numérico: "))
    if valor == 0:
        break
    else:
        itens.append(valor)
    print(itens)

    soma = 0
    for contador in itens:
        soma = soma + contador
        if contador == 3:
            itens.remove(contador)
    print(itens)