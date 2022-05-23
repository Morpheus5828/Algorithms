def bullet_tris(lists):
    n = len(lists)
    for i in range(n, 1, -1):
        for j in range(0, n - 1):
            if lists[j] > lists[j + 1]:
                swap(lists, j, j + 1)

    return lists


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


def swap(lists, j, j_plus_un):
    tmp = lists[j_plus_un]
    lists[j_plus_un] = lists[j]
    lists[j] = tmp


numbers = [13, -2, -5, 6, 8, 0]
print(insertion(numbers))
