#iterar dicionários: Forma mais comum para percorrer os dados de um dicionário é utilizando o comando "for"
contatos = {
    "ronaldorhoney@hotmail.com": {"nome": "Ronaldo", "telefone": "91985541216"},
    "ronaldorhoney6910@gmail.com": {"nome": "Rhoney", "telefone": "91981015189"},
}

for chave, valor in contatos.items():
    print(chave, valor)