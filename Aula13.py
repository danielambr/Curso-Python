c = 0

while c < 10:
    print(f"{c}")
    c += 1

print("\n\n")

p = 0
   
while p != 10:
    print(f"{p}")
    p += 1
    
print("\n\n")

r = "S"

while r == "S":
    g = int(input("Informe um valor "))
    r = str(input("Quer continuar [S|N]: ")).upper()
print("FIM")

x = b = 0

while True:
    i = int(input("Informe um número: "))
    b += i
    if i == 999:
        break
print(f"O somatório dos numeros é igual a {b}")