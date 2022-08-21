'''
Больше среднего

Напишите программу, которая выводит количество элементов квадратной матрицы в каждой строке, больших среднего арифметического элементов данной строки.

Формат входных данных
На вход программе подаётся натуральное число nnn — количество строк и столбцов в матрице, затем элементы матрицы (целые числа) построчно через пробел.

Формат выходных данных
Программа должна вывести nnn чисел — для каждой строки количество элементов матрицы, больших среднего арифметического элементов данной строки.
Тестовые данные 🟢

Sample Input 1:

4
1 2 3 4
5 6 3 15
0 2 3 1
5 2 8 5

Sample Output 1:

2
1
2
1
'''

def above_average(m_size):
    matrix = []
    result = 0
    for elem in range(m_size):
        temp = [int(num) for num in input().split()]
        matrix.append(temp)
    for row in matrix:
        for elem in row:
            if elem > sum(row)/m_size:
                result += 1
        print(result)
        result = 0


matrix_size = int(input())
above_average(matrix_size)
