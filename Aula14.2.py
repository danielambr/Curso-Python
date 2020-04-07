"""
Listas
"""

lanche = ["Hamburguer","Suco","Pizza","Pudim"]

lanche.append("Cookie") # Append adiciona no final

print(f"{lanche}")

lanche.insert(0,"Hot dog")

print(f"{lanche}")

print(f"{len(lanche)}")

pedido = lanche.copy()  # Ou fazendo a atribuição direta pedido = lanche[:]

print(f"Pedido = {pedido}")

for v in enumerate(pedido):
    print(f"{v}")

del lanche[0]

print(f"{lanche}")

lanche.pop(4)

print(f"{lanche}")

lanche.remove('Pudim')

print(f"{lanche}")

lanche.insert(3,'Pudim')

print(f"{lanche}")

if "Hod dog" in lanche:
    lanche.remove("Hot dog")
else:
    print("Hot dog não está entre nós!")

valores = [10,9,6,4,3,1,5,7,2,8]

print(f"{valores}")

valores.sort()

print(f"{valores}")

valores.sort(reverse=True)

print(f"{valores}")

print(f"{len(valores)}")

# Exemplo atribuição lista
a = [2,3,4,5]
b = a[:]    
b[2] = 8
print(f"{a}")
print("\n")
print(f"{b}")
