import random
import time
import threading
import matplotlib.pyplot as plt

def bubble_sort(nums):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True

def insertion_sort(nums):
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        while j >= 0 and key < nums[j]:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key

def selection_sort(nums):
    for i in range(len(nums)):
        min_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]

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
    lengths = [100, 1000, 3000, 5000, 7000,10000]
    repetitions = 10

    bubble_sort_times = []
    insertion_sort_times = []
    selection_sort_times = []
    for length in lengths:
        bubble_sort_time = sort_and_measure(bubble_sort, length, repetitions)
        insertion_sort_time = sort_and_measure(insertion_sort, length, repetitions)
        selection_sort_time = sort_and_measure(selection_sort, length, repetitions)

        bubble_sort_times.append(bubble_sort_time)
        insertion_sort_times.append(insertion_sort_time)
        selection_sort_times.append(selection_sort_time)

    plt.plot(lengths, bubble_sort_times, label='Bubble Sort')
    plt.plot(lengths, insertion_sort_times, label='Insertion Sort')
    plt.plot(lengths, selection_sort_times, label='Selection Sort')
    plt.xlabel('Length of Array')
    plt.ylabel('Time (seconds)')
    plt.title('Sorting Time Complexity')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
