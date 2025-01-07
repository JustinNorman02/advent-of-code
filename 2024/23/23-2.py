import networkx as nx

# with open("test.txt") as f:
with open("data.txt") as f:

    lines = f.read().split("\n")

    for i in range(len(lines)):
        lines[i] = tuple(lines[i].split('-'))

    G = nx.Graph()

    # print(lines)

    G.add_edges_from(lines)


    c = list(nx.find_cliques(G))

    largest_clique = max(c, key=len) if c else None

    if largest_clique:
        print(largest_clique)
        largest_clique = sorted(largest_clique)
        print(','.join(largest_clique))

