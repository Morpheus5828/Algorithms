def sequential_research(lists, searching_value):
    list_size = len(lists)
    number_of_element = 0
    while (number_of_element < list_size - 1) and (lists[number_of_element] != searching_value):
        number_of_element += 1
    return lists[number_of_element] == searching_value


def other_sequential_research(lists, searching_value):
    for number_of_element in lists:
        if lists[number_of_element] == searching_value:
            return True
    return False

# O(3n)



