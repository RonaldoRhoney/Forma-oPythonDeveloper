contatos = {
    "ronaldorhoney@hotmail.com": {"nome": "ronaldo", "telefone": "91985541216"}
}

copia = contatos.copy()
copia["ronaldorhoney@hotmail.com"] = {"nome": "Rhoney"}

contatos["ronaldorhoney@hotmail.com"] # {"nome": "Ronaldo", "telefone": 91985541216}
copia["ronaldorhoney@hotmail.com"] # {"nomee": "Rhoney"}