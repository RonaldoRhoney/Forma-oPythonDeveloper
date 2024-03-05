nome  = "Rhoney"
idade = 30
profissao = "Desenvolvedor"
linguagem = "Python"
saldo = 50.529

dados = {"nome": "Rhoney", "idade": 30}

print("Nome: %s Idade: %d" % (nome, idade))

print("Nome: {} Idade {}".format(nome, idade))

print("Nome: {1} Idade: {0}".format(idade, nome))
print("Nome: {1} Idade {0} nome: {1} {1}".format(idade, nome))

print("Nome:{nome} Idade: {Idade}".format(nome=nome, Idade=idade))
print("Nome: {name} Idade: {age} {name} {age}".format(age=idade, name=nome))
print("Nome: {nome} Idade: {idade}".format(**dados))

print(f"Nome: {nome} Idade: {idade}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.2f}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:10.2f}")


