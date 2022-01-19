# 59365031

'''
Формат ввода
    В первой строке задано число участников n, 1 ≤ n ≤ 100 000.
    В каждой из следующих n строк задана информация про одного из участников.
    i-й участник описывается тремя параметрами:
        - уникальным логином (строкой из маленьких латинских букв длиной не 
            более 20)
        - числом решённых задач Pi
        - штрафом Fi
        - Fi и Pi — целые числа, лежащие в диапазоне от 0 до 109.
Формат вывода
    Для отсортированного списка участников выведите по порядку их логины по 
    одному в строке.
'''


def effective_quick_sort(array):
    def partition(left, right):
        pivot = array[(left + right) // 2]
        while left < right:
            while array[left] > pivot:
                left += 1
            while pivot > array[right]:
                right -= 1
            array[left], array[right] = array[right], array[left]
        return right

    def quick_sort(left, right):
        if left < right:
            partition_index = partition(left, right)
            quick_sort(left, partition_index - 1)
            quick_sort(partition_index + 1, right)

    quick_sort(0, len(array) - 1)

    return array


if __name__ == '__main__':
    class Participant:
        def __init__(self, login, proper, forfeit):
            self.login = login
            self.proper = int(proper)
            self.forfeit = int(forfeit)

        def __gt__(self, other):
            if self.proper < other.proper:
                return False
            if self.proper > other.proper:
                return True
            if self.forfeit < other.forfeit:
                return True
            if self.forfeit > other.forfeit:
                return False
            return self.login < other.login

        def __str__(self) -> str:
            return self.login

    nums = (int(input()))
    participants = [
        Participant(*input().split()) for _ in range(nums)
    ]

    effective_quick_sort(participants)

    print(*participants, sep='\n')
