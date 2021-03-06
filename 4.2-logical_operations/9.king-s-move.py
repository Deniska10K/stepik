"""
Даны две различные клетки шахматной доски. Напишите программу,  которая определяет, может ли король попасть с первой
клетки на вторую одним ходом. Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца и номер
строки сначала для первой клетки, потом для второй клетки. Программа должна вывести «YES», если из первой клетки ходом
короля можно попасть во вторую, или «NO» в противном случае.

Формат входных данных
На вход программе подаётся четыре числа от 1 до 8.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Примечание. Шахматный король ходит по горизонтали, вертикали и диагонали, но только на 1 клетку.
"""

king_coords, point_coords = [int(input()) for _ in range(2)], [int(input()) for _ in range(2)]
print("YES" if (point_coords[0] in range(king_coords[0] - 1, king_coords[0] + 2)) and
      (point_coords[1] in range(king_coords[1] - 1, king_coords[1] + 2)) else "NO")
