def calcular_total(numeros):
    return sum(numeros)



def retono_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor



print(calcular_total([10, 20, 34])) # 64
print(retono_antecessor_e_sucessor(10)) # (9, 11)
