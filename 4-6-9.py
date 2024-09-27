"""
Заполнение диагоналями 🌶️

На вход программе подаются два натуральных числа nnn и mmm. Напишите программу, которая создает матрицу размером n×mn \times mn×m заполнив её "диагоналями" в соответствии с образцом.

Формат входных данных
На вход программе на одной строке подаются два натуральных числа nnn и mmm — количество строк и столбцов в матрице.

Формат выходных данных
Программа должна вывести указанную матрицу в соответствии с образцом.

Примечание. Для вывода элементов матрицы как в примерах, отводите ровно 333 символа на каждый элемент. Для этого используйте строковый метод ljust(). Можно обойтись и без ljust(), система примет и такое решение 😇
Тестовые данные 🟢

Sample Input 1:

3 5

Sample Output 1:

1  2  4  7  10
3  5  8  11 13
6  9  12 14 15
"""


def fill_matrix(n_size, m_size, source_nums):
    matrix = []
    cnt = 0
    for sum in source_nums:
        for r in range(n_size):
            cnt += 1
            nums = []
            for c in range(m_size):
                if r + c == sum:
                    nums.append(cnt)
        matrix.append(nums)
    return matrix


def main():
    in_nums = [int(num) for num in input().split()]
    n, m = in_nums[0], in_nums[1]
    matrix_nums = [int(num) for num in range(n + m + 1)]
    matrix = fill_matrix(n, m, matrix_nums)
    for row in matrix:
        print(*row)
    print(matrix_nums)


main()
