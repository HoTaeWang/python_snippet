# Two strings are anagrams if they contain the same letters.
def is_anagram(s1, s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()
    if sorted(s1) == sorted(s2):
        return True
    else:
        return False
    
# Test cases
print(is_anagram('listen', 'silent')) # True
print(is_anagram('triangle', 'integral')) # True
print(is_anagram('hello', 'world')) # False
print(is_anagram('Emperor Octavian', 'Captain over Rome')) # True

