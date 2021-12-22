#!/usr/bin/env python3
from typing import List


def optimized_bubble_sort(array: list) -> List:
    """Optimized Bubble sort
    Best case scenario where the array is already sorted
    By adding swapped variable, we prevent execution of all other iterations

    :param array:
    :return:
    """
    for i in range(0, len(array)):
        # set to false,to verify if the array at any point is fully sorted
        swapped = False
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
                swapped = True
        if not swapped:
            break


def bubble_sort(array: list) -> List:
    """Bubble sort algorithm


    :param array:
    :return:
    """

    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp


array = [-2, 45, 0, 11, -9]
array_sorted = [-2, 45, 0, 11, -9] # should be sorted by optimized BS
print(f"Original array:{array}")
bubble_sort(array=array)
print(f"[BS]Sorted array:{array}")
optimized_bubble_sort(array=array_sorted)
print(f"[OptimizedBS]Sorted array:{array_sorted}")




