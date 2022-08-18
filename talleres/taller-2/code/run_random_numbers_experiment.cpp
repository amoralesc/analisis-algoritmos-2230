/**
 * Compilation instructions:
 * $ g++ -std=c++11 run_random_numbers_experiment.cpp reverse_binary_representation.cpp experiment.cpp -o run_random_numbers_experiment
 * 
 * Execution instructions:
 * $ ./run_random_numbers_experiment <n>
 * <n>: quantity of random numbers to generate and test
 */

#include <iostream>
#include <stdlib.h>
#include <time.h>
#include <math.h>
#include "reverse_binary_representation.h"
#include "experiment.h"

int main(int argc, char* argv[]) {
    if (argc < 2) {
        std::cerr
            << "Usage: " << argv[0]
            << " <n>"
            << std::endl;
        return(-1);
    }
    unsigned int n = std::atoi(argv[1]);
    if (n < 1) {
        std::cerr
            << "n must be greater than 0"
            << std::endl;
        return(-1);
    }

    srand(time(NULL));
    unsigned int MAX_NUMBER = pow(2, MAX_POWER_OF_10);
    double iterative_time = 0, divide_conquer_time = 0;

    for (unsigned int i = 0; i < n; i++) {
        unsigned int number = rand() % MAX_NUMBER;

        iterative_time += 
            doExperiment(number, &reverseBinaryRepresentationIterative) / pow(10, 6);
        divide_conquer_time +=
            doExperiment(number, &reverseBinaryRepresentationDC) / pow(10, 6);
    }
    std::cout 
        << "Iterative: " << iterative_time << " milliseconds" << std::endl
        << "Divide & Conquer: " << divide_conquer_time << " milliseconds" << std::endl;
}
