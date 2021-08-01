"""
Даны три вещественных числа a, b, c. Напишите программу, которая находит вещественные корни квадратного уравнения
ax^2 + bx + c = 0.

На вход программе подается три вещественных числа a≠0, b, c, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести вещественные корни уравнения если они существуют или текст «Нет корней» в противном случае.

Примечание. Если уравнение имеет два корня, то следует вывести их в порядке возрастания.
"""

a, b, c = (float(input()) for _ in range(3))

discriminant = b ** 2 - 4 * a * c
if discriminant > 0:
    equations_root_1 = (-b - discriminant ** .5) / (2 * a)
    equations_root_2 = (-b + discriminant ** .5) / (2 * a)
    print(f"{min(equations_root_1, equations_root_2)}\n{max(equations_root_1, equations_root_2)}")
elif discriminant == 0:
    equations_root_1 = -b / (2 * a)
    print(f"{equations_root_1}")
else:
    print(f"Нет корней")
