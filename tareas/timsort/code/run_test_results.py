"""
Warning:

    The results file cannot contain a sequence size of 0.
    The regression algorithm calculates n * log(n) for each sequence size,
    so the sequence size of 0 will result in a log(0) value, which is undefined.

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

    <results_file>: the input file containing the results of the experiment
"""

import sys
import numpy as np
import matplotlib.pyplot as plt


def regression(x, y, degree=1):
    """Computes the regression of the given data.

    Args:
        x: a sequence of numbers
        y: a sequence of numbers
        degree: the degree of the polynomial to fit

    Returns:
        <polynomial, r2>
        polynomial: the fitted polynomial
        r2: the r-squared value
    """
    # Fit the polynomial
    coeffs = np.polyfit(x, y, degree)
    p = np.poly1d(coeffs)

    # Calculate r-squared
    yhat = p(x)
    ybar = np.sum(y) / len(y)
    ssreg = np.sum((yhat - ybar) ** 2)
    sstot = np.sum((y - ybar) ** 2)
    r_squared = ssreg / sstot

    return p, r_squared


def main():
    # Inputs
    results_file = open(sys.argv[1], "r")
    results = results_file.readlines()
    results_file.close()

    # remove the newline character from each string
    results = [result.rstrip() for result in results]
    # split each line into a list of strings
    results = [result.split() for result in results]
    # convert each string into a list of numbers
    results = [[float(number) for number in line] for line in results]
    # transpose the list of lists so that each list is a column
    # where results[0] is the column of sequence size and
    # results[1] is the column of the average time
    results = list(map(list, zip(*results)))

    # Calculate the regression of the average time
    # For the best case, the regression should fit a polynomial of degree 1
    # For the average and worst cases, the regression should fit a n*log(n) polynomial

    # Transform the sequence sizes to a n * log(n) form
    results[0] = [x * np.log(x) for x in results[0]]
    # Calculate the regression
    regression_results = regression(results[0], results[1], 1)

    # Print the regression results
    print("\nRegression results:")
    print("Polynomial:", regression_results[0])
    print("R-squared:", regression_results[1])

    # Plot
    plt.plot(results[0], results[1], "o", label="Data", markersize=4)
    plt.plot(results[0], regression_results[0](results[0]), label="Regression")
    plt.xlabel("Sequence size (n * log(n))")
    plt.ylabel("Average time (s)")
    plt.title("TimSort with reverse sorted sequences")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
    sys.exit(0)
