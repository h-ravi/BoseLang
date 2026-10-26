import time


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    j = low
    while j < high:
        if arr[j] <= pivot:
            i += 1
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp
        j += 1
    tmp = arr[i + 1]
    arr[i + 1] = arr[high]
    arr[high] = tmp
    return i + 1


def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)


seed = 123456789
arr = []
for _ in range(2000):
    seed = (seed * 1103515245 + 12345) % 2147483648
    arr.append(seed % 100000)

start = time.perf_counter()

quicksort(arr, 0, len(arr) - 1)

end = time.perf_counter()

print("RESULT:", arr[1000])
print("TIME:", (end - start) * 1000.0)
