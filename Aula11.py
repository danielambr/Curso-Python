nome = str(input("Insira seu nome\n")).strip() #o método remove os espaços antes do nome

print(f"Olá {nome}")

nome2 = str(input("Insira seu nome\n")).strip("n") #o método remove os espaços

print(f"Olá {nome2}")

nome3 = str(input("Insira seu nome\n")).capitalize() #o método coloca a primeira letra em maiúsculo
nome4 = str(input("Insira seu nome\n")).upper() # o método coloca todas as letras em maiúsculo 
                                                # Para deixar o nome em minusculo utilizar o método lower()

if nome3 == nome4:
    print(f"Os nomes: {nome3} e {nome4} são iguais")
else:
    print(f"Os nomes: {nome3} e {nome4} são diferentes")

