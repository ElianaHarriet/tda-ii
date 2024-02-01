#!/usr/bin/python3
# import grafo as grafo
import lib as lib
from scipy.spatial import distance

OPCIONES = {"TODO": ("TPF/src/asoiaf-all-edges.csv", "weight"),
            "SELECTOS": ("TPF/src/asoiaf-selected.csv", "Weight")}

GRAFO_CSV, PESO_ARISTA = OPCIONES["SELECTOS"] # Elegir a conveniencia
SEP = ','
ORIGEN_ARISTA = "Source"
DESTINO_ARISTA = "Target"
CANT_NODOS_WALKS = 4 # con 5 la queda mi pc
TAM_MODELADO = 100

# # # # # # # # # # # # # # # # # # # #
#       Tomado del punto 4 - TP1      #
# # # # # # # # # # # # # # # # # # # #

def main():
    grafo = lib.cargar_grafo(GRAFO_CSV, SEP, ORIGEN_ARISTA, DESTINO_ARISTA, PESO_ARISTA, False)
    print("Grafo cargado ✔")

    grafo_er = lib.generar_erdos_renyi(grafo, TAM_MODELADO)
    print("Simulación de un modelado de Erdös-Rényi ✔")
    grafo_pa = lib.generar_preferential_attachment(grafo, TAM_MODELADO)
    print("Simulación de un modelado de Preferential Attachment (ley de potencias) ✔")

    all_walks = lib.all_anonymous_walks(grafo, CANT_NODOS_WALKS)
    total = sum(all_walks.values())
    prob = []
    print(f"Representación de anonymous walks de la red original (largo de {CANT_NODOS_WALKS} nodos) ✔")
    
    all_walks_er = lib.all_anonymous_walks(grafo_er, CANT_NODOS_WALKS)
    total_er = sum(all_walks_er.values())
    prob_er = []
    print(f"Representación de anonymous walks del modelado de Erdös-Rényi (largo de {CANT_NODOS_WALKS} nodos) ✔")

    all_walks_pa = lib.all_anonymous_walks(grafo_pa, CANT_NODOS_WALKS)
    total_pa = sum(all_walks_pa.values())
    prob_pa = []
    print(f"Representación de anonymous walks del modelado de Preferential Attachment (largo de {CANT_NODOS_WALKS} nodos) ✔")

    walks = set(all_walks.keys()) | set(all_walks_er.keys()) | set(all_walks_pa.keys())

    for w in walks:
        times = all_walks.get(w, 0)
        times_er = all_walks_er.get(w, 0)
        times_pa = all_walks_pa.get(w, 0)
        prob.append(times / total)
        prob_er.append(times_er / total_er)
        prob_pa.append(times_pa / total_pa)
    
    dist_coseno_er = distance.cosine(prob, prob_er)
    print(f"Distancia coseno entre la red original y el modelado de Erdös-Rényi: {dist_coseno_er}")
    dist_coseno_pa = distance.cosine(prob, prob_pa)
    print(f"Distancia coseno entre la red original y el modelado de Preferential Attachment: {dist_coseno_pa}")




if __name__ == "__main__":
    main()
