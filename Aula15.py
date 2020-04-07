"""
Estrutura compostas
Tuplas ()
Listas []
*Dicionários {}
"""
dados = dict()

dados = {"nome":'Pedro',"idade":25}

print(dados)

print(dados['nome'])

dados['sexo'] = 'M'

print(dados)

dados['peso'] = 80

print(dados)

del dados['peso']

print(dados)

filme1 = {'titulo':'Star Wars',
         'ano':1977,
         'diretor':'George Lucas'
         }

filme2 = {'titulo':'Matrix',
         'ano':1999,
         'diretor':'Wachouski'
         }

filme3 = {'titulo':'Avengers',
         'ano':2012,
         'diretor':'Joss Whedon'
         }

print(filme1.values())

print(filme1.keys())

print(filme1.items())

for k,v in filme1.items():
    print(f'O {k} é {v}')

print('\n')  
locadora = list()

locadora.append(filme1)
locadora.append(filme2)
locadora.append(filme3)

print(locadora)

estado = dict()
brasil = list()

for c in range(0,3):
    estado['uf'] = str(input("Unidade Federativa: "))
    estado['sigla'] = str(input("Sigla do Estado: "))
    brasil.append(estado.copy())

print(brasil)

for e in brasil:
    print(e)

for e in brasil:
    for k, v in e.items():
        print(f"O campo {k} tem o valor {v}")
        
for e in brasil:
    for v in e.values():
        print(v)
