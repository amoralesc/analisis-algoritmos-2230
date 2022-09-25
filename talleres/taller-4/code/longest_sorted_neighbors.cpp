#include "longest_sorted_neighbors.h"

#include <algorithm>

unsigned int longestSortedNeighbors(
    std::vector<std::vector<unsigned int>> &matrix, 
    unsigned int i, unsigned int j,
    std::vector<std::vector<unsigned int>> &memo
) {
    if (memo[i][j] != 0) {
        return memo[i][j];
    }
    unsigned int max = 0;
    if (i > 0 && matrix[i][j] - 1 == matrix[i - 1][j]) {
        max = std::max(max, longestSortedNeighbors(matrix, i - 1, j, memo));
    }
    if (i < matrix.size() - 1 && matrix[i][j] - 1 == matrix[i + 1][j]) {
        max = std::max(max, longestSortedNeighbors(matrix, i + 1, j, memo));
    }
    if (j > 0 && matrix[i][j] - 1 == matrix[i][j - 1]) {
        max = std::max(max, longestSortedNeighbors(matrix, i, j - 1, memo));
    }
    if (j < matrix[0].size() - 1 && matrix[i][j] - 1 == matrix[i][j + 1]) {
        max = std::max(max, longestSortedNeighbors(matrix, i, j + 1, memo));
    }
    memo[i][j] = max + 1;
    return memo[i][j];
}

unsigned int longestSortedNeighbors(std::vector<std::vector<unsigned int>> matrix) {
    unsigned int max = 0;
    std::vector<std::vector<unsigned int>> memo(matrix.size(), std::vector<unsigned int>(matrix[0].size()));
    for (unsigned int i = 0; i < matrix.size(); i++) {
        for (unsigned int j = 0; j < matrix[0].size(); j++) {
            if (memo[i][j] == 0) {
                max = std::max(max, longestSortedNeighbors(matrix, i, j, memo));
            } else {
                max = std::max(max, memo[i][j]);
            }
        }
    }
    return max;
}
