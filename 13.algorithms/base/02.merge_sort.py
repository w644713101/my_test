
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    # 创建临时数组
    L = [0] * n1
    R = [0] * n2

    # 拷贝数据到临时数组 arrays L[] 和 R[]
    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    # 归并临时数组到 arr[l...r]
    i, j, k = 0, 0, l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # 拷贝L[]的保留元素
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # 拷贝R[]的保留元素
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def merge_sort(arr, l, r):
    if l < r:
        m = int((l + r -1) / 2)
        merge_sort(arr, l, m)
        merge_sort(arr, m + 1, r)
        merge(arr, l, m, r)


arr = [12, 11, 13, 5, 6, 7]
n = len(arr)
print('给定的数组')
for i in range(n):
    print('%d' % arr[i])

merge_sort(arr, 0, n-1)
print('排序后的数组')
for i in range(n):
    print('%d' % arr[i])







