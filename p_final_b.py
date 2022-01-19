# 58826136
'''
Формат ввода
В единственной строке дано выражение, записанное в обратной польской
нотации. Числа и арифметические операции записаны через пробел.

На вход могут подаваться операции: +, -, *, / и числа, по модулю не
превосходящие 10000.

Гарантируется, что значение промежуточных выражений в тестовых данных
по модулю не больше 50000.

Формат вывода
Выведите единственное число — значение выражения.
'''

OPERATIONS = {
    '+': lambda stack, operand_1, operand_2:
        stack.push(operand_1 + operand_2),
    '-': lambda stack, operand_1, operand_2:
        stack.push(operand_1 - operand_2),
    '*': lambda stack, operand_1, operand_2:
        stack.push(operand_1 * operand_2),
    '/': lambda stack, operand_1, operand_2:
        stack.push(operand_1 // operand_2),
}


class Stack:
    def __init__(self):
        self.__items = []

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        try:
            return self.__items.pop()
        except IndexError:
            raise IndexError('Stack is empty')


def calculate(notation):
    stack = Stack()
    for sym in notation:
        if sym in OPERATIONS:
            operand_2, operand_1 = int(stack.pop()), int(stack.pop())
            OPERATIONS[sym](stack, operand_1, operand_2)
        else:
            stack.push(int(sym))
    return stack.pop()


def main():
    with open('input.txt', 'r') as file:
        notation = file.readline().strip().split()

    print(calculate(notation))


if __name__ == '__main__':
    main()
