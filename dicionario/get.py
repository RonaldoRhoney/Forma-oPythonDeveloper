contatos = {
    "ronaldorhoney@hotmail.com": {"nome": "Ronaldo", "telefone": "91985541216"}
}

contatos["chave"] #KeyError

contatos.get("chave") # None
contatos.get("chave", {}) # {}
contatos.get("ronaldorhoney@hotmail.com", {}) # {"ronaldorhoney@hotmail.com": {"nome": "ronaldo", "telefone": "91985541216"}}