"""
    Заполнение 4

На вход программе подается натуральное число nnn. Напишите программу, которая создает матрицу размером n×n заполнив её
в соответствии с образцом.

Формат входных данных
На вход программе подается натуральное число nnn — количество строк и столбцов в матрице.

Формат выходных данных
Программа должна вывести указанную матрицу в соответствии с образцом.

Примечание. Для вывода элементов матрицы как в примерах, отводите ровно 333 символа на каждый элемент. Для этого
используйте строковый метод ljust(). Можно обойтись и без ljust(), система примет и такое решение 😇
Тестовые данные 🟢

Sample Input 1:

5

Sample Output 1:

1  1  1  1  1
0  1  1  1  0
0  0  1  0  0
0  1  1  1  0
1  1  1  1  1
"""


def fill_matrix(n):
    matrix = []
    for r in range(n):
        nums = []
        for c in range(n):
            if r == c or n == r + c + 1 \
                    or (r < c and r < n - 1 - c) \
                    or (r > c and r > n - 1 - c):
                nums.append(1)
            else:
                nums.append(0)
        matrix.append(nums)

    return matrix


def main():
    size_of_matrix = int(input())
    matrix = fill_matrix(size_of_matrix)

    for row in matrix:
        for num in row:
            print(str(num).ljust(3), end='')
        print()


main()
