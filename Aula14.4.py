import random

maquina = random.randint(0,10)

escolha = str(input("[I]impar ou [P]par: "))[0].strip().upper()

if escolha == "I":
    print("Você escolheu Impar \n")
else:
    print("Você escolheu Par \n")

valor = int(input("Insira um numero entre 0 e 10: "))

soma = maquina + valor
print (f"Sua jogada {valor} \nA jogada do computador {maquina}\n")
if soma % 2 == 0:
    if escolha == "P":
        print("Você ganhou!")
    else:
        print("Você perdeu :(")
else:
    if escolha == "I":
        print("Você perdeu :(!")
    else:
        print("Você ganhou!")
        
print("Fim de jogo")


