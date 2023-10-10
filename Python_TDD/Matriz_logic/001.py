import time

matriz = [[25.0, 20.0, 19.3, 15.9], [18.7, 24.5, 17.8, 19.9], [22.4, 19.2, 15.9, 23.8]]


novaMatriz = []

inicio = time.time()

for linha in matriz:
    listaNotas = []
    for elemento in linha:
        listaNotas.append(elemento * 2)
    novaMatriz.append(listaNotas)

fim = time.time()

print(f'Tempo de execucao: {fim - inicio}')

print(novaMatriz)
