import lib

GRAPH_CSV_PATH = "TPF/src/csvs/asoiaf-all-edges.csv"
COLORS_PATH = "TPF/src/gephi/colors_by_clusters.txt"
TOP_NODES = 10

def main():
    print("Loading graph...")
    groups_dict = lib.get_groups(COLORS_PATH)
    groups = list(groups_dict.values())
    graph = lib.load_nx_graph(GRAPH_CSV_PATH, ",", "Source", "Target", "weight", False)
    print("Graph loaded successfully")
    
    print(f"Number of groups: {len(groups)}")
    avg = round(sum([len(group) for group in groups]) / len(groups), 3)
    print(f"Average number of nodes per group: {avg}")
    print(f"Max number of nodes per group: {max([len(group) for group in groups])}")
    print(f"Min number of nodes per group: {min([len(group) for group in groups])}")
    print("::Groups::")
    for i in range(len(groups)):
        print(f"Group {i+1} ({len(groups[i])} nodes)")
        if len(groups[i]) > TOP_NODES:
            print(f"\tTop {TOP_NODES} nodes:")
        else:
            print("\tNodes:")
        nodes = "\n\t - ".join(lib.get_top_nodes(graph, groups[i], TOP_NODES))
        print(f"\t - {nodes}")

if __name__ == "__main__":
    main()