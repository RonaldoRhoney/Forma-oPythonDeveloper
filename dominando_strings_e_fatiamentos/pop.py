contatos = {
    "ronaldorhoney@hotmail.com": {"nome": "Ronaldo", "telefone": "91985541216"}
}

resultado = contatos.pop("ronaldorhoney@hotmail.com") # {"nome": "Ronaldo", "telefone": "91985541216"}

print(resultado)

resultado = contatos.pop("ronaldorhoney@hotmail.com", "nao encontrou") # {}
print(resultado)