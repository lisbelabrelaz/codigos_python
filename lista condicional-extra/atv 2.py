ano = int(input("Informe um ano: "))

if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0): # !=0, não é divisível
    print(f"O ano {ano} é bissexto.")
else:
    pint(f"O ano {ano} não é bissexto.")    