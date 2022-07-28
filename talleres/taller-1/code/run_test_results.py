"""
Prerrequisites:

    The following packages must be installed (requirements.txt):
    - numpy
    - matplotlib

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

    $ python run_test_results.py <results_file> <b> <e> <s>

    <results_file>: the input file containing the results of the experiments
    <b>: the lower bound of the sequence size
    <e>: the upper bound of the sequence size
    <s>: the step size
"""

import sys
import numpy as np
import matplotlib.pyplot as plt


def regression(x, y, degree):
    """Computes the regression of the given data.

    Args:
        x: a sequence of numbers
        y: a sequence of numbers
        degree: the degree of the polynomial to fit

    Returns:
        {coefficients, r2}
    """
    # Calculate the polynomial coefficients and crate the polynomial
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


def main():
    # Inputs
    results_file = open(sys.argv[1], "r")
    results = results_file.readlines()
    results_file.close()
    b = int(sys.argv[2])
    e = int(sys.argv[3])
    s = int(sys.argv[4])

    # remove the newline character from each string
    results = [result.rstrip() for result in results]
    # split each line into a list of strings
    results = [result.split() for result in results]
    # convert each string into a list of numbers
    results = [[float(number) for number in line] for line in results]
    # transpose the list of lists so that each list is a column
    # where results[1] is naive, results[2] is improved, results[3] is insertion
    results = list(map(list, zip(*results)))

    # Calculate the regression of the average time of each algorithm
    # The regression should fit a polynomial of 2nd degree
    regression_results = {}
    regression_results["naive"] = regression(np.arange(b, e + 1, s), results[1], 2)
    regression_results["improved"] = regression(np.arange(b, e + 1, s), results[2], 2)
    regression_results["insertion"] = regression(np.arange(b, e + 1, s), results[3], 2)

    # Print the regression results
    print("\nRegression results:")
    print("Naive bubble sort:")
    print(regression_results["naive"])
    print("Improved bubble sort:")
    print(regression_results["improved"])
    print("Insertion sort:")
    print(regression_results["insertion"])

    # Plot the original results
    plt.plot(range(b, e + 1, s), results[1], label="Naive bubble sort")
    plt.plot(range(b, e + 1, s), results[2], label="Improved bubble sort")
    plt.plot(range(b, e + 1, s), results[3], label="Insertion sort")
    plt.legend()
    plt.xlabel("Sequence size (# elements)")
    plt.ylabel("Average time (s)")
    plt.show()


if __name__ == "__main__":
    main()
    sys.exit(0)
