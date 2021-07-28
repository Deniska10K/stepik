"""
Напишите программу, в которой рассчитывается сумма и произведение цифр положительного трёхзначного числа.

Формат входных данных
На вход программе подаётся положительное трёхзначное число.

Формат выходных данных
Программа должна вывести два числа с поясняющим текстом: сумма цифр и произведение цифр.
"""

from functools import reduce
digit = input()
print(f"Сумма цифр = {sum(map(int, digit))}\n"
      f"Произведение цифр = {reduce(lambda a, b: a * b, list(map(int, (i for i in digit))))}")
