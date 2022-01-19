# 58826118

'''
Формат ввода
    В первой строке записано количество команд n — целое число, не
    превосходящее 100000. Во второй строке записано число m — максимальный
    размер дека. Он не превосходит 50000. В следующих n строках записана одна
    из команд:
        push_back(value) – добавить элемент в конец дека. Если в деке уже
            находится максимальное число элементов, вывести «error».
        push_front(value) – добавить элемент в начало дека. Если в деке уже
            находится максимальное число элементов, вывести «error».
        pop_front() – вывести первый элемент дека и удалить его. Если дек был
            пуст, то вывести «error».
        pop_back() – вывести последний элемент дека и удалить его. Если дек 
            был пуст, то вывести «error».
    Value — целое число, по модулю не превосходящее 1000.

Формат вывода
    Выведите результат выполнения каждой команды на отдельной строке.
    Для успешных запросов push_back(x) и push_front(x) ничего 
    выводить не надо.
'''

OPERATIONS = {
    'push_back': lambda queue, value: queue.push_back(value),
    'push_front': lambda queue, value: queue.push_front(value),
    'pop_back': lambda queue: queue.pop_back(),
    'pop_front': lambda queue: queue.pop_front(),
}


class DequeIsFullError(Exception):
    pass


class Deque:
    def __init__(self, max_size):
        self.__queue = [None] * max_size
        self.__max_size = max_size
        self.__front = 0
        self.__back = 1
        self.__size = 0

    def is_empty(self):
        return self.__size == 0

    def __unar_operation(self, attribute: int, flag: bool):
        if flag:
            attribute += 1
        else:
            attribute -= 1
        return attribute % self.__max_size

    def push_back(self, value):
        if self.__size == self.__max_size:
            raise DequeIsFullError('Deque is full')
        else:
            self.__queue[self.__back] = value
            self.__back = self.__unar_operation(self.__back, True)
            self.__size += 1

    def push_front(self, value):
        if self.__size == self.__max_size:
            raise DequeIsFullError('Deque is full')
        else:
            self.__queue[self.__front] = value
            self.__front = self.__unar_operation(self.__front, False)
            self.__size += 1

    def pop_back(self):
        if self.is_empty():
            raise IndexError('Deque is empty')
        else:
            self.__back = self.__unar_operation(self.__back, False)
            value = self.__queue[self.__back]
            self.__queue[self.__back] = None
            self.__size -= 1
            return value

    def pop_front(self):
        if self.is_empty():
            raise IndexError('Deque is empty')
        else:
            self.__front = self.__unar_operation(self.__front, True)
            value = self.__queue[self.__front]
            self.__queue[self.__front] = None
            self.__size -= 1
            return value


def calculate(size_queue, commands):
    queue = Deque(max_size=size_queue)
    result = []
    for command, *arguments in commands:
        if command in OPERATIONS:
            try:
                operation = OPERATIONS[command](queue, *arguments)
                if operation is not None:
                    result.append(operation)
            except (IndexError, DequeIsFullError,):
                result.append('error')
    return result


def main():
    with open('input.txt', 'r') as file:
        count_commands = int(file.readline().strip())
        size_queue = int(file.readline().strip())
        commands = []
        for idx in range(count_commands):
            commands.append(file.readline().strip().split())
    print(*calculate(size_queue, commands), sep='\n')


if __name__ == '__main__':
    main()
