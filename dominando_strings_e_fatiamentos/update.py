# este método permite atualização do dicionário:
contatos = {
    "ronaldorhoney@hotmail.com": {'nome': 'Ronaldo', 'telefone': '91985541216'}
}

contatos.update({"ronaldorhoney@hotmail.com": {"nome": "Rhoney"}})
contatos # {"ronaldorhoney@hotmail.com": {"nome": "Rhoney"}

contatos.update({"douglas_s@gmail.com": {"nome": "Douglas", "telefone": "11111111999"}})

contatos # {"ronaldorhoney@hotmail.com": {"nome": "Rhoney"}, {"douglas_s@gmail.com": {"nome": "Douglas", "telefone": "11111111999"}}