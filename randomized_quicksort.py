import random
import time
import sys

# Safely increase recursion limit for large lists
sys.setrecursionlimit(10000)

def randomized_quicksort(arr):
    """Efficient Randomized Quicksort using recursive divide-and-conquer."""
    if len(arr) <= 1:
        return arr
    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]

    # Partitioning while skipping the pivot
    less = [x for i, x in enumerate(arr) if x < pivot or (x == pivot and i != pivot_index)]
    greater = [x for x in arr if x > pivot]

    return randomized_quicksort(less) + [pivot] + randomized_quicksort(greater)


def deterministic_quicksort_iterative(arr):
    """Iterative version of deterministic quicksort (first element as pivot)."""
    if len(arr) <= 1:
        return arr

    stack = [(0, len(arr) - 1)]
    while stack:
        start, end = stack.pop()
        if start >= end:
            continue

        # Use the first element as pivot
        pivot = arr[start]
        low = start + 1
        high = end

        while True:
            while low <= high and arr[high] >= pivot:
                high -= 1
            while low <= high and arr[low] <= pivot:
                low += 1
            if low <= high:
                arr[low], arr[high] = arr[high], arr[low]
            else:
                break

        arr[start], arr[high] = arr[high], arr[start]
        stack.append((start, high - 1))
        stack.append((high + 1, end))
    return arr


def test_quicksort_performance():
    """Compare Randomized vs Deterministic Quicksort empirically."""
    sizes = [1000, 5000, 10000, 20000]
    input_types = ['random', 'sorted', 'reversed', 'repeated']

    for size in sizes:
        for input_type in input_types:
            if input_type == 'random':
                arr = [random.randint(0, size) for _ in range(size)]
            elif input_type == 'sorted':
                arr = list(range(size))
            elif input_type == 'reversed':
                arr = list(range(size, 0, -1))
            elif input_type == 'repeated':
                arr = [random.choice([1, 2, 3]) for _ in range(size)]

            arr_copy = arr[:]

            start = time.time()
            randomized_quicksort(arr)
            rand_duration = time.time() - start

            start = time.time()
            deterministic_quicksort_iterative(arr_copy)
            det_duration = time.time() - start

            print(f"Size: {size:5}, Type: {input_type:9}, "
                  f"Randomized: {rand_duration:.5f}s, "
                  f"Deterministic: {det_duration:.5f}s")

if __name__ == "__main__":
    test_quicksort_performance()
