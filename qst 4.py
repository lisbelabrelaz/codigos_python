total_compra = 0.0

# Recebe os preços das mercadorias
while True:
    preco = float(input("Digite o preço da mercadoria (ou 0 para finalizar): "))
    
    if preco == 0:
        break
    elif preco < 0:
        print("Preço inválido. Por favor, insira um valor positivo.")
    else:
        total_compra += preco

# Exibe o total da compra
print(f"Total da compra: R$ {total_compra:.2f}")

# Recebe o valor pago pelo cliente
while True:
    valor_pago = float(input("Digite o valor em dinheiro que o cliente irá usar para pagar: "))
    
    if valor_pago < total_compra:
        print("Valor pago é menor que o total da compra. Por favor, insira um valor suficiente.")
    else:
        break

# Calcula e exibe o troco
troco = valor_pago - total_compra
print(f"Troco a ser devolvido: R$ {troco:.2f}")

