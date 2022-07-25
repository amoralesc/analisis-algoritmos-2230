from re import I


def naive_bubble_sort(seq):
    for i in range(len(seq)):
        for j in range(len(seq)-1):
            if seq[j+1] < seq[j]:
                seq[j], seq[j+1] = seq[j+1], seq[j]
    return seq

def optimized_bubble_sort(seq):
    for i in range(len(seq)):
        for j in range(len(seq)-1-i):
            if seq[j+1] < seq[j]:
                seq[j], seq[j+1] = seq[j+1], seq[j]
    return seq

def insertion_sort(seq):
    for j in range(1, len(seq)):
        k = seq[j]
        i = j - 1
        while 0 < i and k < seq[i]:
            seq[i+1] = seq[i]
            i -= 1
        seq[i+1] = k
    return seq
