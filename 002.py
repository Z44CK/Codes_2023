# Pede o valor de duas notas e calcule sua média, A atribuição de conceitos obedece à tabela abaixo:
# Média de Aproveitamento  Conceito
# Entre 9.0 e 10.0        A
# Entre 7.5 e 9.0         B
# Entre 6.0 e 7.5         C
# Entre 4.0 e 6.0         D
# Entre 4.0 e zero        E
# Existe outras maneiras de resolver esse excercicio, essa foi a primeira forma que encontrei!! 

nota1 = float(input('Informe a nota 1: '))
nota2 = float(input('Informe a nota 2: '))

media = (nota1 + nota2) / 2

if media > 9.0 <= 10.0:
     print(f'Nota: {nota1}, {nota2}\n'
           f'Media: {media:.2f}\n'
           f'Conceito A: Aprovado!\n')
elif media > 7.5 <= 9.0:
     print(f'Nota: {nota1}, {nota2}\n'
           f'Media: {media:.2f}\n'
           f'Conceito B: Aprovado!\n')
elif media > 6.0 <= 7.5:
     print(f'Nota: {nota1}, {nota2}\n'
           f'Media: {media:.2f}\n'
           f'Conceito C: Aprovado!\n')
elif media > 4.0 <= 6.0:
     print(f'Nota: {nota1}, {nota2}\n'
           f'Media: {media:.2f}\n'
           f'Conceito D: Reprovado!\n')
elif media == 0 <= 4.0:
     print(f' Nota: {nota1}, {nota2}\n'
           f'Media: {media:.2f}\n'
           f'Conceito E: Reprovado!\n')
else:
  print('Entre com um valor valido:')
