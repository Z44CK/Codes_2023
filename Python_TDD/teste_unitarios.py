import pytest
from test_fizzbuzz import verifica_multiplo


class testemutiplos:

    def teste_multiplo_de_5(self):
        assert (verifica_multiplo(10), 'Fizz')

    def teste_multiplo_de_7(self):
        assert(verifica_multiplo(14), 'Buzz')

    def teste_mutiplo_de_ambos(self):
        assert(verifica_multiplo(35), 'FizzBuzz')

    def test_nao_multiplo(self):
        assert(verifica_multiplo(8), 'miss')


if __name__ == '__main__':
    pytest.main()
    
