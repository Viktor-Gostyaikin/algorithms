class StackMax:
    def __init__(self):
        self.items = []
        self.max_item = []
    def push(self, item):
        self.items.append(item)
        if len(self.max_item) > 0:
            if item > self.max_item[-1]:
                self.max_item.append(item)
            else:
                self.max_item.append(self.max_item[-1])
        else:
            self.max_item.append(item)
            
    def pop(self):
        self.items.pop()
        self.max_item.pop()

    def get_max(self):
        if len(self.items) == 0:
            return 'None'
        return self.max_item[-1]


def calculate(commands):
    result = ''
    stack = StackMax()
    for command in commands:
        if command[0] == 'get_max':
            result += f'{stack.get_max()}\n'
        elif command[0] == 'pop':
            if len(stack.items) == 0:
                result += 'error\n'
            else:
                stack.pop()
        elif command[0] == 'push':
            stack.push(int(command[1]))
    return result
    

def main():
    with open('input.txt', 'r') as file:
        count = int(file.readline().strip())
        commands = [file.readline().strip().split() for index in range(count)]
    print(calculate(commands))

if __name__ == '__main__':
    main()



