contatos = {
    "ronaldorhoney@hotmail.com": {"nome": "Ronaldo", "telefone": "91985541216"},
    "ronaldorhoney6910@gmail.com": {"nome": "Rhoney", "telefone": "91981015189"},
}

resultado = "ronaldorhoney@hotmail.com" in contatos #True
print(resultado)

resultado = "jluia@gmail.com" in contatos # False
print(resultado) 

resultado = "idade" in contatos["ronaldorhoney6910@gmail.com"]  # False
print(contatos)

resultado = "telefone" in contatos["ronaldorhoney@hotmail.com"] # True
print(contatos)