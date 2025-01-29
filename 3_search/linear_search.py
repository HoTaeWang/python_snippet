def linear_search(arr_list, n):
    for i in arr_list:
        if i == n:
            return True
    return False


arr_list = [18, 1, 32, 91, 5, 15, 9, 100, 3]
print(linear_search(arr_list, 91))
print(linear_search(arr_list, 10000))
