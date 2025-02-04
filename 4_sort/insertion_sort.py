def insertion_sort(arr_list):
    for i in range(1, len(arr_list)):
        key = arr_list[i]
        while i > 0 and key < arr_list[i-1]:
            arr_list[i] = arr_list[i-1]
            i -= 1
        arr_list[i] = key
    return arr_list


