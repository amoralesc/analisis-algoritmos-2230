"""
Prerrequisites:

    The following packages must be installed (requirements.txt):
    - matplotlib

    The requirements can be installed through a venv as follows:

    1. Create a virtual environment
    $ python -m venv venv

    2. Activate the virtual environment (Linux/Mac)
    $ source venv/bin/activate
    
    3. Install the packages
    $ pip install -r requirements.txt

    If working on Windows (PowerShell), step 2 can be replaced by:
    $ venv\Scripts\activate
    You may need to activate the PS scripts first (one-time only):
    $ Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

Execution instructions:

    $ python run_random_experiment.py <input_file> <b> <e> <s>

    <input_file>: the input binary file to build the random sequence from
    <b>: the lower bound of the sequence size
    <e>: the upper bound of the sequence size
    <s>: the step size
"""

import struct, sys
import matplotlib.pyplot as plt
from sorting import *
from experiment import *


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
    # and the average time of each algorithm is stored

    data = {}
    data["naive"] = []
    data["improved"] = []
    data["insertion"] = []
    for n in range(b, e + 1, s):
        nbr = do_experiment(input_sequence[0:n], naive_bubble_sort)
        ibr = do_experiment(input_sequence[0:n], improved_bubble_sort)
        inr = do_experiment(input_sequence[0:n], insertion_sort)
        if not (nbr[0] and ibr[0] and inr[0]):
            print("ERROR: Input sequence was not ordered")
            sys.exit(1)
        print(n, nbr[1], ibr[1], inr[1])
        data["naive"] += [nbr[1]]
        data["improved"] += [ibr[1]]
        data["insertion"] += [inr[1]]

    # Calculate the regression of the average time of each algorithm
    # The regression should fit a polynomial of 2nd degree
    results = {}
    results["naive"] = regression(np.arange(b, e + 1, s), data["naive"], 2)
    results["improved"] = regression(np.arange(b, e + 1, s), data["improved"], 2)
    results["insertion"] = regression(np.arange(b, e + 1, s), data["insertion"], 2)

    # Print the regression results
    print("\nRegression results:")
    print("Naive bubble sort:")
    print(results["naive"])
    print("Improved bubble sort:")
    print(results["improved"])
    print("Insertion sort:")
    print(results["insertion"])

    # Plot the results
    plt.plot(range(b, e + 1, s), data["naive"], label="Naive bubble sort")
    plt.plot(range(b, e + 1, s), data["improved"], label="Improved bubble sort")
    plt.plot(range(b, e + 1, s), data["insertion"], label="Insertion sort")
    plt.legend()
    plt.xlabel("Sequence size (# elements)")
    plt.ylabel("Average time (s)")
    plt.show()


if __name__ == "__main__":
    main()
    sys.exit(0)
