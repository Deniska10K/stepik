"""
Даны две различные клетки шахматной доски. Напишите программу, которая определяет, может ли ладья попасть с первой
клетки на вторую одним ходом. Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца и номер
строки сначала для первой клетки, потом для второй клетки. Программа должна вывести «YES», если из первой клетки ходом
ладьи можно попасть во вторую, или «NO» в противном случае.

Формат входных данных
На вход программе подаётся четыре числа от 1 до 8.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Примечание. Шахматная ладья ходит по горизонтали или вертикали.
"""

rock_coords, point_coords = [input() for _ in range(2)], [input() for _ in range(2)]
print("YES" if (rock_coords[0] == point_coords[0]) or (rock_coords[1] == point_coords[1]) else "NO")
