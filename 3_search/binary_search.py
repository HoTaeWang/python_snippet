from bisect import bisect_left

# Theory of Binary Search
def binary_search(arr_list, n):
    first = 0
    last = len(arr_list) -1
    while last >= first:
        mid = (first + last)  // 2
        if arr_list[mid] == n:
            return True
        else:
            if n < arr_list[mid]:
                last = mid -1
            else:
                first = mid + 1
    return False

# Using bisect_left for real-world application
def b_search(arr_list, n):
    index = bisect_left(arr_list, n)
    if index != len(arr_list) and arr_list[index] == n:
        return True
    return False

sorted_fruits = ['apple', 'banana', 'cherry', 'date', 'fig']

print(binary_search(sorted_fruits, 'banana')) # True
print(binary_search(sorted_fruits, 'mango')) # False

print(b_search(sorted_fruits, 'cherry')) # True
print(b_search(sorted_fruits, 'mango')) # False
