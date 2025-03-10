def move_zeros(arr):
    zero_index = 0
    for index, n in enumerate(arr):
        print(index, n)
        if n != 0:
            print("index = ", index, "zero_index = ", zero_index, "n = ", n)
            arr[zero_index] = n
            if zero_index != index:
                arr[index] = 0
            zero_index += 1
    return arr
            
arr = [8, 0, 3, 0, 12]
move_zeros(arr)
print(arr)

#arr = [0, 1, 0, 3, 12]
#move_zeros(arr)
#print(arr)



