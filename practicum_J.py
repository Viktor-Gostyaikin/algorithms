'''
    Формат ввода
    В единственной строке дано число n (2 ≤ n ≤ 109), которое нужно факторизовать.

    Формат вывода
    Выведите в порядке неубывания простые множители, на которые раскладывается число n.
'''
def _input(file):
    with open(file, 'r') as file:
        n = int(file.readline().strip())
    return n

def calculate(n):
    i = 2
    primes = ''
    while i * i <= n:
        if i != 0:
            while n % i == 0:
                n = int(n / i)
                primes = primes + str(i) + ' '
        i += 1
    if n > 1:
        primes += str(n)
    
    return primes
print(calculate(_input('input.txt')))