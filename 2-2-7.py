'''
Тимур и Руслан пытаются разделить фронт работы по курсу "Python для профессионалов". Для этого они решили сыграть в камень, ножницы и бумагу. Помогите ребятам бросить честный жребий и определить, кто будет делать очередной модуль нового курса.

Формат входных данных
На вход программе подаются две строки текста, содержащие слова "камень", "ножницы" или "бумага".
На первой строке записан выбор Тимура, на второй – выбор Руслана.

Формат выходных данных
Программа должна вывести результат жеребьёвки, то есть кто победит: Тимур, Руслан или же они сыграют вничью.

Примечание. Правила игры стандартные: камень побеждает ножницы, но проигрывает бумаге, а ножницы побеждают бумагу.
'''

tim_choice, rus_choice = input(), input()
stone, scissors, paper = 'камень', 'ножницы', 'бумага'

if (tim_choice == paper and rus_choice == stone) or \
        (tim_choice == stone and rus_choice == scissors) or \
        (tim_choice == scissors and rus_choice == paper):
    print('Тимур')
elif tim_choice == rus_choice:
    print('ничья')
else:
    print('Руслан')