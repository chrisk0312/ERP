import time
import random

# Generate an array of 100 random integers
arr = [random.randint(1, 1000) for _ in range(100)]


# Measure the execution time
start_time = time.time()

# Sorting the array using Selection Sort
n = len(arr)
for i in range(n-1):
    min_index = i
    for j in range(i+1, n):
        if arr[min_index] > arr[j]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]

# Measure the execution time
end_time = time.time()

# Print the sorted array
print("Sorted array:", arr)

# Print the execution time
print("Execution time:", end_time - start_time, "seconds")




