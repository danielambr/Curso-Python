#nome = str(input("Insira o seu nome: ")).strip()

#print(f"O nome {nome} possui {len(nome) - nome.count(' ')} letras") #A função 'len' retorna a contagem das letras


nome2 = "Daniel"

print(nome2.islower()) # O método .is.. realiza a verificação do objeto
print(nome2.isnumeric())
print(nome2.isupper())
print(nome2.isalpha()) # verifica se é letra
print(nome2.isalnum())


print(f"{nome2[0:1:1]}") # 0 - do primeiro índice :1 até o primeiro índice :1 exibe de quantas em quantas letras.

print(f"{nome2[::2]}") # 0 - Deverá exibir as letras Dne

nome3 = str(input("Insira o seu nome: ")).strip().split() # o método split() divide/quebra os valores e os coloca em uma lista
print(f"{nome3}")


print(f"{nome3[len(nome3) - 1 ]}")