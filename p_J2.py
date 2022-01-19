class Node:  
    def __init__(self, value, next_item=None):  
        self.value = value  
        self.next_item = next_item

class ListQueue:
    def __init__(self):
        self._size = 0
        self.head = None
        self.tail = None
    
    def put(self, item):
        if self.head == None:
            self.head = Node(value=item)
            self.tail = self.head
            self._size += 1
        else:
            self.tail.next_item = Node(value=item)
            self.tail = self.tail.next_item
            self._size += 1
    
    def get(self):
        if self.head != None:
            rtrn = self.head
            self.head = self.head.next_item
            self._size -= 1
            return rtrn.value + '\n'
        else:
            return 'error\n'
    
    def size(self):
        return str(self._size) + '\n'

def calculate(commands):
    '''
    get() — вывести элемент, находящийся в голове очереди, и удалить его.
        Если очередь пуста, то вывести «error».
    put(x) — добавить число x в очередь
    size() — вывести текущий размер очереди'''
    queue = ListQueue()
    result = ''
    for command in commands:
        if command[0] == 'put':
            queue.put(command[1])
        elif command[0] == 'get':
            result += queue.get()
        elif command[0] == 'size':
            result += queue.size()
    return result

def main():
    with open('input.txt', 'r') as file:
        count_commands = int(file.readline().strip())
        commands = []
        for idx in range(count_commands):
            commands.append(file.readline().strip().split())
    print(calculate(commands))
    # print(commands)

if __name__ == '__main__':
    main()