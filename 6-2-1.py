"""
Вершина параболы

Уравнение параболы имеет вид y =ax2+bx+cy =ax^2 + bx + cy =ax2+bx+c, где a≠0a \neq 0a=0. Напишите программу, которая по
 введенным значениям a,b,ca, b, ca,b,c определяет и выводит вершину параболы.

Формат входных данных
На вход программе подаются три целых числа, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести координаты вершины параболы.

Примечание. Координаты вершины параболы y=ax2+bx+cy=ax^2+bx+cy=ax2+bx+c имеют вид
(−b2a; 4ac−b24a)\left(-\dfrac{b}{2a}; \, \dfrac{4ac-b^2}{4a}\right)(−2ab​;4a4ac−b2​).
Тестовые данные 🟢

Sample Input 1:

-2
6
1

Sample Output 1:

(1.5, 5.5)
"""


def main():
    a, b, c = int(input()), int(input()), int(input())
    vertex = get_vertex(a, b, c)
    print(vertex)


def get_vertex(a, b, c):
    x = -b / (2 * a)
    y = (4 * a * c - b ** 2)/(4 * a)
    vertex = (x, y)
    return vertex


main()
