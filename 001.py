# Programa que pede três valores, e a soma dos valores deve informar se pode se um triangulo equilátero, isósceles, escalno ou se não forma triangulo algum.


lado1 = float(input('Informe primeiro valor: '))
lado2 = float(input('Informe segundo valor: '))
lado3 = float(input('Informe terceiro valor: '))

if (lado1 + lado2 < lado3) or (lado1 + lado3 < lado2) or (lado2 + lado3 < lado1):
    print('Não é um triangulo')
elif (lado1 == lado2) and (lado1 == lado3):
    print('Triangulo Equilátero: três lados iguais')
elif (lado1 == lado2) or (lado1 == lado3) or (lado2 == lado3):
    print('Triangulo Isósceles: quaisquer dois lados iguais')
else:
    print('Triangulo Escaleno: três lados diferentes')

