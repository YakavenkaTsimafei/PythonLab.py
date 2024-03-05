import random
import time
import threading
import matplotlib.pyplot as plt

def heapify(nums, heap_size, root_index):
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child

    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child

    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
        heapify(nums, heap_size, largest)

def heap_sort(nums):
    n = len(nums)

    for i in range(n, -1, -1):
        heapify(nums, n, i)

    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)

def merge(left_list, right_list):
    sorted_list = []
    left_list_index = right_list_index = 0

    left_list_length, right_list_length = len(left_list), len(right_list)

    for _ in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1
        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1

    return sorted_list

def merge_sort(nums):
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2
    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])

    return merge(left_list, right_list)

def partition(nums, low, high):
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1
        j -= 1
        while nums[j] > pivot:
            j -= 1
        if i >= j:
            return j
        nums[i], nums[j] = nums[j], nums[i]

def quick_sort(nums):
    def _quick_sort(items, low, high):
        if low < high:
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)
    _quick_sort(nums, 0, len(nums) - 1)

def measure_sorting_time(algorithm, nums):
    start_time = time.time()
    algorithm(nums)
    end_time = time.time()
    return end_time - start_time

def generate_random_list(length):
    return [random.randint(0, 1000) for _ in range(length)]

def sort_and_measure(algorithm, length, repetitions):
    times = []
    for _ in range(repetitions):
        nums = generate_random_list(length)
        sorting_time = measure_sorting_time(algorithm, nums)
        times.append(sorting_time)
    return sum(times) / repetitions

def main():
    lengths = [100, 1000, 3000, 5000, 7000, 10000, 20000, 50000]
    repetitions = 10

    heap_sort_times = []
    merge_sort_times = []
    quick_sort_times = []
    for length in lengths:
        heap_sort_time = sort_and_measure(heap_sort, length, repetitions)
        merge_sort_time = sort_and_measure(merge_sort, length, repetitions)
        quick_sort_time = sort_and_measure(quick_sort, length, repetitions)

        heap_sort_times.append(heap_sort_time)
        merge_sort_times.append(merge_sort_time)
        quick_sort_times.append(quick_sort_time)

    plt.plot(lengths, heap_sort_times, label='Heap Sort')
    plt.plot(lengths, merge_sort_times, label='Merge Sort')
    plt.plot(lengths, quick_sort_times, label='Quick Sort')
    plt.xlabel('Length of Array')
    plt.ylabel('Time (seconds)')
    plt.title('Sorting Time Complexity')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
