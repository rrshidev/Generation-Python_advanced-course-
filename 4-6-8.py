"""
Заполнение змейкой

На вход программе подаются два натуральных числа n и m. Напишите программу, которая создает матрицу размером n×m,
заполнив её "змейкой" в соответствии с образцом.

Формат входных данных
На вход программе на одной строке подаются два натуральных числа nnn и mmm — количество строк и столбцов в матрице.

Формат выходных данных
Программа должна вывести указанную матрицу в соответствии с образцом.

Примечание. Для вывода элементов матрицы как в примерах, отводите ровно 333 символа на каждый элемент.
Для этого используйте строковый метод ljust(). Можно обойтись и без ljust(), система примет и такое решение 😇
Тестовые данные 🟢

Sample Input 1:

3 5

Sample Output 1:

1  2  3  4  5
10 9  8  7  6
11 12 13 14 15
"""


def fill_matrix(n_size, m_size, source_nums):
    matrix = []
    for r in range(n_size):
        row_nums = []
        for c in range(m_size):
            if r % 2 == 0:
                row_nums.append(str(source_nums[c]))
            else:
                row_nums.insert(0, str(source_nums[c]))
        source_nums = source_nums[c + 1 : ]
        matrix.append(row_nums)
    return matrix


def main():
    in_nums = [int(num) for num in input().split()]
    n, m = in_nums[0], in_nums[1]
    matrix_nums = [int(num) for num in range(1, n * m + 1)]
    matrix = fill_matrix(n, m, matrix_nums)
    for row in range(n):
        for col in range(m):
            print(*matrix[row][col].ljust(3), end='')
        print()


main()
