import random
import time

def Advanced_BubbleSort(A):
    n = len(A)
    for i in range(n-1):
        sorted = True
        for j in range(0, n-i-1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
                sorted = False
        if sorted:
            break
    return A

array = [random.randint(1, 100) for _ in range(100)]
start_time = time.time()
sorted_array = Advanced_BubbleSort(array)
end_time = time.time()
time_taken = end_time - start_time
print(f"버블정렬: {sorted_array}")
print(f"소요시간: {time_taken}초")
