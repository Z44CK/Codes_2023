def verifica_multiplo(n):
    if n % 5 == 0 and n % 7 == 0:
        return 'FizzBuzz'
    elif n % 5 == 0:
        return 'Fizz'
    elif n % 7 == 0:
        return 'Buzz'
    else:
        return 'miss'
