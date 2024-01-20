saldo = 1000
saque = 250
limite = 200
conta_especial = True

exp = saldo or saque and limite or conta_especial and saldo or saque
print(exp)