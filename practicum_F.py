'''
    Формат ввода
    В единственной строке записана фраза или слово.
    Буквы могут быть только латинские.
    Длина текста не превосходит 20000 символов.

    Формат вывода
    Выведите «True», если фраза является палиндромом, и «False», если не является.
'''

import string

def _input(file):
    with open(file, 'r') as file:
        sentence = list(file.readline().strip())
        punctuation_list = string.punctuation + string.digits + '\n\xa0«»\t—… ,.'
    clean_text = list(''.join(
        [letter.lower() for letter in sentence if letter not in punctuation_list]
    ))
    return clean_text

def _calculation(clean_text:list, palindrom:bool=False):
    count_lett = len(clean_text)
    if count_lett == 1:
        palindrom = True
    else:
        for i in range(count_lett//2):
            if clean_text[i] == clean_text[-i-1]:
                palindrom = True
            else:
                palindrom = False
                break
    return palindrom
print(_calculation(_input('input.txt')))
