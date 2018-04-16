# -*- coding: UTF-8 -*-


# 希尔排序
def shell_sort(array):
    n = len(array)
    gap = n // 2
    while gap > 0:
        for i in range(n):
            if i+gap < n:
                tmp = array[i+gap]  # 待插入元素
                index = i + gap  # 待插入位置
                while index - gap >= 0 and tmp < array[index - gap]:
                    array[index] = array[index - gap]
                    index -= gap
                array[index] = tmp
        gap = gap // 2
    return array