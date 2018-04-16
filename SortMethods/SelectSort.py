# -*- coding: UTF-8 -*-


def select_sort(array):
    n = len(array)
    for sorted_index in range(n-1):  # sorted_index 为下一个最小值插入的位置
        min_index = sorted_index  # 最小元素索引
        for j in range(sorted_index+1, n):
            if array[min_index] > array[j]:
                min_index = j
        array[sorted_index], array[min_index] = array[min_index], array[sorted_index]  # 将原先位置元素与最小值交换
    return array