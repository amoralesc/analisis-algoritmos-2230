import sys, random, itertools, pprint


def create_random_grid(n: int, m: int) -> list:
    grid = [[0 for _ in range(n)] for _ in range(n)]

    # Add q mines to the grid at random positions
    mines = set()
    while len(mines) < m:
        i = random.randint(0, n - 1)
        j = random.randint(0, n - 1)
        grid[i][j] = 1
        mines.add((i, j))

    return grid


def find_mines_bf(grid: list, m: int) -> list:
    # Find the m mines by brute force
    # Basically, compute all m-combinations of the [i][j] pairs
    # and check if they are the mines. Eventually, we will find
    # the correct combination.

    # First, create the list of all possible pairs
    pairs = []
    for i in range(len(grid)):
        for j in range(len(grid)):
            pairs += [(i, j)]

    # Now, compute all m-combinations of the pairs
    # and check if they are the mines
    for mines in itertools.combinations(pairs, m):
        all_mines = True
        k = 0
        while k < m and all_mines:
            mine = mines[k]
            if grid[mine[0]][mine[1]] != 1:
                all_mines = False
            k += 1
        if all_mines:
            return list(mines)

    return []


def main(n: int, m: int) -> None:
    grid = create_random_grid(n, m)
    print("grid =")
    pprint.pprint(grid)

    mines = find_mines_bf(grid, m)
    print("\nmines =", mines)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3", sys.argv[0], "n m")
        sys.exit(1)
    n = int(sys.argv[1])  # n x n grid
    q = int(sys.argv[2])  # m mines

    main(n, q)
