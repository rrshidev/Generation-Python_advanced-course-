'''
Симметричная матрица

Напишите программу, которая проверяет симметричность квадратной матрицы относительно главной диагонали.

Формат входных данных
На вход программе подаётся натуральное число nnn — количество строк и столбцов в матрице, затем элементы матрицы построчно через пробел.

Формат выходных данных
Программа должна вывести YES, если матрица симметрична относительно главной диагонали, и слово NO в противном случае.
Тестовые данные 🟢

Sample Input 1:

3
0 1 2
1 2 3
2 3 4

Sample Output 1:

YES


'''

def is_simmetry(S_M_S):
    matrix = []
    for row in range(S_M_S):
        temp = [int(element) for element in input().split()]
        matrix.append(temp)
    s_matrix = []
    for c in range(S_M_S):
        tmp_str = []
        for r in range(S_M_S):
            tmp_str.append(matrix[r][c])
        s_matrix.append(tmp_str)
    if matrix == s_matrix:
        print('YES')
    else:
        print('NO')


square_matrix_size = int(input()) #shortly name of it value - SMS =)
is_simmetry(square_matrix_size)