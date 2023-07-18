# -*- coding: utf-8 -*-
# @Time    : 2023/7/17 13:47
# @Author  : wzh
# @Email   : 644713101@qq.com
# @File    : 01.quick_sort.py

def partition(arr, low, high):
    i = (low - 1)  # 记录最后一个移动的点
    pivot = arr[high]  # 哨兵，与这个相比，比这个数小的挪过去
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]  # 把哨兵挪过去
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)


arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quick_sort(arr, 0, n-1)
print("排序后的数组:")
for i in range(n):
    print("%d" %arr[i])




