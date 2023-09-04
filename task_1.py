# Напишите функцию для транспонирования матрицы

def transposed_matrix_1(matrix: list) -> list:
    '''Транспонирование матрицы: Вариант 1''' 
    t_matrix = []
    for i in range(len(matrix[0])):
        new_list = []
        for row in matrix:
            new_list.append(row[i])
        t_matrix.append(new_list)
    return t_matrix


def transposed_matrix_2(matrix: list) -> list:
    '''Транспонирование матрицы: Вариант 2''' 
    return [list(elem) for elem in zip(*matrix)]


data = [[1,2], [3,4], [5,6]]
print(transposed_matrix_1(data))
print(transposed_matrix_2(data))