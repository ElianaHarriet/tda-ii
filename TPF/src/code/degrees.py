import statistics
# import networkx as nx
import lib

GRAPH_CSV_PATH = "TPF/src/asoiaf-all-edges.csv"

def degrees_quantity(graph):
    degrees = {}
    for v in graph.nodes():
        d = graph.degree(v)
        degrees[d] = degrees.get(d, 0) + 1
    return degrees


def degrees(graph):
    degrees = degrees_quantity(graph)
    keys_vector = [k for k, v in degrees.items() for i in range(v)]

    min_degree =  min(degrees.keys())
    max_degree = max(degrees.keys())
    avg_degree = sum([k * v for k, v in degrees.items()]) / graph.number_of_nodes()
    median_degree = statistics.median(keys_vector)

    return min_degree, max_degree, avg_degree, median_degree

def main():
    print("Loading graph...")
    graph = lib.load_nx_graph(GRAPH_CSV_PATH, ",", "Source", "Target", "weight", False)
    print("Graph loaded successfully")
    print("Calculating degrees...")
    min_degree, max_degree, avg_degree, median_degree = degrees(graph)
    print("Degrees calculated successfully")
    print(f" -> Minimum degree: {min_degree}")
    print(f" -> Maximum degree: {max_degree}")
    print(f" -> Average degree: {round(avg_degree, 3)}")
    print(f" -> Median degree: {median_degree}")

if __name__ == "__main__":
    main()