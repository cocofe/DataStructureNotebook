# -*- coding: UTF-8 -*-
# 归并排序


def merge_sort(array):
    # 递归拆分数组
    if len(array) <= 1:
        return array
    num = len(array) // 2
    left = merge_sort(array[:num])
    right = merge_sort(array[num:])
    return merge(left, right)


def merge(left, right):
    # 合并数组
    lp = rp = 0
    ret = []
    while lp < len(left) and rp < len(right):
        if left[lp] < right[rp]:
            ret.append(left[lp])
            lp += 1
        else:
            ret.append(right[rp])
            rp += 1
    ret += left[lp:]
    ret += right[rp:]
    return ret
