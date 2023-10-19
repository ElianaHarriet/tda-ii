import grafo
import csv
import networkx as nx
import random
from graphrole import RecursiveFeatureExtractor, RoleExtractor

def cargar_grafo(path, sep, origen, destino, peso, dirigido):
    """
    Crea un grafo dado un csv con forma de lista de aristas
    Parámetros:
     - Path del csv
     - Separador de columnas
     - Nombre de la columna de origen
     - Nombre de la columna de destino
     - Nombre de la columna de peso
     - Si el grafo es dirigido
    """
    g = grafo.Grafo(dirigido)
    with open(path, newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=sep)
        for row in reader:
            if not g.vertice_pertenece(row[origen]):
                g.agregar_vertice(row[origen])
            if not g.vertice_pertenece(row[destino]):
                g.agregar_vertice(row[destino])
            g.agregar_arista(row[origen], row[destino], int(row[peso]))
    return g

def cargar_grafo_nx(path, sep, origen, destino, peso, dirigido):
    g = nx.DiGraph() if dirigido else nx.Graph()
    with open(path, newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=sep)
        for row in reader:
            if not g.has_node(row[origen]):
                g.add_node(row[origen])
            if not g.has_node(row[destino]):
                g.add_node(row[destino])
            g.add_edge(row[origen], row[destino], weight=int(row[peso]))
    return g

def grados(grafo):
    grados = {}
    for v in grafo.obtener_vertices():
        grados[v] = len(grafo.adyacentes(v))
    return grados


def generar_erdos_renyi(original, cant_nodos):
    cant_aristas = original.cantidad_aristas()
    aristas_posibles = cant_nodos * (cant_nodos - 1)
    if not original.es_dirigido():
        aristas_posibles = aristas_posibles // 2
    proba = cant_aristas / aristas_posibles
    
    # return nx.erdos_renyi_graph(cant_nodos, proba)

    grafo_er = grafo.Grafo(original.es_dirigido())
    for i in range(cant_nodos):
        grafo_er.agregar_vertice(i)
    for i in range(cant_nodos):
        for j in range(i + 1, cant_nodos):
            if random.random() < proba:
                grafo_er.agregar_arista(i, j)

    return grafo_er

def generar_preferential_attachment(original, cant_nodos):
    original_grados = grados(original)
    grado_promedio = round(sum(original_grados.values()) / len(original_grados))

    if cant_nodos < grado_promedio:
        raise ValueError("La cantidad de nodos debe ser mayor al grado promedio")
    
    # return nx.barabasi_albert_graph(cant_nodos, grado_promedio)

    grafo_pa = grafo.Grafo(False)

    for i in range(grado_promedio):
        grafo_pa.agregar_vertice(i)
        for j in range(i):
            grafo_pa.agregar_arista(i, j)
    
    for i in range(grado_promedio, cant_nodos):
        grafo_pa.agregar_vertice(i)
        pa_grados = grados(grafo_pa)
        nodos = list(pa_grados.keys())
        probabilidades = [pa_grados[nodo] for nodo in nodos]
        total_grados = sum(probabilidades)
        probabilidades = [p / total_grados for p in probabilidades]
        adyacentes = random.choices(nodos, probabilidades, k=grado_promedio)

        for ady in adyacentes:
            grafo_pa.agregar_arista(i, ady)
    
    return grafo_pa

def all_anonymous_walks(grafo, n):
    walks = all_walks(grafo, n)
    _anonymous_walks = {}
    for w in walks:
        walk = []
        visitados = {}
        for v in w:
            visitados[v] = visitados.get(v, len(visitados))
            walk.append(visitados[v])
        _anonymous_walks[str(walk)] = _anonymous_walks.get(str(walk), 0) + 1

    return _anonymous_walks

def all_walks(grafo, n):
    walks = {}

    for i in range(1, n + 1):
        walks[i] = {}
        for v in grafo.obtener_vertices():
            walks[i][v] = []
            if i == 1:
                walks[i][v] = [[v]]
                continue
            for w in grafo.adyacentes(v):
                walks_w = walks[i - 1][w]
                for walk in walks_w:
                    walks[i][v] += [[v] + walk]

    walks_n = []
    for v in grafo.obtener_vertices():
        walks_n += walks[n][v]
    
    return walks_n

def extraer_roles(grafo, n_roles):
    # Se extraen las características principales del grafo
    feature_extractor = RecursiveFeatureExtractor(grafo)
    features = feature_extractor.extract_features()

    # Se calculan los roles para cada nodo
    role_extractor = RoleExtractor(n_roles)
    role_extractor.extract_role_factors(features)
    node_roles = role_extractor.roles
    print('\nNode role membership by percentage:')
    print(role_extractor.role_percentage.round(2))
    return node_roles