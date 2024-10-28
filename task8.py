# Напишите рекурсивную функцию, которая
# раскладывает натуральное число на простые сомножители.
#
# Пример:
# Ввод:
# 378
# Вывод:
# 2*3*3*3*7

n = int(input())

def func(n, k=2, r=[]):
    if n==1:
        return r
    if n%k==0:
        return func(n // k, k, r + [k])
    else:
        return func(n, k + 1, r)

func(n)
print(func(n))
