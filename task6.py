# Напишите функцию, которая сокращает дробь вида M/N.
# Где M и N - наутральные числа.
# В качестве аргументов она принимает числитель и знаменатель,
# выводит числитель и знаменатель после сокращения
#
# Пример:
# Ввод:
# 25 15
# Вывод:
# 5 3

nums_input = list(map(int, input().split()))
D = 1
while nums_input[0] >= D and nums_input[1] >= D:
    if nums_input[0] % D == 0 and nums_input[1] % D == 0:
        nums_input[0] /= D
        nums_input[1] /= D
    D += 1
nums_input = map(int, nums_input)
output = ' '.join(map(str, nums_input))
print(output)

