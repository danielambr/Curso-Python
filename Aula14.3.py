"""
Import

math e random
"""

"""
funções internas
Exemplos: print, input e len
"""

"""
Funções externas
Exemplo:
import math
"""
import math
print(math.sqrt(9))

valor = float(input("Insira um valor"))

print(math.ceil(valor)) # ceil arredonda para cima

print(math.trunc(valor)) # trunc arredonda para baixo


"""
Importar função específica
"""

from math import factorial

val = int(input("Insira um valor"))

print(f"O fatorial de {val} é igual a {factorial(val)}")



