dicionarioordenado = {'color 1': 'Red', 'color 2': 'Green', 'color 3': 'Blue'}
print(dicionarioordenado)

novo_elemento = {'color 4': 'Orange'}
dicionarioordenado = {**novo_elemento, **dicionarioordenado}

print(dicionarioordenado)
