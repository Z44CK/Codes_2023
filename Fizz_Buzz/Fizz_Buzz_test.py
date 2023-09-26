# Para quem está com dificuldades para resolver esse probleminha, criei essa solução, fiz e refiz várias vezes
# até chegar nessa solução, utilizo o site HackerRank para resolver desafios diários.

def fizzbuzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print('fizzbuzz')
        elif i % 3 == 0:
            print('fizz')
        elif i % 5 == 0:
            print('buzz')
        else:
            print(i)


if __name__ == '__main__':
    n1 = int(input().strip())
    fizzbuzz(n1)

# Neste código, a função fizzBuzz recebe um valor inteiro
# de n como parâmetro e implementa a lógica para imprimir a sequência de
# FizzBuzz de acordo com as condições especificadas.
# No bloco if __name__ == '__main__':, você pode ler o valor de n a partir da entrada padrão e
# em seguida, chamar a função fizzBuzz para imprimir a sequência até o valor de n.
