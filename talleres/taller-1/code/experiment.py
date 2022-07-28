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
"""

import time
import numpy as np


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


def regression(x, y, degree):
    """Computes the regression of the given data.

    Args:
        x: a sequence of numbers
        y: a sequence of numbers
        degree: the degree of the polynomial to fit

    Returns:
        {coefficients, r2}
    """

    coeffs = np.polyfit(x, y, degree)
    p = np.poly1d(coeffs)

    # Calculate r-squared
    yhat = p(x)
    ybar = np.sum(y) / len(y)
    ssreg = np.sum((yhat - ybar) ** 2)
    sstot = np.sum((y - ybar) ** 2)

    results = {}
    results["coeffs"] = coeffs
    results["r_squared"] = ssreg / sstot

    return results
