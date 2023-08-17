# Exemplo de uma classe e seus objetos

class Carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} acelerou...')


fusca = Carro('Fusca')
fusca.acelerar()
celta = Carro('Celta')
celta.acelerar()
