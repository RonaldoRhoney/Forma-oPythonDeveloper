#neste método você cria chaves e pode determinar o que será posto em cada parâmetro:

dict.fromkeys(["nome", "telefone"]) # {"nome": "telefone": None}

dict.fromkeys(["nome", "telefone"], "vazio") # {"nome": "vazio", "telefone": "vazio"}