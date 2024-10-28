# Напишите функцию convert_base(num, from_base, to_base),
# которая переводит натуральное число num из системы
# счисления с основанием from_base в систему счисления
# с основанием to_base
# 2 ≤ to_base ≤ 36 ; 2 ≤ from_base ≤ 36
# На входе три числа num, from_base, to_base
# На выходе одно число - результат работы функции
# Подсказка (если не получается решить):
# Попробуйте разбить задачу на две подзадачи:
# перевод из десятичной системы счисления в любую
# перевод из любой системы счисления в десятичную
# Объедините эти две подзадачи, получите ответ.

import string
def convert_base(num, from_base, to_base):
    nums_symbols = list(string.digits) + list(string.ascii_uppercase)
    num = list(reversed(list(num)))
    num_in_10 = 0
    for i in range(len(num)):
        num_in_10 += nums_symbols.index(num[i]) * (from_base**i)

    num_digits = []
    while num_in_10 >= 1:
        num_digits.append(nums_symbols[num_in_10 % to_base])
        num_in_10 //= to_base
    num_out = ''.join(list(reversed(num_digits)))
    return num_out


num = input()
print(convert_base(num, 13, 30))

