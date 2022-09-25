#include "longest_sorted_neighbors.h"

#include <iostream>
#include <algorithm>    // std::max
#include <utility>      // std::pair, std::make_pair

unsigned int longestSortedNeighbors(
    std::vector<std::vector<unsigned int>> &matrix, 
    unsigned int i, unsigned int j,
    std::vector<std::vector<unsigned int>> &M,
    std::vector<std::vector<std::pair<unsigned int, unsigned int>>> &B
) {
    if (M[i][j] != 0) {
        return M[i][j];
    }
    unsigned int max = 0;
    if (i > 0 && matrix[i][j] - 1 == matrix[i - 1][j]) {
        max = std::max(max, longestSortedNeighbors(matrix, i - 1, j, M, B));
        B[i][j] = std::make_pair(i - 1, j);
    }
    if (i < matrix.size() - 1 && matrix[i][j] - 1 == matrix[i + 1][j]) {
        max = std::max(max, longestSortedNeighbors(matrix, i + 1, j, M, B));
        B[i][j] = std::make_pair(i + 1, j);
    }
    if (j > 0 && matrix[i][j] - 1 == matrix[i][j - 1]) {
        max = std::max(max, longestSortedNeighbors(matrix, i, j - 1, M, B));
        B[i][j] = std::make_pair(i, j - 1);
    }
    if (j < matrix[0].size() - 1 && matrix[i][j] - 1 == matrix[i][j + 1]) {
        max = std::max(max, longestSortedNeighbors(matrix, i, j + 1, M, B));
        B[i][j] = std::make_pair(i, j + 1);
    }
    M[i][j] = max + 1;
    return M[i][j];
}

std::vector<unsigned int> longestSortedNeighbors(
    std::vector<std::vector<unsigned int>> matrix
) {
    std::vector<std::vector<unsigned int>> M(
        matrix.size(), 
        std::vector<unsigned int>(matrix[0].size())
    );
    std::vector<std::vector<std::pair<unsigned int, unsigned int>>> B(
        matrix.size(),
        std::vector<std::pair<unsigned int, unsigned int>>(
            matrix[0].size()
        )
    );

    // Initialize B with their own coordinates
    for (unsigned int i = 0; i < matrix.size(); i++) {
        for (unsigned int j = 0; j < matrix[0].size(); j++) {
            B[i][j] = std::make_pair(i, j);
        }
    }

    // Find the longest sorted neighbors
    // After the loops end:
    // - max will contain the length of the longest sorted neighbors
    // - max_pos will contain the position of the first element of the longest
    //   sorted neighbors
    unsigned int max = 0;
    std::pair<unsigned int, unsigned int> max_pos;
    for (unsigned int i = 0; i < matrix.size(); i++) {
        for (unsigned int j = 0; j < matrix[0].size(); j++) {
            max = std::max(max, longestSortedNeighbors(matrix, i, j, M, B));
            if (max == M[i][j]) {
                max_pos = std::make_pair(i, j);
            }
        }
    }

    // Backtrack the B matrix to find the longest sorted neighbors
    std::vector<unsigned int> ans;
    while (B[max_pos.first][max_pos.second] != max_pos) {
        ans.push_back(matrix[max_pos.first][max_pos.second]);
        max_pos = B[max_pos.first][max_pos.second];
    }
    ans.push_back(matrix[max_pos.first][max_pos.second]);
    // Reverse ans
    std::reverse(ans.begin(), ans.end());

    return ans;
}
