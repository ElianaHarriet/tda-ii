#!/usr/bin/python3
import lib

GRAFO_CSV = "code/World.csv"
SEP = ','
ORIGEN_ARISTA = "Source"
DESTINO_ARISTA = "Target"
PESO_ARISTA = "ConexionAeropuertos"
CANT_ROLES = 4
ROLES_TXT = f"code/roles{CANT_ROLES}.txt"

# # # # # # # # # # #
#      Punto 6      #
# # # # # # # # # # #

def main():
    grafo = lib.cargar_grafo_nx(GRAFO_CSV, SEP, ORIGEN_ARISTA, DESTINO_ARISTA, PESO_ARISTA, False)
    print("Grafo cargado ✔")

    node_roles = lib.extraer_roles(grafo, CANT_ROLES)
    
    different_roles = list(set(node_roles.values()))
    different_roles.sort()
    with open(ROLES_TXT, 'w') as file:
        for role in different_roles:
            file.write(f'Nodos con rol {role}:\n')
            suma_grados = 0
            cant_nodos = 0
            for node in grafo.nodes:
                if node_roles[node] == role:
                    file.write(f'{node}, ')
                    suma_grados += grafo.degree[node]
                    cant_nodos += 1
            file.write(f'\nPromedio de grado: {suma_grados / cant_nodos}\n\n')
    
    print(f"Roles asignados y guardados en {ROLES_TXT} ✔")


if __name__ == "__main__":
    main()
