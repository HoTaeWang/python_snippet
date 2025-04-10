# Here is the syntax for a list comprehension
# new list = [expression for member in iterable (if conditional)]
# The if conditional is optional
# [expression(i) for i in iterable if filter(i) ]

print( [c for c in "selftaught"] )

s = "Buy 1 get 2 free"
nl = [c for c in s if c.isdigit()]
print(nl)

last_nl = [c for c in s if c.isdigit()][-1]
print(last_nl)

# list comprehension test
# [expression(i) for i in iterable if filter(i) ]
# [expression(i) for i in iterable]
# [expression for member in iterable (if conditional)]
# [expression for member in iterable]
# [expression for member in iterable if filter(member)]
# [expression for member in iterable if conditional]
test_list = ["selftaught", "code", "sit", "eat", "programming", "dinner",
"one", "two", "coding", "a", "tech"]
print([word for word in test_list if len(word) >= 4])