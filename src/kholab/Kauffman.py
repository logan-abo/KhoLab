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
        return

    if size[rx] < size[ry]:
        rx, ry = ry, rx

    parent[ry] = rx
    size[rx] += size[ry]


def compute_kauffman_bracket():

    # Crossing Info
    PD = [(7,1,8,32), (1,26,2,27), (11,2,12,3), (3,16,4,17), (13,5,14,4), (5,15,6,14), (25,6,26,7), (19,8,20,9), (9,28,10,29), (21,11,22,10), (15,13,16,12), (17,31,18,30), (23,18,24,19), (27,21,28,20), (29,22,30,23), (31,25,32,24)]
    crossings = [tuple(x - 1 for x in t) for t in PD]

    # Number of crossings
    N = len(crossings)
    format = "{0:0"+str(2*N)+"b}"

    unknot = LaurentPolynomial({-2: -1, 2: -1})
    kauffman_bracket = LaurentPolynomial()


    for state in range(1 << N):

        ## parent keeps track of equivalence of edges (merging)
        parent = list(range(2*N))
        size = [1] * (2*N)


        # compute the all zeros crossing
        for k, c in enumerate(crossings):

            bit = (state >> k) & 1

            # First pair
            union(parent, size, c[0], c[1 + 2*bit])

            # Second pair
            union(parent, size, c[2 - bit], c[3 - bit])


        roots = set()
        for j in range(2*N):
            roots.add(find(parent, j))
        num_loops = len(roots)

        state_power = N - 2 * state.bit_count()
        state_poly = LaurentPolynomial({state_power: 1})

        kauffman_bracket += state_poly * (unknot ** (num_loops-1))


    print(kauffman_bracket)


    