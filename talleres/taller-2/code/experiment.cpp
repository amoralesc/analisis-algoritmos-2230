#include "experiment.h"
#include <chrono>


/**
 * @brief The function runs an experiment that measures the time it takes to
 * compute the reversed binary representation of a number through the passed
 * algorithm. The function runs the experiment multiple times and returns the
 * average time.
 * 
 * @param x the number to find its reversed binary representation
 * @param function the algorithm to use
 * @param run_times the number of times to run the experiment. Default is 10.
 * @return (double) the average time it takes in nanoseconds (10^-9 s)
 */
double doExperiment(
    unsigned int x, unsigned int (*function)(unsigned int), unsigned int run_times
) {
    if (run_times < 0) {
        return -1;
    }
    double time_total = 0;
    for (unsigned int i = 0; i < run_times; i++) {
        auto start = std::chrono::steady_clock::now();
        int y = function(x);
        auto end = std::chrono::steady_clock::now();
        time_total += std::chrono::duration_cast<std::chrono::nanoseconds>(end - start).count();
    }
    return time_total / run_times;
}
