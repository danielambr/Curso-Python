from random import choice

print("      ##  #######     ##    ## ######## ##    ##    ########   #######  ")
print("      ## ##     ##    ##   ##  ##       ###   ##    ##     ## ##     ## ")
print("      ## ##     ##    ##  ##   ##       ####  ##    ##     ## ##     ## ")
print("      ## ##     ##    #####    ######   ## ## ##    ########  ##     ## ")
print("##    ## ##     ##    ##  ##   ##       ##  ####    ##        ##     ## ")
print("##    ## ##     ##    ##   ##  ##       ##   ###    ##        ##     ## ")
print(" ######   #######     ##    ## ######## ##    ##    ##         #######  \n")
 
player = str(input("Escolha entre: pedra, papel ou tesoura: "))
opcoes = ["pedra","papel","tesoura"]
maquina = choice(opcoes)
print(f"Você escolheu {player} e o computador escolheu {maquina}")
if player == maquina:
    print("Empate!")
else:
    if player == "pedra" and maquina == "papel":
        print("Você perdeu")
    elif player == "tesoura" and maquina == "pedra":
        print("Você perdeu")
    elif player == "papel" and maquina == "tesoura":     
        print("Você perdeu")
    elif player == "tesoura" and maquina == "papel":
        print("Você ganhou!")
    elif player == "pedra" and maquina == "tesoura":
        print("Você ganhou!")
    elif player == "papel" and maquina == "pedra":
        print("Você ganhou!")
print("\n FIM DE JOGO!")





