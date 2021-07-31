"""
Даны две различные клетки шахматной доски. Напишите программу,  которая определяет, может ли конь попасть с первой
клетки на вторую одним ходом. Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца и номер
строки сначала для первой клетки, потом для второй клетки. Программа должна вывести «YES», если из первой клетки ходом
коня можно попасть во вторую или «NO» в противном случае.

Формат входных данных
На вход программе подаётся четыре числа от 1 до 8.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Примечание. Шахматный конь ходит буквой «Г».
"""

horse_coords = [int(input()) for _ in range(2)]
point_coords = [int(input()) for _ in range(2)]

delta1, delta2 = abs(point_coords[0] - horse_coords[0]), abs(point_coords[1] - horse_coords[1])

if ((delta1 == 1) and (delta2 == 2)) or ((delta1 == 2) and (delta2 == 1)):
    print("YES")
else:
    print("NO")
