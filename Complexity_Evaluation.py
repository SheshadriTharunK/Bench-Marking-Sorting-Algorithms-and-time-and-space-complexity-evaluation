import time
import random
import matplotlib.pyplot as plt

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr.pop()
        less_than_pivot = []
        greater_than_pivot = []
        for element in arr:
            if element <= pivot:
                less_than_pivot.append(element)
            else:
                greater_than_pivot.append(element)
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

def benchmark(sort_func, data):
    start_time = time.time()
    sort_func(data)
    end_time = time.time()
    return end_time - start_time

def run_experiment():
    dataset_sizes = [100, 500, 1000, 5000, 10000]
    results = {size: {} for size in dataset_sizes}

    for size in dataset_sizes:
        data = [random.randint(1, 1000) for _ in range(size)]
        algorithms = {
            "Bubble Sort": bubble_sort,
            "Selection Sort": selection_sort,
            "Insertion Sort": insertion_sort,
            "Merge Sort": merge_sort,
            "Quick Sort": quick_sort
        }

        for algorithm_name, algorithm_func in algorithms.items():
            results[size][algorithm_name] = benchmark(algorithm_func, data.copy())

    return results

def plot_results(results):
    for size, algorithms in results.items():
        plt.figure(figsize=(10, 6))
        plt.bar(algorithms.keys(), algorithms.values(), color=['red', 'green', 'blue', 'purple', 'orange'])
        plt.title(f'Algorithm Performance for Dataset Size {size}')
        plt.xlabel('Sorting Algorithms')
        plt.ylabel('Execution Time (seconds)')
        plt.show()

# Main execution
experiment_results = run_experiment()
print(experiment_results)
plot_results(experiment_results)
