import threading
from threading import Thread


def proc1():
    print('Processo 1')


# função inicializada
t1 = Thread(target=proc1()).start()
# retorna se o objeto thread criado ativa atualmente
print('A thread está ativa: ', threading.current_thread().is_alive())
# retorna o nome da thread ativa atualmente
print('O Nome da thread atual:', threading.current_thread().getName())
# retorna o identificador de thead da thread atual
print('Consulta o indicador thead do trhead atual:', threading.get_ident())
# retorna a quantidade de threads ativas atualmente
print('Quantidade de thread ativa:', threading.active_count())
# retorna uma lista com as threads ativas atualmente
print('Lista com todos os threads ativos:', threading.enumerate())
