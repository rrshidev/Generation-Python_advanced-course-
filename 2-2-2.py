"""
Формат входных данных
На вход программе подается строка текста из разделенных пробелами натуральных чисел.

Формат выходных данных
Программа должна вывести одно число – количество элементов списка, больших предыдущего.

"""
nums = [int(num) for num in input().split()]

cnt = 0
prev = float('inf')
for num in nums:
    if num > prev:
        cnt += 1
    prev = num
print(cnt)
