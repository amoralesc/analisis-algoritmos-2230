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

    $ python run_sorted_experiment.py <b> <e> <s>

    <b>: the lower bound of the sequence size
    <e>: the upper bound of the sequence size
    <s>: the step size
"""

import sys
import numpy as np
from timsort import timsort
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
    # and sort it
    input_sequence.sort()

    # Perform experiments
    # The experiment is performed for each size of the sequence
    # and the average time of each algorithm is stored

    data = []
    for n in range(b, e + 1, s):
        results = do_experiment(input_sequence[0:n], timsort)
        if not results[0]:
            print("ERROR: Input sequence was not ordered")
            sys.exit(1)
        print(n, results[1])
        data += [results[1]]

    # To test the results (regression and plotting), use run_test_results.py
    # with the data as given by the code above in a file.


if __name__ == "__main__":
    main()
    sys.exit(0)
