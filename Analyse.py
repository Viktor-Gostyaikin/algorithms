import time
'''
Алгоритм вычисления
среднего числа случаев выполнения деления
в алгоритме Евклида 
'''

N = 1000
sum_of_iter = 0
sum_of_iter2 = 0
sum_of_iter3 = 0

'''
Скорость выполнения в два раза меншье, чем у второй функции
'''

def eculid(m:float, n:float):
    count = 0
    if n > m:
        m, n = n, m
    while n and m:
        m = m % n
        count += 1
        if m == 0:
            return n, count
        else:
            n = n % m
            count += 1
            if n == 0:
                return m, count


'''
Самый быстрый по скорости.
'''
def eculid_2(m, n):
    count = 0
    if n > m:
        m, n = n, m
    r=m%n
    count += 1
    while r:
        m=n
        n=r
        r=m%n
        count += 1
    return n, count


'''
Самый долгий, в 2,5 раза дольше, чем второй
'''

def eculid_recursion(m, n, count=0):
    count += 1
    if m == 0:
        return n, count
    return eculid_recursion(n % m, m, count)



for m in range(1, N+1):
    nod, sum = eculid(m, N)
    sum_of_iter += sum
    # print(n, m, nod, sum)
    nod2, sum2 = eculid_2(m, N)
    sum_of_iter2 += sum2
    nod3, sum3 = eculid_recursion(m, N)
    sum_of_iter3 += sum3
    # print(m, sum, sum2, sum3)
result = sum_of_iter/N
result2 = sum_of_iter2/N
result3= sum_of_iter3/N
print(result, result2, result3)


'''
Сравнение быстроты выполнения функций
'''
start = time.monotonic()
for m in range(100000):
    eculid(m, N)
result = time.monotonic() - start
print("standard time : {:>.3f}".format(result) + " seconds")
start = time.monotonic()
for i in range(100000):
    eculid_2(m, N)
result = time.monotonic() - start
print("standard time: {:>.3f}".format(result) + " seconds")
start = time.monotonic()
for i in range(100000):
    eculid_recursion(m, N)
result = time.monotonic() - start
print("standard time: {:>.3f}".format(result) + " seconds")