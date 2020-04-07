salario = int(input("Informe o valor do salario"))
porcent = int(input("Informe a porcentagem de reajuste"))

print(f"O valor do salario reajustado é de R$ {salario + salario * porcent /100} reais.")

reajuste = salario * porcent / 100

print(f"O valor do salario reajustado é de R$ {salario + reajuste} reais.")