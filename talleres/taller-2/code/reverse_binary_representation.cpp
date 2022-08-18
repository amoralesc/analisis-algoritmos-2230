#include "reverse_binary_representation.h"


/**
 * @brief The function finds the reversed binary representation of a natural
 * number. That is, it calculates the binary representation of the number,
 * reverses it, and then converts it to a decimal number. It uses an iterative
 * algorithm.
 * 
 * @param x the natural number to find its reversed binary representation
 * @return (unsigned int) the reversed binary representation
 */
unsigned int reverseBinaryRepresentationIterative(unsigned int x) {
    unsigned long long 
        b = 0,
        factor2 = 1, 
        factor10 = 1;
    while (x > 0) {
        b += (x % 2) * factor10;
        x /= 2;
        factor2 = factor2 * 2;
        factor10 *= 10;
    }
    int y = 0;
    while (b > 0) {
        factor2 /= 2;
        y += (b % 10) * factor2;
        b /= 10;
    }
    return y;
}

/**
 * @brief The function reverses a number that starts in a beg digit
 * and ends in an end digit, divided by a q middle digit. i.e.: 123456
 * where beg = 0, end = 5, q = 2 becomes 456123.
 * 
 * @param num the number to reverse
 * @param n the number of digits in the number
 * @param beg the beginning digit (0-indexed)
 * @param q the middle digit (0-indexed)
 * @param end the ending digit (0-indexed)
 * @param pow10 a precomputed array of powers of 10
 * @return unsigned long long the reversed number
 */
unsigned long long reverseNumberAux(
    unsigned long long num, unsigned int n, int beg, int q, int end, unsigned long long pow10[]
) {
    unsigned long long 
        pow1 = pow10[n - beg],
        pow2 = pow10[n - end - 1],
        pow3 = pow10[end - q];
    int 
        num_left = num / pow1,
        num_right = num % pow2,
        num_mid = (num / pow2) % (pow1 / pow2);
    return num_left * pow1 + num_mid * pow2 + num_right;
}

/**
 * @brief The function reverses a number using divide and conquer.
 * It first divides the number into two parts, and then recursively calls
 * itself on each part. When the number can no longer be divided, it
 * calls ::reverseNumberAux to reverse the number from the beg digit
 * to the end digit.
 * 
 * @param num the number to reverse
 * @param n the number of digits in the number
 * @param beg the current beginning digit (0-indexed)
 * @param end the current end digit (0-indexed)
 * @param pow10 a precomputed array of powers of 10
 * @return (unsigned long long) the reversed number
 */
unsigned long long reverseNumber(
    unsigned long long num, unsigned int n, int beg, int end, unsigned long long pow10[]
) {
    if (beg < end) {
        int q = (beg + end) / 2;
        num = reverseNumber(num, n, beg, q, pow10);
        num = reverseNumber(num, n, q + 1, end, pow10);
        return reverseNumberAux(num, n, beg, q, end, pow10);
    } else {
        return num;
    }
}

/**
 * @brief The function finds the reversed binary representation of a natural
 * number. That is, it calculates the binary representation of the number,
 * reverses it, and then converts it to a decimal number. It uses a divide and
 * conquer algorithm.
 * 
 * @param x the natural number to find its reversed binary representation
 * @return (unsigned int) the reversed binary representation
 */
unsigned int reverseBinaryRepresentationDC(unsigned int x) {
    unsigned int n = 0;
    unsigned long long
        b = 0,
        factor10 = 1,
        pow10[MAX_POWER_OF_10 + 1];     // Powers of 10 are precomputed
    pow10[0] = 1;
    while (x > 0) {
        b += (x % 2) * factor10;
        x /= 2;
        n++;
        factor10 *= 10;
        pow10[n] = factor10;
    }
    unsigned long long b2 = reverseNumber(b, n, 0, n - 1, pow10);
    int y = 0;
    unsigned long long factor2 = 1;
    while (b2 > 0) {
        y += (b2 % 10) * factor2;
        b2 /= 10;
        factor2 *= 2;
    }
    return y;
}
