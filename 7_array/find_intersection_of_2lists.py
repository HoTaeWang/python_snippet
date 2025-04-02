this_weeks_winners = [2, 43, 48, 62, 64, 28, 3, 41]
most_common_winners = [1, 28, 42, 70, 2, 10, 62, 31, 4, 14]

# Method 1: Using list comprehension    
def return_intersection(list1, list2):
    intersection = [v for v in list1 if v in list2]
    return intersection

# Method 2: Using set intersection
def return_interset(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    intersection = list(set1.intersection(set2))
    return intersection

list1 = [2, 43, 48, 62, 64, 28, 3]
list2 = [1, 28, 42, 70, 2, 10, 62, 31, 4, 14]
print("intersection = ", return_intersection(list1, list2))
# Output: [2, 28, 62]
print("interset =", return_interset(list1, list2))