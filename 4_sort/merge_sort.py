def merge_sort(arr_list):
    if len(arr_list) > 1:
        mid = len(arr_list) // 2
        left_half = arr_list[:mid]
        right_half = arr_list[mid:]
        merge_sort(left_half)
        merge_sort(right_half)

        left_index = right_index = arr_index = 0
        while left_index < len(left_half) and right_index < len(right_half):
            if left_half[left_index] <= right_half[right_index]:
                arr_list[arr_index] = left_half[left_index]
                left_index += 1
            else:
                arr_list[arr_index] = right_half[right_index]
                right_index += 1
            arr_index += 1

        while left_index < len(left_half):
            arr_list[arr_index] = left_half[left_index]
            left_index += 1
            arr_index += 1

        while right_index < len(right_half):
            arr_list[arr_index] = right_half[right_index]
            right_index += 1
            arr_index += 1
        
    return arr_list

