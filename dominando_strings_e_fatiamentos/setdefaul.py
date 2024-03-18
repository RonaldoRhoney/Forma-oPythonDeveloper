contatos = {"nome": "Ronaldo", "telefone": "91985541216"}

contatos.setdefault("nome", "Pedro") # "Ronaldo" não haverá alterações 
print(contatos) # {'nome': 'Ronaldo', 'telefone': '91985541216'}

contatos.setdefault("idade", 28)
print(contatos) # {'nome': 'Ronaldo', 'telefone': '91985541216', "idade": 28} houve mudança, uma vez que a chave idade = 28 não existia anteriormente
