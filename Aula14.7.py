teste = list()

teste.append("Daniel")
teste.append(42)
galera = list()
galera.append(teste[:])
teste[0] = "Chico"
teste[1] = 6
galera.append(teste[:])
print(galera)

grupo = [["Chico",6],["Daniel",42],["Lilia",39],["Maria",14]]

print(grupo[0])

print(grupo[0][1])

print(grupo[2][1])

print(grupo[-1][0])

for p in grupo:
    print(p)

for p in grupo:
    print(f"O(A) {p[0]} possui {p[1]} anos")
    

galerinha = list()
dados = list()

"""
for c in range(0,3):
    dados.append(str(input("Nome: ")))
    dados.append(int(input("Idade: ")))
    galerinha.append(dados[:])
    dados.clear()

print(galerinha)
"""

totmai = totmen = 0

galerinha = [["Daniel",42],["Chico",6],["Lilia",39],["Maria",14]]

for p in galerinha:
    if p[1] >= 18: # [1] - verifica apenas as idades
        print(f"{p[0]} é maior de idade")
        totmai += 1
    else:
        print(f"{p[0]} é menor de idade")
        totmen += 1

print(f"Temos {totmai} maiores e {totmen} menores de idade.")
