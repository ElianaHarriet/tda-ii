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

def nx_graph_to_csv(graph, path, sep, source, target, weight):
    with open(path, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=[source, target, weight], delimiter=sep)
        writer.writeheader()
        for edge in graph.edges(data=True):
            writer.writerow({source: edge[0], target: edge[1], weight: edge[2][weight]})

def get_top_nodes(graph, group, top_nodes):
    nodes = []
    for node in group:
        nodes.append((node, graph.degree(node)))
    nodes.sort(key=lambda x: x[1], reverse=True)
    nodes = list(map(lambda x: x[0], nodes))
    return nodes[:top_nodes]

def get_groups(path):
    groups = {}
    with open(path, 'r') as f:
        for line in f:
            name, group = line.split(":rgb:")
            group = group.replace("\n", "")
            groups[group] = groups.get(group, []) + [name]
    return groups