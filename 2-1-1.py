"""
На вход программе подаются два целых числа aaa и bbb. Напишите программу, которая выводит:

    сумму чисел aaa и bbb;
    разность чисел aaa и bbb;
    произведение чисел aaa и bbb;
    частное чисел aaa и bbb;
    целую часть от деления числа aaa на bbb;
    остаток от деления числа aaa на bbb;
    корень квадратный из суммы их 10-х степеней: sqrt(a^10 + b^10)
"""

a = int(input())
b = int(input())

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(((a ** 10) + (b ** 10)) ** (1/2))

