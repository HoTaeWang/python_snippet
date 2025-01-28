def streak_numbers(n):
    if n == 0:
        return
    streak_numbers(n-1)
    print(n)

# Test
streak_numbers(10)
