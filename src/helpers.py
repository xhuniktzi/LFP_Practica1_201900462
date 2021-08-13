from typing import List
from estudiante import Estudiante


def bubble_sort(array: List[Estudiante], reverse=False):
    cp_array = array.copy()

    n = len(cp_array)

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if not reverse:
                if cp_array[j].nota > cp_array[j + 1].nota:
                    cp_array[j], cp_array[j + 1] = cp_array[j + 1], cp_array[j]
            else:
                if cp_array[j].nota < cp_array[j + 1].nota:
                    cp_array[j], cp_array[j + 1] = cp_array[j + 1], cp_array[j]

    return cp_array
