#!/usr/bin/python3
import lib


OPCIONES = {"TODO": ("TPF/src/asoiaf-all-edges.csv", "weight"),
            "SELECTOS": ("TPF/src/asoiaf-selected.csv", "Weight")}

OPCION = "SELECTOS" # Elegir a conveniencia
GRAFO_CSV, PESO_ARISTA = OPCIONES[OPCION]
SEP = ','
ORIGEN_ARISTA = "Source"
DESTINO_ARISTA = "Target"
CANT_ROLES = None # Elegir a conveniencia
ROLES_TXT = f"TPF/src/code/old_tps/roles{OPCION}{CANT_ROLES if CANT_ROLES else '-auto'}.txt"

# # # # # # # # # # # # # # # # # # # #
#       Tomado del punto 6 - TP1      #
# # # # # # # # # # # # # # # # # # # #

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
