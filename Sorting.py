def bullet_tris(lists):
    n = len(lists)
    for i in range(n, 1, -1):
        for j in range(0, n - 1):
            if lists[j] > lists[j + 1]:
                swap(lists, j, j + 1)

    return lists


def swap(lists, j, j_plus_un):
    tmp = lists[j_plus_un]
    lists[j_plus_un] = lists[j]
    lists[j] = tmp


##########################################


def insertion(lists):
    n = len(lists)
    for i in range(1, n):
        key = lists[i]
        j = i - 1
        while (j >= 0) and (lists[j] > key):
            lists[j + 1] = lists[j]
            j -= 1
        lists[j + 1] = key
    return lists


##########################################


def quick(l, r, lists):
    # Terminate condition for recursion
    if len(lists) == 1:
        return lists
    if l < r:
        q = partition(l, r, lists)
        quick(l, q - 1, lists)
        quick(q + 1, r, lists)
    return lists


def partition(left, right, lists):
    pivot_value, ptr = lists[right], left
    for j in range(left, right):
        if lists[j] <= pivot_value:
            lists[j], lists[ptr] = lists[ptr], lists[j]
            ptr += 1
    lists[ptr], lists[right] = lists[right], lists[ptr]
    return ptr


##########################################

numbers = [13, -2, -5, 6, 8, 0]
print(quick(0, len(numbers) - 1, numbers))
