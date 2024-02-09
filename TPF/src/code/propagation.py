import lib
import random

INITIAL_NODE = "Daenerys-Targaryen"
INFECTION_PROB = 0.025
RECOVERY_PROB = 0.05
DYING_PROB = 0.025

GRAPH_CSV_PATH = "TPF/src/csvs/asoiaf-all-edges.csv"
PARAMS = f"{INITIAL_NODE}|I{INFECTION_PROB}|R{RECOVERY_PROB}|D{DYING_PROB}"
RESULT_PATH = f"TPF/src/csvs/propagation_result({PARAMS}).csv"
COL_NAME = "Status"

SUCEPTIBLE = "Suceptible"
INFECTED = "Infected"
RECOVERED = "Recovered"
DEAD = "Dead"
ITERATIONS = 20

def simulate_virus(nx_graph):
    status = {node: SUCEPTIBLE for node in nx_graph.nodes()}
    status[INITIAL_NODE] = INFECTED

    status_count = {SUCEPTIBLE: 0, INFECTED: 0, RECOVERED: 0, DEAD: 0}
    status_count[INFECTED] = 1
    status_count[SUCEPTIBLE] = len(nx_graph.nodes()) - 1

    for _ in range(ITERATIONS):
        if status_count[INFECTED] == 0:
            break

        for node in nx_graph.nodes():
            if status[node] == INFECTED:
                
                for neighbor in nx_graph.neighbors(node):
                    if status[neighbor] == SUCEPTIBLE and random.random() < INFECTION_PROB:                      
                        prev_status = status[neighbor]
                        status[neighbor] = INFECTED
                        status_count[prev_status] -= 1
                        status_count[INFECTED] += 1
                        # print(f"{neighbor} infected by {node}")
                
                if random.random() < RECOVERY_PROB:
                    status[node] = RECOVERED
                    status_count[INFECTED] -= 1
                    status_count[RECOVERED] += 1
                    # print(f"{node} recovered")
                elif random.random() < DYING_PROB:
                    status[node] = DEAD
                    status_count[INFECTED] -= 1
                    status_count[DEAD] += 1
                    # print(f"{node} died")

    return status, status_count

def main():
    print("Loading graph...")
    graph = lib.load_nx_graph(GRAPH_CSV_PATH, ",", "Source", "Target", "weight", False)
    print("Graph loaded successfully")
    
    print("Simulating virus propagation...")
    status, status_count = simulate_virus(graph)
    print(f"Status count: {status_count}")
    print("Virus propagation simulated successfully")

    print("Saving results...")
    lib.save_status(RESULT_PATH, status, COL_NAME)
    print("Results saved successfully")

if __name__ == "__main__":
    main()