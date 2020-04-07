"""
Tuplas <- 
Listas 
Dicionários
"""

lanche = ('Hamburguer','Suco','Pizza','Pudim')

print(f"{lanche[0]}")

print(f"{lanche[0:2]}")

print(f"{lanche[1:]}")

print(f"{lanche[-1]}")

print(f"{lanche[-2]}")

print (f"{len(lanche)}")

print("\n")

for c in lanche:
    print(f"{c}")

for c in range (0,len(lanche)):
    print(f"{c}")
    
for pos, c in enumerate(lanche):
    print(f"{c} posição {pos}")
    
print(sorted(lanche))

