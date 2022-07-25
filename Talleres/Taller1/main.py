import time
import sort
import numpy as np

# Parameters for the test
# The number of elements in each testing sequence
N = [10000, 20000, 30000]

# DO NOT TOUCH THESE
# The names of the sorting algorithms
sort_names = ["Naive Bubble Sort", "Optimized Bubble Sort", "Insertion Sort"]
# The sorting algorithms to be tested (coming from the sort.py file)
sort_algorithms = [
    sort.naive_bubble_sort,
    sort.optimized_bubble_sort,
    sort.insertion_sort,
]


def test_unsorted_random_numbers(N, names, algorithms):
    """Creates a random sequence of numbers, of length n = N[i],
    and sorts it using the algorithms in algorithms[i].
    Records the time of execution of each sorting algorithm
    and returns the results as a dictionary."""

    data = {}
    for name in names:
        data[name] = {}

    for n in N:
        seq = np.random.randint(0, n, n)
        for name, algorithm in zip(names, algorithms):
            testing_seq = seq.copy()
            start = time.time()
            algorithm(testing_seq)
            end = time.time()
            data[name][n] = end - start

    return data


def test_sorted_descending_numbers(N, names, algorithms):
    """Creates a sequence of numbers sorted in descending order,
    of length n = N[i], and sorts it using the algorithms in algorithms[i].
    Records the time of execution of each sorting algorithm
    and returns the results as a dictionary."""

    data = {}
    for name in names:
        data[name] = {}

    for n in N:
        seq = np.arange(n, 0, -1)
        for name, algorithm in zip(names, algorithms):
            testing_seq = seq.copy()
            start = time.time()
            algorithm(testing_seq)
            end = time.time()
            data[name][n] = end - start

    return data


def test_sorted_ascending_numbers(N, names, algorithms):
    """Creates a sequence of numbers sorted in ascending order,
    of length n = N[i], and sorts it using the algorithms in algorithms[i].
    Records the time of execution of each sorting algorithm
    and returns the results as a dictionary."""

    data = {}
    for name in names:
        data[name] = {}

    for n in N:
        seq = np.arange(n)
        for name, algorithm in zip(names, algorithms):
            testing_seq = seq.copy()
            start = time.time()
            algorithm(testing_seq)
            end = time.time()
            data[name][n] = end - start

    return data


def main():
    data = {}
    data["unsorted_random"] = test_unsorted_random_numbers(
        N, sort_names, sort_algorithms
    )
    data["sorted_descending"] = test_sorted_descending_numbers(
        N, sort_names, sort_algorithms
    )
    data["sorted_ascending"] = test_sorted_ascending_numbers(
        N, sort_names, sort_algorithms
    )
    print(data)


if __name__ == "__main__":
    main()
