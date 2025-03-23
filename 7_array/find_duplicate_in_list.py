def return_dups(iterable):
    dups = []
    a_set = set()

    for item in iterable:
        l1 = len(a_set)
        a_set.add(item)
        l2 = len(a_set)
        if l1 == l2:
            dups.append(item)
    return dups

a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9]
dups = return_dups(a_list)
print(dups)
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
# The return_dups() function takes an iterable and returns a list of duplicates in the iterable. It uses a set to keep track of the items that have been seen before, and if an item is already in the set, it is added to the list of duplicates. The function then returns the list of duplicates.