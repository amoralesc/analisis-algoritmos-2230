def insertion_sort(seq, b, e):
    for j in range(b + 1, e + 1):
        i = j
        while i > b and seq[i] < seq[i - 1]:
            seq[i], seq[i - 1] = seq[i - 1], seq[i]
            i -= 1


def merge(seq, b, q, e):
    n1 = q - b + 1
    n2 = e - q
    left = [0] * (n1 + 1)
    right = [0] * (n2 + 1)
    for i in range(n1):
        left[i] = seq[b + i]
    for i in range(n2):
        right[i] = seq[q + i + 1]
    left[n1] = float("inf")
    right[n2] = float("inf")
    i = 0
    j = 0

    for k in range(b, e + 1):
        if left[i] < right[j]:
            seq[k] = left[i]
            i += 1
        else:
            seq[k] = right[j]
            j += 1


def timsort(seq):
    n = len(seq)
    min_run = 32

    # Sort individual subarrays of size min_run
    for b in range(0, n, min_run):
        # The end of the subarray is either the current beginning + run size
        # or the end of the array, whichever is smaller
        e = min(b + min_run - 1, n - 1)
        insertion_sort(seq, b, e)

    # Start merging from size RUN (or 32). It will merge
    # to form size 64, then 128, 256 and so on ....
    size = min_run
    while size < n:
        # Pick starting point of left sub array.
        # After every merge, left increases by 2*size
        for b in range(0, n, 2 * size):

            # Find ending point of left sub array
            # q+1 is starting point of right sub array
            q = min(n - 1, b + size - 1)
            e = min((b + 2 * size - 1), (n - 1))

            # Merge sub array seq[left.....mid] &
            # seq[mid+1....right]
            if q < e:
                merge(seq, b, q, e)

        size = 2 * size
