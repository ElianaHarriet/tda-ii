#!/usr/bin/python3
import grafo
import lib
from graphrole import RecursiveFeatureExtractor, RoleExtractor
import networkx as nx
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
import random
from scipy.spatial import distance

grafo_csv = "World.csv"

def main():
    print("Cargando grafo...")
    grafo = lib.cargar_grafo(grafo_csv, ',', 'Source', 'Target', 'ConexionAeropuertos', False)
    grafo_nx = lib.cargar_grafo_nx(grafo_csv, ',', 'Source', 'Target', 'ConexionAeropuertos', False)
    print("Grafo cargado")
    
    # Cálculos para el punto 1
    print("Cantidad de vertices: ", grafo.cantidad_vertices())
    print("Cantidad de aristas: ", grafo.cantidad_aristas())
    diametro = lib.diametro(grafo)
    print("Diametro: ", len(diametro), " - ", diametro)
    grados = lib.grados(grafo)
    grado_promedio = round(sum(grados.values()) / len(grados), 2)
    print("Grado promedio: ", grado_promedio)
    print("Coef clustering:", lib.clustering(grafo))

    # Punto 4

    # simulación de un modelado de Erdös-Rényi
    grafo_er = lib.generar_erdos_renyi(grafo, 100)
    grafo_pa = lib.generar_preferential_attachment(grafo, 100)

    n = 4

    all_walks = lib.all_anonymous_walks(grafo, n)
    total = sum(all_walks.values())
    prob = []
    
    all_walks_er = lib.all_anonymous_walks(grafo_er, n)
    total_er = sum(all_walks_er.values())
    prob_er = []

    all_walks_pa = lib.all_anonymous_walks(grafo_pa, n)
    total_pa = sum(all_walks_pa.values())
    prob_pa = []

    walks = set(all_walks.keys()) | set(all_walks_er.keys()) | set(all_walks_pa.keys())

    for w in walks:
        times = all_walks.get(w, 0)
        times_er = all_walks_er.get(w, 0)
        times_pa = all_walks_pa.get(w, 0)
        prob.append(times / total)
        prob_er.append(times_er / total_er)
        prob_pa.append(times_pa / total_pa)
    
    dist_coseno_er = distance.cosine(prob, prob_er)
    print(f"Distancia de coseno entre original y erdos_renyi: {dist_coseno_er}")
    dist_coseno_pa = distance.cosine(prob, prob_pa)
    print(f"Distancia de coseno entre original y preferential_attachment: {dist_coseno_pa}")

    # # Cálculos para el punto 6
    # # extract features
    # feature_extractor = RecursiveFeatureExtractor(grafo_nx)
    # features = feature_extractor.extract_features()
    # print(f'\nFeatures extracted from {feature_extractor.generation_count} recursive generations:')
    # print(features)
    # # assign node roles
    # role_extractor = RoleExtractor(n_roles=None)
    # role_extractor.extract_role_factors(features)
    # node_roles = role_extractor.roles
    # print('\nNode role assignments:')
    # print(node_roles)
    # print('\nNode role membership by percentage:')
    # print(role_extractor.role_percentage.round(2))
    # # build color palette for plotting
    # unique_roles = sorted(set(node_roles.values()))
    # color_map = sns.color_palette('Paired', n_colors=len(unique_roles))
    # # map roles to colors
    # role_colors = {role: color_map[i] for i, role in enumerate(unique_roles)}
    # # build list of colors for all nodes in grafo_nx
    # node_colors = [role_colors[node_roles[node]] for node in grafo_nx.nodes]

    # # plot graph
    # plt.figure()
    # with warnings.catch_warnings():
    #     # catch matplotlib deprecation warning
    #     warnings.simplefilter('ignore')
    #     nx.draw(
    #         grafo_nx,
    #         pos=nx.spring_layout(grafo_nx, seed=42),
    #         with_labels=True,
    #         node_color=node_colors,
    #     )

    # # Guardar la figura en un archivo
    # plt.savefig('roles-fig.png')
    # # Cerrar la figura para liberar memoria
    # plt.close()

    # # Para cada nodo, imprimir su rol
    # path = f'roles-nodes.txt'
    # different_roles = list(set(node_roles.values()))
    # different_roles.sort()
    # nodes = 0
    # with open(path, 'w') as file:
    #     for role in different_roles:
    #         file.write(f'Nodos con rol {role}:\n')
    #         for node in grafo_nx.nodes:
    #             if node_roles[node] == role:
    #                 file.write(f'{node}, ')
    #                 nodes += 1
    #         file.write('\n\n')
    # print(f'Cantidad de nodos: {nodes}')




if __name__ == "__main__":
    main()
