"""
Напишите программу, которая считывает целое положительное число x и выводит на экран последовательность чисел x, 2x, 3x,
4x и 5x, разделённых тремя черточками.

Формат входных данных
На вход программе подаётся целое положительное число.

Формат выходных данных
Программа должна вывести текст согласно условию задачи.
"""

num = int(input())
print('---'.join([str(num * i) for i in range(1, 6)]))
