# Напишите процедуру, которая выводит на экран
# запись переданного ей числа в римской системе счисления.
# Числа находятся в диапазоне [1, 3999]
# I - 1, V - 5, X - 10, L - 50, C  - 100, D - 500, M - 1000
# Пример:
# 2013
# MMXIII

num_in = int(input())
num_out = ''
num_out += (num_in//1000) * 'M'
num_in -= (num_in//1000)*1000

num_out += (num_in//500) * 'D'
num_in -= (num_in//500)*500

num_out += (num_in//100) * 'C'
num_in -= (num_in//100)*100

num_out += (num_in//50) * 'L'
num_in -= (num_in//50)*50

num_out += (num_in//10) * 'X'
num_in -= (num_in//10)*10

num_out += (num_in//5) * 'V'
num_in -= (num_in//5)*5

num_out += (num_in//10) * 'I'
num_in -= (num_in//10)*10

print(num_in, num_out)



# def rome_nums(n):
#     if n == 'I': return 1
#     elif n == 'V': return 5
#     elif n == 'X': return 10
#     elif n == 'L': return 50
#     elif n == 'C': return 100
#     elif n == 'D': return 500
#     elif n == 'M': return 1000
#     else: return 0
#
# num_in = list(input() + 2*' ')
#
# num = 0
# num += rome_nums(num_in[0])
# i = 0
#
# while i < len(num_in) - 1:
#     if rome_nums(num_in[i]) > rome_nums(num_in[i+1]): #если VI
#         if rome_nums(num_in[i+1]) >= rome_nums(num_in[i+2]):
#             num += rome_nums(num_in[i+1])
#         i += 1
#     if rome_nums(num_in[i]) == rome_nums(num_in[i+1]):
#         num += rome_nums(num_in[i+1])
#         i += 1
#
#     elif rome_nums(num_in[i]) < rome_nums(num_in[i+1]):
#         num -= rome_nums(num_in[i+1])
#
#
#         i += 1
#     num = abs(num)
#
# print(num)



