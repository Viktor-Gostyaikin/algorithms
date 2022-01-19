class MyQueueSized:
    def __init__(self, max_size):
        self.queue = [None] * max_size
        self.max_size = max_size
        self.head = 0
        self.tail = 0
        self._size = 0
    
    def is_empty(self):
        return self._size == 0

    def push(self, item):
        if self._size != self.max_size:
            self.queue[self.tail] = item
            self.tail = (self.tail + 1) % self.max_size
            self._size += 1
            return ''
        else:
            return 'error\n'

    def pop(self):
        if self.is_empty():
            return 'None\n'
        item = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_size
        self._size -= 1
        return item + '\n'

    def peek(self):
        '''напечатать первое число в очереди'''
        if self.is_empty():
            return 'None\n'
        return self.queue[self.head] + '\n'

    def size(self):
        '''вернуть размер очереди'''
        return str(self._size) + '\n'


def calculate(size_queue, commands):
    '''При превышении допустимого размера очереди нужно вывести «error».
    При вызове операций pop() или peek() для пустой очереди нужно вывести «None».'''
    queue = MyQueueSized(max_size=size_queue)
    result = ''
    for command in commands:
        if command[0] == 'push':
            result += queue.push(command[1])
        elif command[0] == 'pop':
            result += queue.pop()
        elif command[0] == 'peek':
            result += queue.peek()
        elif command[0] == 'size':
            result += queue.size()
    return result

def main():
    with open('input.txt', 'r') as file:
        count_commands = int(file.readline().strip())
        size_queue = int(file.readline().strip())
        commands = []
        for idx in range(count_commands):
            commands.append(file.readline().strip().split())
    print(calculate(size_queue, commands))

if __name__ == '__main__':
    main()