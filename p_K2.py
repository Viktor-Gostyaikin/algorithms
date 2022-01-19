import math

def calculate(num, degree):
    factorial = math.factorial(num - 2) 
    return (factorial + (factorial * (num - 1)))

def main():
    with open('input.txt', 'r') as file:
        num = list(map(int, file.readline().strip().split()))
    print(calculate(num[0], num[1]))

if __name__ == '__main__':
    main()