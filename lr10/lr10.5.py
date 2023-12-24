import time


def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1


def insertion_sort(alist):
    for i in range(1, len(alist)):
        temp = alist[i]
        j = i - 1
        while j >= 0 and temp < alist[j]:
            alist[j + 1] = alist[j]
            j = j - 1
        alist[j + 1] = temp


def measure_sorting_time(algorithm, size):
    arr = [i for i in range(size, 0, -1)]
    start_time = time.time()
    algorithm(arr)
    end_time = time.time()
    execution_time = (end_time - start_time) * 1000
    return execution_time


arr_sizes = [10, 1000, 2000, 3000, 4000, 5000, 10000]

print(f"{'Size':<10} {'Merge Sort':<16} {'Insertion Sort':<16}")

for size in arr_sizes:
    merge_sort_time = measure_sorting_time(merge_sort, size)
    insertion_sort_time = measure_sorting_time(insertion_sort, size)

    print(f"{size:<10} {merge_sort_time:<16.1f} {insertion_sort_time:<16.1f}")
