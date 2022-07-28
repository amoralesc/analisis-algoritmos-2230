"""
Prerrequisites:

    The following packages must be installed (requirements.txt):
    - numpy

    The requirements can be installed through a venv as follows:

    1. Create a virtual environment
    $ python -m venv venv

    2. Activate the virtual environment
    $ source venv/bin/activate
    
    3. Install the packages
    $ pip install -r requirements.txt

    If working on Windows (PowerShell), step 2 can be replaced by:
    $ venv\Scripts\activate
    You may need to activate the PS scripts first (one-time only):
    $ Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

Execution instructions:

    $ python run_reverse_sorted_experiment.py <b> <e> <s>

    <b>: the lower bound of the sequence size
    <e>: the upper bound of the sequence size
    <s>: the step size
"""

import sys
import numpy as np
from sorting import *
from experiment import *


def main():
    # Inputs
    b = int(sys.argv[1])
    e = int(sys.argv[2])
    s = int(sys.argv[3])

    # Create a random sequence of size e, made up of random numbers
    input_sequence = np.random.randint(
        -(2**31), 2**31, size=e
    ).tolist()  # tolist ensures a python list is returned
    # Sort the sequence in reverse order
    input_sequence.sort(reverse=True)

    # Perform experiments
    # The experiment is performed for each size of the sequence
    # and the average time of each algorithm is returned

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

    # To test the results (regression and plotting), use run_test_results.py
    # with the data as given by the code above in a file.


if __name__ == "__main__":
    main()
    sys.exit(0)
