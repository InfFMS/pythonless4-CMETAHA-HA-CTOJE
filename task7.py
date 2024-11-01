# Напишите функцию is_valid_triangle(side1, side2, side3),
# которая принимает в качестве аргументов три натуральных числа,
# и возвращает значение True, если существует невырожденный треугольник
# со сторонами side1, side2, side3, или False в противном случае.

def is_valid_triangle(side1, side2, side3):
    if side1 + side2 > side3: return True
    elif side1 + side3 > side2: return True
    elif side2 + side3 > side1: return True
    else: return False
