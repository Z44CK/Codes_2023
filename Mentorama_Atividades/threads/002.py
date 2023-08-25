from threading import Thread
import time


def proc1():
    print('Processo 1')
    time.sleep(5)


def proc2():
    print('Processo 2')
    time.sleep(30)


print()
# inicia as threads
t1 = Thread(target=proc1)
t1.start()
print()
t2 = Thread(target=proc2)
t2.start()

# Aguarda um tempo para permitir que as threads sejam inicializadas
time.sleep(2)

# verifica o status das threads
print('A thread 1 está ativa:', t1.is_alive())
print('A thread 2 está ativa:', t2.is_alive())

# aguarda as threads terminarem
t1.join()
t2.join()

print('Todas as threads foram finalizadas')
