"""
Дано пятизначное или шестизначное натуральное число.
Напишите программу, которая изменит порядок его последних пяти цифр на обратный.
Формат входных данных
На вход программе подается одно натуральное пятизначное или шестизначное число.

Формат выходных данных
Программа должна вывести число, которое получится в результате разворота, указанного в условии задачи.
Число нужно выводить без незначащих нулей.
"""


str_num = input()
if len(str_num) == 5:
    str_num = str_num[-1::-1]
elif len(str_num) == 6:
    str_num = str_num[0] + str_num[-1:0:-1]
