import random, sys, itertools, pprint


def create_random_directed_graph(n, p=0.5):
    vertices = [i for i in range(n)]
    edges = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(i + 1, n):
            if i != j:
                q = random.uniform(0, 1)
                if q < p:
                    v = random.randint(1, 100)
                    edges[i][j] = v
                    edges[j][i] = v

    return (vertices, edges)


def vertex_coverage_bf(graph):
    vertices, edges = graph
    best_c = vertices.copy()
    min_c = len(vertices)

    # Brute force: compute all combinations of vertices
    for r in range(1, len(vertices) + 1):
        for c in itertools.combinations(vertices, r):
            c = list(c)
            # covered tracks which vertices are covered by c
            covered = [False for _ in range(len(vertices))]

            # For every vertex in c, mark all connected vertices
            # to it as covered
            for v in c:
                covered[v] = True
                for v2 in range(len(vertices)):
                    if v != v2 and edges[v][v2] > 0:
                        covered[v2] = True

            # Check if every vertex is covered
            covers_all = True
            i = 0
            while i < len(vertices) and covers_all:
                if not covered[i]:
                    covers_all = False
                i += 1

            # The best solution should minimize the amount of
            # vertices required to cover the whole graph
            if covers_all and len(c) < min_c:
                best_c = c
                min_c = len(c)

    return best_c


def vertex_coverage_approx(graph, shuffle=True):
    vertices, edges = graph[0], graph[1]

    # Deconstruct the adjacency matrix into an edges list
    # This makes it easier to do the algo
    edges_list = []
    for i in range(len(vertices)):
        for j in range(i + 1, len(vertices)):
            if edges[i][j] > 0:
                edges_list += [(i, j)]
    # Shuffling ensures that the edges are chosen arbitrarily
    if shuffle:
        random.shuffle(edges_list)
    # c tracks which vertices ensure the coverage
    # by indices (True: ensures, False: doesn't)
    c = [False for _ in range(len(vertices))]

    # The magic algo
    while len(edges_list) > 0:
        edge = edges_list.pop()
        c[edge[0]] = True
        c[edge[1]] = True
        i = len(edges_list) - 1
        while i > -1:
            if edge[0] in edges_list[i] or edge[1] in edges_list[i]:
                edges_list.pop(i)
            i -= 1

    # Add disconnected vertices (the algo doesn't cover those
    # and adding a simple v_i - v_i edge worsens the solution)
    for i in range(len(vertices)):
        is_disconnected = True
        j = 0
        while j < len(vertices) and is_disconnected:
            if i != j and edges[i][j] > 0:
                is_disconnected = False
            j += 1
        if is_disconnected:
            c[i] = True

    # Translate bool list to indices
    c = [i for i in range(len(vertices)) if c[i]]

    return list(c)


def main(n, p):
    graph = create_random_directed_graph(n, p)

    print("vertices =", graph[0])
    print("edges =")
    pprint.pprint(graph[1])
    print()

    best_bf = vertex_coverage_bf(graph)
    print("coverage (brute force) =  ", best_bf)

    best_approx = vertex_coverage_approx(graph)
    print("coverage (approximation) =", best_approx)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3", sys.argv[0], "n p")
        sys.exit(1)
    n = int(sys.argv[1])
    p = float(sys.argv[2])

    main(n, p)

# Note: maybe representing the graph edges as an
# adjacency list vs an adjacency matrix could make
# the approximation algo easier to compute. The
# brute force algo wouldn't suffer from this change
