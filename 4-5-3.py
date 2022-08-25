'''
Обмен столбцов

Напишите программу, которая меняет местами столбцы в матрице.

Формат входных данных
На вход программе на разных строках подаются два натуральных числа nnn и mmm — количество строк и столбцов в матрице, затем элементы матрицы построчно через пробел, затем числа iii и jjj — номера столбцов, подлежащих обмену.

Формат выходных данных
Программа должна вывести указанную таблицу с замененными столбцами.
Тестовые данные 🟢

Sample Input 1:

3
4
11 12 13 14
21 22 23 24
31 32 33 34
0 1

Sample Output 1:

12 11 13 14
22 21 23 24
32 31 33 34
'''

def cols_changer(size_n, size_m):
#matrix burn
    matrix = []
    for strings in range(size_n):
        tmp_str = [int(element) for element in input().split()]
        matrix.append(tmp_str)
#matrix flip
    m_flip = []
    for col in range(size_m):
        tmp = []
        for row in range(size_n):
            tmp.append(matrix[row][col])
        m_flip.append(tmp)
#matrix change
    str_n = input().split(' ')
    n_col_1, n_col_2 = int(str_n[0]), int(str_n[1])
    if n_col_1 < n_col_2:
        m_flip[n_col_1], m_flip[n_col_2] = m_flip[n_col_2], m_flip[n_col_1]
    else:
        m_flip[n_col_2], m_flip[n_col_1] = m_flip[n_col_1], m_flip[n_col_2]
#matrix back-flip & output
    for col in range(size_n):
        result = []
        for row in range(size_m):
            result.append(m_flip[row][col])
        print(*result)


size_n, size_m = int(input()), int(input())
cols_changer(size_n, size_m)
