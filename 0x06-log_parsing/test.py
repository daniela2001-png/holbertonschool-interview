def min_maquina():
    Xi = 1.0
    while Xi / 2.0 > 0.0:
        Xi = Xi / 2.0
    return Xi


print("El m´ınimo n´umero positivo", end=" ")
print("en esta m´aquina es:", min_maquina())
