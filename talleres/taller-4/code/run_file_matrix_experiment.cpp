/**
 * Compilation instructions:
 * $ g++ -std=c++17 run_file_matrix_experiment.cpp longest_sorted_neighbors.cpp -o run_file_matrix_experiment
 * 
 * Execution instructions:
 * $ ./run_file_matrix_experiment <file> [print = 1]
 * <file>: path to the file containing the matrix
 * [print]: print the matrix (1) or not (0). Default: 1
 */

#include <iostream>
#include <iomanip>
#include <vector>
#include <fstream>

#include "longest_sorted_neighbors.h"

std::vector<std::vector<unsigned int>> readMatrix(std::string filename) {
    std::ifstream file(filename);
    if (!file.is_open()) {
        std::cerr << "Error opening file " << filename << std::endl;
        exit(-1);
    }
    
    unsigned int n;
    file >> n;

    std::vector<std::vector<unsigned int>> matrix(n, std::vector<unsigned int>(n));
    for (unsigned int i = 0; i < n; i++) {
        for (unsigned int j = 0; j < n; j++) {
            file >> matrix[i][j];
        }
    }
    file.close();
    
    return matrix;
}

int main(int argc, char *argv[]) {
    if (argc < 2 || argc > 3) {
        std::cerr 
            << "Usage: " << argv[0]
            << " <file>"
            << " [print = 1]"
            << std::endl;
        return -1;
    }
    std::string filename = argv[1];
    bool print = true;
    if (argc == 3) {
        print = std::atoi(argv[2]);
    }
    
    std::vector<std::vector<unsigned int>> matrix = readMatrix(argv[1]);

    if (print) {
        unsigned int max_number = matrix.size() * matrix.size(), padding = 0;
        while (max_number > 0) {
            max_number /= 10;
            padding++;
        }
        std::cout << "Matrix: " << std::endl;
        for (unsigned int i = 0; i < matrix.size(); i++) {
            for (unsigned int j = 0; j < matrix.size(); j++) {
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
    
    return 0;
}
