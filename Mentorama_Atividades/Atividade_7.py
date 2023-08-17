from collections import deque


def ehDigito(caractere):
    return caractere.isdigit()


def lista_encadeada(lista):
    fila_letras = deque()
    pilha_digitos = []

    for caractere in lista:
        if ehDigito(caractere):
            pilha_digitos.append(caractere)
        else:
            fila_letras.append(caractere)

    resultado = []
    while fila_letras:
        resultado.append(fila_letras.popleft())

    while pilha_digitos:
        resultado.append(pilha_digitos.pop())

    return resultado


listas_encadeadas = ['a', '1', 'e', '5', 't', '7', 'w', '8', 'g']
resultado = lista_encadeada(listas_encadeadas)
print(resultado)
