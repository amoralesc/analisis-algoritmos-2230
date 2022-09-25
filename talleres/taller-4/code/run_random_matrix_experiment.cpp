/**
 * Compilation instructions:
 * $ g++ -std=c++17 run_random_matrix_experiment.cpp longest_sorted_neighbors.cpp -o run_random_matrix_experiment
 * 
 * Execution instructions:
 * $ ./run_random_matrix_experiment <n> [print = 1]
 * <n>: size of the matrix
 * [print]: print the matrix (1) or not (0). Default: 1
 */

#include <iostream>
#include <iomanip>
#include <vector>
#include <algorithm>
#include <random>

#include "longest_sorted_neighbors.h"

/**
 * @brief Creates a random matrix of size n x n filled with natural numbers
 * shuffled from 1 to n * n.
 * 
 * @param n the size of the matrix
 * @return (std::vector<std::vector<unsigned int>>) the matrix
 */
std::vector<std::vector<unsigned int>> createRandomMatrix(unsigned int n) {
    // Create a vector of size n * n and fill it with numbers from 1 to n * n
    std::vector<unsigned int> numbers(n * n);
    for (unsigned int i = 0; i < n * n; i++) {
        numbers[i] = i + 1;
    }

    // Shuffle the vector
    auto rd = std::random_device {}; 
    auto rng = std::default_random_engine { rd() };
    std::shuffle(numbers.begin(), numbers.end(), rng);

    // Create a matrix of size n * n and fill it with the shuffled numbers
    std::vector<std::vector<unsigned int>> matrix(n, std::vector<unsigned int>(n));
    for (unsigned int i = 0; i < n; i++) {
        for (unsigned int j = 0; j < n; j++) {
            matrix[i][j] = numbers[i * n + j];
        }
    }
    return matrix;
}

int main(int argc, char* argv[]) {
    if (argc < 2 || argc > 3) {
        std::cerr
            << "Usage: " << argv[0]
            << " <n>"
            << " [print = 1]"
            << std::endl;
        return(-1);
    }
    unsigned int n = std::atoi(argv[1]);
    if (n < 2 || n > 100) {
        std::cerr
            << "n must be between 2 and 100"
            << std::endl;
        return(-1);
    }
    bool print = true;
    if (argc == 3) {
        print = std::atoi(argv[2]);
    }

    std::vector<std::vector<unsigned int>> matrix = createRandomMatrix(n);

    if (print) {
        unsigned int max_number = n * n, padding = 0;
        while (max_number > 0) {
            max_number /= 10;
            padding++;
        }
        std::cout << "Matrix:" << std::endl;
        for (unsigned int i = 0; i < n; i++) {
            for (unsigned int j = 0; j < n; j++) {
                std::cout << std::setw(padding) << matrix[i][j] << " ";
            }
            std::cout << std::endl;
        }
        std::cout << std::endl;
    }

    std::vector<unsigned int> result = longestSortedNeighbors(matrix);
    std::cout << "Result (" << result.size() << "): " << std::endl;
    for (unsigned int i = 0; i < result.size(); i++) {
        std::cout << result[i] << " ";
    }
}
