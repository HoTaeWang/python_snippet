import math

print(math.gcd(20, 12))

def gcf(a, b):
    gcf = None
    if a > b:
        smaller = b
    else:
        smaller = a
    for i in range(1, smaller + 1):
        if a % i == 0 and b % i == 0:
            gcf = i
    return gcf

print(gcf(20, 12))
print(gcf(12, 20))
print(gcf(20, 30))
print(gcf(30, 20))
print(gcf(20, 20))
print(gcf(20, 1))
print(gcf(1, 20))