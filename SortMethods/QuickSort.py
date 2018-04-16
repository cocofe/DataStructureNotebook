# -*- coding: UTF-8 -*-


def quick_sort(array, left, right):
    if left >= right:
        return array
    key = array[left]
    lp, rp = left, right
    while lp < rp:
        while array[lp] < key and lp < rp:
            lp += 1
        while array[rp] > key and lp < rp:
            rp -= 1
        array[lp], array[rp] = array[rp], array[lp]
    quick_sort(array, left, lp)
    quick_sort(array, rp + 1, right)
    return array
