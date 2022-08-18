"""
Prerrequisites:

    The following packages must be installed:
    - numpy
    - matplotlib

Execution instructions:

    $ python run_test_results.py <results_file>

    <results_file>: the input file containing the results of the power of two experiments
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
    results["p"] = p

    return results


def main():
    # Inputs
    results_file = open(sys.argv[1], "r")
    results = results_file.readlines()
    results_file.close()

    # remove the newline character from each string
    results = [result.rstrip() for result in results]
    # split each line into a list of strings
    results = [result.split() for result in results]
    # drop the fisrt row (header)
    results = results[1:]
    # convert each string into a list of numbers
    results = [[float(number) for number in line] for line in results]
    # transpose the list of lists so that each list is a column
    # where results[0] is k, results[1] is iterative, results[2] is divide and conquer
    results = list(map(list, zip(*results)))
    # increase every results[0] by 1
    results[0] = [i + 1 for i in results[0]]

    # Calculate the regression of the average time of each algorithm
    # The regression should fit a line of the form y = mx + b
    regression_results = {}
    regression_results["iterative"] = regression(results[0], results[1], 1)
    regression_results["divide_and_conquer"] = regression(results[0], results[2], 1)

    # Print the regression results
    print("\nRegression results:")
    print("Iterative:")
    print(regression_results["iterative"])
    print("Divide and conquer:")
    print(regression_results["divide_and_conquer"])

    # Plot the results
    plt.plot(results[0], results[1], "o", label="Iterative")
    plt.plot(results[0], results[2], "o", label="Divide & Conquer")
    plt.plot(
        results[0],
        regression_results["iterative"]["p"](results[0]),
        label="Iterative Regression",
    )
    plt.plot(
        results[0],
        regression_results["divide_and_conquer"]["p"](results[0]),
        label="Divide & Conquer Regression",
    )

    plt.legend()
    plt.xlabel("bits")
    plt.ylabel("time (nanoseconds)")
    plt.show()


if __name__ == "__main__":
    main()
    sys.exit(0)
