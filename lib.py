import grafo
import csv
from collections import deque
import networkx as nx
import random

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

def bfs(grafo, origen, destino = None, n = None):
    """
    Busca los caminos minimos dado un vértice de origen
     - En caso de que se especifique un destino, se corta la busqueda
       cuando se encuentra el camino minimo hasta el destino
     - En caso de que se especifique un n, se corta la busqueda cuando
       ya se encontraron todos los caminos de longitud n
    """
    visitados = set()
    padres = {}
    orden = {}
    padres[origen] = None
    orden[origen] = 0

    visitados.add(origen)
    q = deque()
    q.append(origen)

    while len(q) > 0:
        v = q.popleft()
        for w in grafo.adyacentes(v):
            if w not in visitados:
                padres[w] = v
                orden[w] = orden[v] + 1
                visitados.add(w)
                q.append(w)

                if destino != None and w == destino:
                    return padres, orden
                if n != None and orden[w] > int(n):
                    return padres, orden

    return padres, orden

def armar_camino(padre, origen, destino):
    camino = []
    v = destino
    while v != origen:
        camino.append(v)
        v = padre[v]
    camino.append(origen)
    return camino[::-1]

def diametro(grafo):
    max_min_dist = 0
    inicio = None
    destino = None
    padres = None

    for v in grafo.obtener_vertices():
        padre, distancias = bfs(grafo, v)
        for w in distancias:
            if distancias[w] != None and distancias[w] > max_min_dist:
                max_min_dist = distancias[w]
                inicio = v
                destino = w
                padres = padre

    return armar_camino(padres, inicio, destino)

def grados(grafo):
    grados = {}
    for v in grafo.obtener_vertices():
        grados[v] = len(grafo.adyacentes(v))
    return grados

def clustering_v(grafo, vertice):
    adyacentes = grafo.adyacentes(vertice)
    if len(adyacentes) < 2:
        return 0
    suma = 0
    for v in adyacentes:
        for w in adyacentes:
            if w != v  and v != vertice and grafo.estan_unidos(v, w):
                suma += 1
    return float(format(suma / (len(adyacentes) * (len(adyacentes) - 1)), '.3f'))

def cant_triplets(grafo):
    open_triplets = set()
    closed_triplets = set()
    for v in grafo.obtener_vertices():
        adyacentes = grafo.adyacentes(v)
        if len(adyacentes) < 2:
            continue
        for w in adyacentes:
            if v == w:
                continue
            for u in adyacentes:
                if u == v or u == w:
                    continue
                if not grafo.estan_unidos(w, u):
                    open_triplets.add(tuple(sorted((v, w, u))))
                else:
                    closed_triplets.add(tuple(sorted((v, w, u))))
    return open_triplets, closed_triplets

def clustering(grafo):
    open_triplets, closed_triplets = cant_triplets(grafo)
    if len(closed_triplets) == 0:
        return 0
    return float(format(len(closed_triplets) / (len(closed_triplets) + len(open_triplets)), '.3f'))

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
        if len(w) < n:
            continue
        # walk = ""
        walk = []
        visitados = {}
        for v in w:
            visitados[v] = visitados.get(v, len(visitados))
            walk.append(visitados[v])
        _anonymous_walks[str(walk)] = _anonymous_walks.get(str(walk), 0) + 1

    return _anonymous_walks

def walk_from(grafo, v, n):
    if n == 0:
        return []
    if n == 1:
        return [[v]]
    
    walks_v = []
    for w in grafo.adyacentes(v):
        walks_w = walk_from(grafo, w, n - 1)
        for walk in walks_w:
            if len(walk) < n - 1:
                continue
            walks_v += [[v] + walk]
    
    return walks_v

def all_walks(grafo, n):
    walks = []
    for v in grafo.obtener_vertices():
        walks += walk_from(grafo, v, n)
    return walks