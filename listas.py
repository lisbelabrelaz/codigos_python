animais = ["Cachorro","Gato","Ovelha"]
print(type(animais))#exibindo o tipo da variável

print(animais)

#Exibindo todos os itens da lista
print("-"*50)
for itens in animais:
    print(itens)

#1º Etapa: Atualizar dados
print("-"*50)
animais[0] = "Coelho"
print(animais)

#2 Etapa: Inserir dados
print("-"*50)
#Forma 1 - Usando append
animais.append("Cavalo")#Irá inserir um novo item no final da lista
print(animais)

#2° Forma - Usando Insert
animais.insert(1, "Pássaro")# O insert precisa de 2 valores, o 1° será o índice que deseja inserir o valor. O 2º é o conteúdo que quero inserir na lista
print(animais)

#3º Etapa: Excluir dados
print("-"*50)
#Forma 1 - usando pop()
animais.pop()#Remove o último item da lista
print(animais)

#Forma 2 - Usando pop() com índice
animais.pop(0)# Aqui iremos escolher qual índice da lista será excluído
print(animais)

#Forma 3 - Usando remove
animais.remove("Ovelha")
print.animais