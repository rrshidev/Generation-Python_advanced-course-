"""
Standard American Convention

На вход программе подаётся натуральное число. Напишите программу, которая вставляет в заданное число запятые в
соответствии со стандартным американским соглашением о запятых в больших числах.

Формат входных данных
На вход программе подаётся натуральное число n.

Формат выходных данных
Программа должна вывести число с запятыми в соответствии с условием задачи.
"""


num = int(input())
print('{0:,}'.format(num).replace(',', ','))