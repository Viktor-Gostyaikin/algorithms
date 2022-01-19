'''Формат ввода
    В первой строке дана длина текста L (L ≤ 105).

    В единственной строке записан текст, состоящий из строчных латинских букв и пробелов.
    Слово —– последовательность букв, не разделённых пробелами. 
    Пробелы могут стоять в самом начале строки и в самом её конце.

    Формат вывода
    В первой строке выведите самое длинное слово. Во второй строке выведите его длину.
    Если подходящих слов несколько, выведите то, которое встречается раньше.
'''
def _input(file:str):
    with open(file, 'r') as file:
        length_text = int(file.readline().strip())
        text = file.readline().strip().split()
    return length_text, text

def _calculate(length_text, text, count_words=0, longest_word='', count_letters=0):
    length_text -= len(text) - 1
    for i in text:
        if length_text < len(i):
            break
        else:
            length_text -= len(i)
            count_words += 1
    for i in range(count_words):
        count = len(text[i])
        if count > count_letters:
            longest_word = text[i]
            count_letters = count
    return f'{longest_word}\n{count_letters}'

print(_calculate(*_input('input.txt')))