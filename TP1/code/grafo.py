import random

class Grafo:
    
    def __init__(self, esdirigido = True):
        self.vertices = set()
        self.adyacencias = {}
        self.esdirigido = esdirigido
    
    def es_dirigido(self):
        return self.esdirigido
    
    def agregar_vertice(self, v):
        if self.vertice_pertenece(v):
            raise ValueError("El vertice ya existe")
        self.vertices.add(v)
        self.adyacencias[v] = {}
    
    def borrar_vertice(self,v):
        if not self.vertice_pertenece(v):
            raise ValueError("El vertice no existe")
        self.vertices.remove(v)
        del self.adyacencias[v]
        for w in self.vertices:
            if v in self.adyacencias[w]:
                del self.adyacencias[w][v]
        
    def obtener_vertices(self):
        return self.vertices
    
    def cantidad_vertices(self):
        return len(self.vertices)
    
    def cantidad_aristas(self):
        total = sum(len(self.adyacencias[v]) for v in self.vertices)
        if not self.esdirigido:
            total = total // 2
        return total
    
    def vertice_pertenece(self, v):
        return v in self.vertices
    
    def borrar_arista(self, v, w):
        if (self.estan_unidos(v, w)):
            del self.adyacencias[v][w]
            if not self.esdirigido:
                    del self.adyacencias[w][v]           
        
    def agregar_arista(self, v, w, peso = 1):    
        self.adyacencias[v][w] = peso
        if not self.esdirigido:
            self.adyacencias[w][v] = peso
    
    def estan_unidos(self, v, w):
        return w in self.adyacencias[v]

    def peso_arista(self, v, w):
        if self.estan_unidos(v, w):
            return self.adyacencias[v][w]
    
    def adyacentes(self, v):
        return list(self.adyacencias[v])
    
    def vertice_aleatorio(self):
        return random.choice(self.vertices)
    
    def __str__(self):
        return str(self.adyacencias)