'''Задача Иосифа Флавия 🌶️🌶️

nnn человек, пронумерованных числами от 111 до nnn, стоят в кругу. Они начинают считаться, каждый kkk-й по счету человек выбывает из круга, после чего счет продолжается со следующего за ним человека. Напишите программу, определяющую номер человека, который останется в кругу последним.

Формат входных данных
На вход программе подаются два числа nnn и kkk, записанные на отдельных строках.

Формат выходных данных
Программа должна вывести одно число – номер человека, который останется в кругу последним.'''

n, k = int(input()), int(input())
cnt = 0

for i in range(1, n+1):
    cnt = (cnt + k) % i
print(cnt + 1)

'''
for i in range(1, n + 1):
    l.append(i)

def shiftDelIns(l, k):
    while len(l) != 1:
        for i in range(n-k):

            l.insert(0, l.pop())
            l.pop()
            #l.append('*')
    print(l)

shiftDelIns(l, k)
'''

