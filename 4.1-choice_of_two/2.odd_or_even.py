"""
Напишите программу, которая определяет, является число четным или нечетным.

Формат входных данных
На вход программе подаётся одно целое число.

Формат выходных данных
Программа должна вывести «Четное», если число четное, и «Нечетное» — если число нечетное.
"""

print("Четное" if int(input()) % 2 == 0 else "Нечетное")