#Solicita o nome da fazenda ao usuário
nome_fazenda = input("Informe o nome da fazenda")
#Solicita a quantidade de cavalos ao usuário
quantidade_cavalos = int(input("Informe a quantidade de cavalos ao usuário {nome_fazenda}"))
#Calcule a quantidade de ferraduras necessárias (4 por cavalo)
quantidade_ferraduras = quantidade_cavalos * 4


#Exibe o resultado 
print(f"A fazenda {nome_fazenda} possui {quantidade_cavalos} cavalos.")  
print(f"A quantidade total de ferraduras para equipar todos os cavalos é {quantidade_ferraduras}.")