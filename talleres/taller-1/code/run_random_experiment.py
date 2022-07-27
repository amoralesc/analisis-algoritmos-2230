"""
Execution instructions:

    python run_random_experiment.py <input_file> <b> <e> <s>

    <input_file>: the input binary file to build the random sequence from
    <b>: the lower bound of the sequence size
    <e>: the upper bound of the sequence size
    <s>: the step size
"""

import struct, sys, time
from sorting import *


def is_sorted(seq):
    """Checks if the sequence is sorted.

    Args:
        seq: a sequence of elements

    Returns:
        True if the sequence is sorted, False otherwise
    """
    f = True
    for i in range(len(seq) - 1):
        f = f and not (seq[i + 1] < seq[i])
    return f


def do_experiment(seq, sorting_algorithm):
    """Sorts the sequence using the given sorting algorithm. It runs the
    experiment for 10 times and returns the average time.

    Args:
        seq: a sequence of elements
        sorting_algorithm: a sorting algorithm that takes a sequence as input
        and returns a sorted sequence

    Returns:
        [is_sorted, avg_time]
    """
    run_times = 10
    time_total = 0
    sorted = True
    for i in range(run_times):
        copy_seq = seq.copy()
        start = time.time()
        sorting_algorithm(copy_seq)
        end = time.time()
        sorted = sorted and is_sorted(copy_seq)
        time_total += float(end - start)
    return [sorted, time_total / float(run_times)]


def main():
    # Inputs
    input_file = open(sys.argv[1], "rb")
    input_buffer = input_file.read()
    input_file.close()
    b = int(sys.argv[2])
    e = int(sys.argv[3])
    s = int(sys.argv[4])

    # Data type configuration
    element_type = int
    element_size = 4
    element_id = "i"
    N = len(input_buffer) // element_size

    # Read sequence as numbers
    input_sequence = []
    for i in range(N):
        input_sequence += [
            struct.unpack(
                element_id, input_buffer[element_size * i : element_size * (i + 1)]
            )[0]
        ]

    # Perform experiments
    # The experiment is performed for each size of the sequence
    # and the average time of each algorithm is returned
    for n in range(b, e + 1, s):
        nbr = do_experiment(input_sequence[0:n], naive_bubble_sort)
        ibr = do_experiment(input_sequence[0:n], improved_bubble_sort)
        inr = do_experiment(input_sequence[0:n], insertion_sort)
        if not (nbr[0] and ibr[0] and inr[0]):
            print("ERROR: Input sequence was not ordered")
            sys.exit(1)
        print(n, nbr[1], ibr[1], inr[1])


if __name__ == "__main__":
    main()
    sys.exit(0)
