# -*- coding: UTF-8 -*-


def max_heapify(arr, start, end):
    """
    维护最大堆,本质上是从start向下遍历, 如果子节点大于父节点, 则父节点与子节点交换, 
    然后, 继续以该子节点为起点,向下调整
    """
    while start < end:
        left = start * 2 + 1
        right = start * 2 + 2
        if left < end and arr[left] > arr[start]:
            largest = left
        else:
            largest = start
        if right < end and arr[right] > arr[largest]:
            largest = right
        if largest != start:
            arr[largest], arr[start] = arr[start], arr[largest]
            start = largest
        else:
            break


def build_max_heap(arr):
    """构建初始最大堆, 只能确保首个元素为最大值"""
    length = len(arr)
    for x in range(length // 2 - 1, -1, -1):
        max_heapify(arr, x, length)


def heap_sort(arr):
    """利用最大堆实现升序排序, 每次取走一个根节点,可以获得当前堆中的最大值, 因此取n次即可得到有序序列"""
    length = len(arr)
    build_max_heap(arr)
    while length > 0:
        max_heapify(arr, 0, length)
        arr[0], arr[length - 1] = arr[length - 1], arr[0]
        length -= 1
    return arr
