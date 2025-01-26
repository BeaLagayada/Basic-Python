def enhanced_radix_sort(arr):
    """
    Enhanced Radix Sort with optimized space complexity and execution time.

    Parameters:
        arr (list): List of non-negative integers to sort.

    Returns:
        list: Sorted list of integers.
    """
    if len(arr) == 0:
        return arr

    # Find the maximum number to determine the number of digits
    max_num = max(arr)

    # Determine the number of significant digits
    exp = 1  # Start with the least significant digit

    # Perform Radix Sort using an optimized counting sort
    while max_num // exp > 0:
        arr = optimized_counting_sort(arr, exp)
        exp *= 10

    return arr


def optimized_counting_sort(arr, exp):
    """
    Optimized counting sort used in Radix Sort.

    Parameters:
        arr (list): List of integers to sort based on the current digit.
        exp (int): Current digit's place (1, 10, 100, etc.).

    Returns:
        list: Partially sorted list of integers.
    """
    n = len(arr)
    count = [0] * 10  # Only 10 digits (0-9)
    output = [0] * n  # Output array

    # Count occurrences of each digit
    for num in arr:
        index = (num // exp) % 10
        count[index] += 1

    # Convert counts to positions
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array in reverse order to maintain stability
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    # Copy the output array back to the original array
    return output


# Test the Enhanced Radix Sort
if _name_ == "_main_":
    import time

    data = [170, 45, 75, 90, 802, 24, 2, 66, 12345, 54321, 987, 321]
    print("Original array:", data)

    start = time.time()
    sorted_data = enhanced_radix_sort(data)
    end = time.time()

    print("Sorted array:", sorted_data)
    print(f"Execution time: {end - start:.6f} seconds")