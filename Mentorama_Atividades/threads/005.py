from threading import Thread
import time


def soma1(a, b):

    numeros = range(a, b)
    print(sum(numeros))


def soma2(a, b):
    soma = 0
    for numero in range(a, b):
        soma += numero
    print(soma)


inicio = time.time()

t1 = Thread(target=soma1, args=[1, 2000])
t2 = Thread(target=soma2, args=[1, 1560])

t1.start()
t2.start()

t2.join()
fim = time.time()
print()
print(f'Fim da execução: {fim-inicio}')
