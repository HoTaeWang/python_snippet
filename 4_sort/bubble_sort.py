def bubble_sort(sorted_list):
    length = len(sorted_list) -1
    for i in range(length):
        swapped = False
        for j in range(length -i):
            if sorted_list[j] > sorted_list[j+1]:
                sorted_list[j], sorted_list[j+1] = sorted_list[j+1], sorted_list[j]
                swapped = True
        if not swapped:
            break   # if no swap happened in the inner loop, the list is already sorted
    return sorted_list

       