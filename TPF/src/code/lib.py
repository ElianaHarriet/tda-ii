import csv
import networkx as nx

def load_nx_graph(path, sep, source, target, weight, directed):
    g = nx.DiGraph() if directed else nx.Graph()
    with open(path, newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=sep)
        for row in reader:
            if not g.has_node(row[source]):
                g.add_node(row[source])
            if not g.has_node(row[target]):
                g.add_node(row[target])
            g.add_edge(row[source], row[target], weight=int(row[weight]))
    return g