'''
Произведение чисел

Напишите программу для определения, является ли число произведением двух чисел из данного набора, выводящую результат в виде ответа «ДА» или «НЕТ».

Формат входных данных
В первой строке подаётся число n (0<n<1000)n\, (0 < n < 1000)n(0<n<1000) – количество чисел в наборе. В последующих nnn строках вводятся целые числа, составляющие набор (могут повторяться). Затем следует целое число, которое является или не является произведением двух каких-то чисел из набора.

Формат выходных данных
Программа должна вывести «ДА» или «НЕТ» в соответствии с условием задачи.

Примечание 1. Само на себя число из набора умножиться не может, другими словами, два множителя должны иметь разные индексы в наборе.

Примечание 2. Для решения задачи используйте вложенные циклы.
'''

n = int(input())
stringInputList = [input() for i in range(0, n)]
mul = int(input())


def multi_check():
    result = 'НЕТ'
    for i in range(n):
        x = int(stringInputList[i])
        for j in range(n):
            y = int(stringInputList[j])
            if i != j:
                if x * y == mul:
                    result = 'ДА'
                    return result
    return result

print(multi_check())

