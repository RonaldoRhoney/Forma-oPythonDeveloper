contatos = {
    "ronaldorhoney@hotmail.com": {"nome": "Ronaldo", "telefone": "91985541216"},
    "ronaldorhoney6910@gmail.com": {"nome": "Rhoney", "telefone": "91981015189", "extra": {"a": 1}},
}

#acessando os dados:

telefone = contatos["ronaldorhoney@hotmail.com"]["telefone"] # "91985541216"
print(telefone)

extra = contatos["ronaldorhoney6910@gmail.com"]["extra"]["a"]
print(extra)