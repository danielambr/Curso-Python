"""
Listas parte 2
"""

dados = list()

dados.append("Hamburguer")

print(f"{dados}")

dados.append("Suco")

print(f"{dados}")

print(f"{dados[1]}")

lanches = list()

lanches.append(dados[:])

lanches.append(["Pizza","Refrigerante"])

lanches.append(["Pudim","Água"])

print(f"{lanches}")

print(f"{lanches[0][1]}")


