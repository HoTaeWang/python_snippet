def bubble_sort(sorted_list):
    length = len(sorted_list) -1
    for i in range(length):
        for j in range(length -i):
            if sorted_list[j] > sorted_list[j+1]:
                sorted_list[j], sorted_list[j+1] = sorted_list[j+1], sorted_list[j]
    return sorted_list

list = [64, 34, 25, 12, 22, 11, 90]
print('length = ', len(list))
print(bubble_sort(list))

        