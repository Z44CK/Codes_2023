# Programa alterado para mostrar a variação de tempo e seu tempo de processamento!

import time

n = 'Olá, mundo!'

for i in range(5):
    print(n)
    time.sleep(3)
print('Variação do tempo', time.perf_counter())
print('Tempo de processamento', time.time())
