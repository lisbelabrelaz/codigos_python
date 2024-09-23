# Solicita o valor da conta e o percentual da gorjeta
valor_conta = float(input("Valor da conta: R$ "))
percentual_gorjeta = float(input("Percentual de gorjeta (ex: 10, 15 ou 20): "))

# Calcula a gorjeta e o total
gorjeta = valor_conta * (percentual_gorjeta / 100)
total = valor_conta + gorjeta

# Exibe os resultados
print(f"Gorjeta: R$ {gorjeta:.2f}")
print(f"Total: R$ {total:.2f}")



