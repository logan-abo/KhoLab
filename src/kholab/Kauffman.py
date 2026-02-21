from collections import defaultdict

from .LaurentPolynomial import LaurentPolynomial


def find(parent, x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]   # path compression
        x = parent[x]
    return x


def union(parent, size, x, y):
    rx = find(parent, x)
    ry = find(parent, y)

    if rx == ry:
        return 0

    if size[rx] < size[ry]:
        rx, ry = ry, rx

    parent[ry] = rx
    size[rx] += size[ry]

    return 1


def compute_kauffman_bracket():

    # Crossing Info
    PD = [(7,1,8,32), (1,26,2,27), (11,2,12,3), (3,16,4,17), (13,5,14,4), (5,15,6,14), (25,6,26,7), (19,8,20,9), (9,28,10,29), (21,11,22,10), (15,13,16,12), (17,31,18,30), (23,18,24,19), (27,21,28,20), (29,22,30,23), (31,25,32,24)]
    crossings = [tuple(x - 1 for x in t) for t in PD]

    # Number of crossings
    N = len(crossings)
    print("Crossings:", N)

    unknot = LaurentPolynomial({-2: -1, 2: -1})
    unknot_powers = [unknot**i for i in range(2*N + 1)]

    counts = defaultdict(int)

    resolution_pairs = []

    for a,b,c,d in crossings:
        resolution_pairs.append([
            ((a,b),(c,d)),   # 0 resolution
            ((a,d),(b,c))    # 1 resolution
        ])


    for state in range(1 << N):

        ## parent keeps track of equivalence of edges (merging)
        parent = list(range(2*N))
        size = [1] * (2*N)

        components = 2*N

        # compute the all zeros crossing
        for k, c in enumerate(crossings):

            bit = (state >> k) & 1

            pairs = resolution_pairs[k][bit]

            components -= union(parent, size, pairs[0][0], pairs[0][1])
            components -= union(parent, size, pairs[1][0], pairs[1][1])


        num_loops = components

        state_power = N - 2 * state.bit_count()

        counts[(state_power, num_loops)] += 1


    kauffman_bracket = LaurentPolynomial()

    for (power, loops), multiplicity in counts.items():

        term = LaurentPolynomial({power: multiplicity})
        term *= unknot_powers[loops - 1]

        kauffman_bracket += term

    print(kauffman_bracket)


    