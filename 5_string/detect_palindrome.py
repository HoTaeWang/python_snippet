# A palindrome is a word that reads the same backward as forward.
def is_palindrome(word):
    if word.lower() == word[::-1].lower():
        return True
    else:
        return False
    
# Test cases
print(is_palindrome('racecar')) # True
print(is_palindrome('hello')) # False
print(is_palindrome('Able was I ere I saw Elba')) # True
print(is_palindrome('Hannah')) # True
print(is_palindrome('Madam')) # True

