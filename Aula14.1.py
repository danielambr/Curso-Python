a = (2,4,6,8)
b = (3,5,7,9)
c = a + b
d = b + a
f = c + d

print(f"C = {c} \n")
print(f"D = {d} \n")

print(f"C ordenado = {sorted(c)}")

print(f"{f.count(2)}")

print(f"{a.index(2)}")

del(f)
print(f"{f}")
