/**
 * Compilation instructions:
 * $ g++ -std=c++11 run_powers_two_experiment.cpp reverse_binary_representation.cpp experiment.cpp -o run_powers_two_experiment
 * 
 * Execution instructions:
 * $ ./run_powers_two_experiment <r>
 * <k>: the max power of two to test (between 0 and 19)
 */

#include <iostream>
#include "reverse_binary_representation.h"
#include "experiment.h"


int main(int argc, char* argv[]) {
    if (argc < 2) {
        std::cerr
            << "Usage: " << argv[0]
            << " <k>"
            << std::endl;
        return(-1);
    }
    unsigned int k = std::atoi(argv[1]);
    if (k < 0 || k > MAX_POWER_OF_10 + 1) {
        std::cerr
            << "k must be between 0 and 20"
            << std::endl;
        return(-1);
    }

    std::cout << "2^i " << "iterative_(ns) " << "divide_conquer_(ns)" << std::endl;
    unsigned long long power2 = 1;
    for (unsigned int i = 0; i < k; i++) {
        double iterative_time = 
            doExperiment(power2, &reverseBinaryRepresentationIterative, 100);
        double divide_conquer_time =
            doExperiment(power2, &reverseBinaryRepresentationDC, 100);
        
        std::cout 
            << i << " " 
            << iterative_time << " " 
            << divide_conquer_time
            << std::endl;
        power2 *= 2;
    }
}
