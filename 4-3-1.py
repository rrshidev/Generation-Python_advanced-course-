'''
На вход программе подается число nnn. Напишите программу, которая создает и выводит построчно список, состоящий из nnn списков [[1, 2, ..., n], [1, 2, ..., n], ..., [1, 2, ..., n]].

Формат входных данных
На вход программе подается натуральное число nnn.

Формат выходных данных
Программа должна вывести построчно указанный список.
'''

def list_str(n):
    lString = []
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            lString.append(j)
        print(lString)
        lString = []

num_str = int(input())

list_str(num_str)