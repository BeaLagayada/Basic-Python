import pandas as pd
import time
import sys

# Load dataset from CSV file
df = pd.read_csv('data1.csv')

# Display the entire dataset
print("Dataset Loaded:")
print(df.to_string(index=False))

# Extract the columns for sorting and searching
names = df[df.columns[0]].tolist()  # Assume first column contains names
ages = df[df.columns[1]].tolist()  # Assume second column contains ages

def radix_sort_with_names(arr, names):
    max_num = max(arr)
    exp = 1  # Start with the least significant digit
    while max_num // exp > 0:
        counting_sort_with_names(arr, names, exp)
        exp *= 10

def counting_sort_with_names(arr, names, exp):
    n = len(arr)
    output = [0] * n
    name_output = [""] * n
    count = [0] * 10  # Radix base is 10

    # Count occurrences
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    # Update count array to store cumulative positions
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build output arrays
    for i in reversed(range(n)):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        name_output[count[index] - 1] = names[i]
        count[index] -= 1

    # Copy output to the original arrays
    for i in range(n):
        arr[i] = output[i]
        names[i] = name_output[i]

def interpolation_search(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high and x >= arr[low] and x <= arr[high]:
        if arr[high] == arr[low]:
            if arr[low] == x:
                return low
            break

        # Estimate position
        pos = low + ((x - arr[low]) * (high - low) // (arr[high] - arr[low]))

        if pos < 0 or pos >= len(arr):
            break

        if arr[pos] == x:
            return pos
        elif arr[pos] < x:
            low = pos + 1
        else:
            high = pos - 1

    return -1  # Element not found

# Clone datasets for testing
ages_copy = ages[:]
names_copy = names[:]

# Print unsorted dataset
print("Unsorted Data:")
print(list(zip(names[:10], ages[:10])), "...")  # Print first 10 entries as sample

# Time Radix Sort
start_time = time.time()
radix_sort_with_names(ages_copy, names_copy)
end_time = time.time()
print(f"Radix Sort Time: {end_time - start_time:.6f} seconds")

# Print sorted dataset
print("Sorted Data:")
print(list(zip(names_copy[:10], ages_copy[:10])), "...")  # Print first 10 entries as sample

# Check sorting accuracy
correct_positions = sum(1 for i, j in zip(ages_copy, sorted(ages)) if i == j)
accuracy_percentage = (correct_positions / len(ages)) * 100
print(f"Sorting Accuracy: {accuracy_percentage:.2f}%")

# Space Complexity
print(f"Memory Usage: {sys.getsizeof(ages_copy)} bytes")

# Time Interpolation Search
key = ages_copy[len(ages_copy) // 2]  # Use a middle value for searching
start_time = time.time()
result = interpolation_search(ages_copy, key)
end_time = time.time()
print(f"Interpolation Search Time: {end_time - start_time:.6f} seconds")
if result != -1:
    print(f"Key Found at Index: {result}, Name: {names_copy[result]}")
else:
    print("Key Not Found")
