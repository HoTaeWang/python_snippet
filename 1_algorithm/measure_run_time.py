import time

start = time.time()
# Code to measure time 
for i in range(0, 10000):
    print(i)
end = time.time()

print("Time taken in seconds: ", end - start)
