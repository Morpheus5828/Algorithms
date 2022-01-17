def bullet_tris(lists):
    n = len(lists)
    for i in range(n, 1, -1):
        for j in range(0, n-1):
            if lists[j] > lists[j + 1]:
                swap(list, j, j + 1)

    return lists


def swap(list, j, j_plus_un):
    tmp = list[j_plus_un]
    list[j_plus_un] = list[j]
    list[j] = tmp

