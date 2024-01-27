import lib
import networkx as nx

GRAPH_CSV_PATH = "TPF/src/asoiaf-all-edges.csv"
COLORS_PATH = "TPF/src/gephi/colors_by_clusters.txt"

def get_group_assignments(groups):
    assignments = {}
    for k, v in groups.items():
        for node in v:
            assignments[node] = k
    return assignments

def get_clusters_relations(graph, groups, weighted=False):
    rel_graph = nx.Graph()
    groups_transposed = get_group_assignments(groups)
    top_nodes = {}
    for k, v in groups.items():
        top_nodes[k] = lib.get_top_nodes(graph, v, 1)[0]
        rel_graph.add_node(top_nodes[k])

    edges = set()
    for edge in graph.edges(data=True):
        source = edge[0]
        target = edge[1]
        if (source, target) in edges:
            continue # We already added this edge (works because the graph is undirected)
        edges.add((source, target))
        edges.add((target, source))
        weight = edge[2]["weight"]
        top_node_source = top_nodes[groups_transposed[source]]
        top_node_target = top_nodes[groups_transposed[target]]
        if top_node_source != top_node_target:
            if not rel_graph.has_edge(top_node_source, top_node_target):
                rel_graph.add_edge(top_node_source, top_node_target, weight=weight)
            else:
                rel_graph[top_node_source][top_node_target]["weight"] += weight if weighted else 1

    return rel_graph

def main():
    print("Loading graph...")
    groups = lib.get_groups(COLORS_PATH)
    graph = lib.load_nx_graph(GRAPH_CSV_PATH, ",", "Source", "Target", "weight", False)
    print("Graph loaded successfully")

    print("Generating clusters relations graph...")
    rel_graph = get_clusters_relations(graph, groups)
    rel_graph_weighted = get_clusters_relations(graph, groups, True)
    print("Clusters relations graph generated successfully")

    print("Saving clusters relations graphs...")
    lib.nx_graph_to_csv(rel_graph, "TPF/src/clusters_relations.csv", ",", "Source", "Target", "weight")
    lib.nx_graph_to_csv(rel_graph_weighted, "TPF/src/clusters_relations_weighted.csv", ",", "Source", "Target", "weight")
    print("Clusters relations graphs saved successfully, you can find them at " + \
          "TPF/src and then import it to Gephi")

if __name__ == "__main__":
    main()
    
    