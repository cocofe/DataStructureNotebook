# -*- coding: UTF-8 -*-


def insert_sort(array):
    n = len(array)
    if n < 2:
        return array
    for i in range(1,n):
        index = i - 1  # 待插入位置
        tmp = array[i]  # 待插入数字
        while index >= 0 and tmp < array[index]:
            array[index+1] = array[index]  # index所在的值向后移动一位
            index -= 1
        array[index+1] = tmp  # 将待插入数字插入到正确位置, 保证已排序数据有序
    return array