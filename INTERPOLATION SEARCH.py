import random
import time

def interpolation_search(arr, x):
    low, high = 0, len(arr) - 1
    while low <= high and x >= arr[low] and x <= arr[high]:
        pos = low + ((x - arr[low]) * (high - low)) // (arr[high] - arr[low])
        if arr[pos] == x:
            return pos
        if arr[pos] < x:
            low = pos + 1
        else:
            high = pos - 1
    return -1

# Test with uniformly distributed data
def test_interpolation_search(n, x):
    data = sorted([random.randint(0, 100000) for _ in range(n)])
    start_time = time.time()
    interpolation_search(data, x)
    end_time = time.time()
    return end_time - start_time

# Test scalability
sizes = [1000, 5000, 10000, 50000, 100000]
for size in sizes:
    # Search for a random value in the array
    x = random.randint(0, 100000)
    time_taken = test_interpolation_search(size, x)
    print(f"Interpolation Search time for size {size}: {time_taken} seconds")
