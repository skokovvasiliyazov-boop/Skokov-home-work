"""
Дана матрица n*m

пример:

2 3 4 5
2 4 3 5
4 3 4 2

Для каждой строки вывести:
- сумму всех значений в строке
- среднее арифметическое значение в строке
- максимальное значение
- индекс максимального значения
- минимальное значение
- индекс минимального
Тоже самое сделать для каждого столбца
Тоже самое сделать для всей таблицы (всех значений),
индекс максимального и минимального значения во всей таблице должен
содержать и номер строки и номер столбца
"""


# matrix = [[2,3,4,5],
#           [2,4,3,5],
#           [4,3,4,2]]

rows = int(input("Введите количество строк: " ))
cols = int(input("Введите количество столбцов: " ))

matrix = []

print("Вводите элементы построчно разделяя их пробелами: ")

for i in range(rows):
    row = list(map(int, input(f"Строка{i + 1}: ").split()))
    matrix.append(row)

    print("\n Созданная матрица: ")
    for row in matrix:
        print(row)

print("-сумма каждой строки")
rows_sum = [sum(row) for row in matrix]
print(f"-{rows_sum}")

print("-среднее арифметическое значение в строке")
average_value_rows = [sum(row) // cols for row in matrix]
print(f"-{average_value_rows}")

print("-максимальное значение в строке")
max_value_rows = [max(row) for row in matrix]
print(f"-{max_value_rows}")

print("-максимальный индекс в строке")
max_indices_row = [row.index(max(row)) for row in matrix ]
print(f"-{max_indices_row}")

print("-минимальный индекс в строке")
min_indices_row = [row.index(min(row)) for row in matrix ]
print(f"-{min_indices_row}")

print("-минимальное значение в строке")
min_value_rows = [min(row) for row in matrix]
print(f"-{min_value_rows}")

print("Расчёт для стлобцов")

print("-сумма каждого столбца")
cols_sum = [sum(cols) for cols in zip(*matrix)]
print(f"-{cols_sum}")

print("-среднее арифметическое значение в столбце")
average_value_rows = [sum(clos) // cols for clos in zip(*matrix)]
print(f"-{average_value_rows}")

print("-максимальное значение в столбце")
max_value_cols = [max(cols) for cols in zip(*matrix)]
print(f"-{max_value_cols}")

print("-максимальный индекс в столбце")
max_indices_cols = [cols.index(max(cols)) for cols in zip(*matrix)]
print(f"-{max_indices_cols}")

print("-минимальный индекс в столбце")
min_indices_cols = [cols.index(min(cols)) for cols in zip(*matrix)]
print(f"-{min_indices_cols}")

print("-минимальное значение в столбце")
min_value_cols = [min(row) for row in zip(*matrix)]
print(f"-{min_value_cols}")
