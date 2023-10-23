#!/usr/bin/python3
import lib

GRAFO_CSV = "code/World.csv"
SEP = ','
ORIGEN_ARISTA = "Source"
DESTINO_ARISTA = "Target"
PESO_ARISTA = "ConexionAeropuertos"
PUENTES_GLOBALES_TXT = "code/global.txt"
PUENTES_LOCALES_TXT = "code/local.txt"
# # # # # # # # # # #
#      Punto 6      #
# # # # # # # # # # #

def main():
    grafo = lib.cargar_grafo_nx(GRAFO_CSV, SEP, ORIGEN_ARISTA, DESTINO_ARISTA, PESO_ARISTA, False)
    print("Grafo cargado ✔")

    puentes_globales = lib.extraer_puentes_globales(grafo)
    
    with open(PUENTES_GLOBALES_TXT, 'w') as file:
        for bridge in puentes_globales:
            file.write(f'Puentes Globales:\n')
            file.write(f'Puente: {bridge}\n')
    
    print(f"Puentes globales guardados en {PUENTES_GLOBALES_TXT} ✔")

    puentes_locales = lib.extraer_puentes_locales(grafo)

    with open(PUENTES_LOCALES_TXT, 'w') as file:
        for bridge in puentes_locales:
            file.write(f'Puentes Locales:\n')
            file.write(f'Puente: {bridge}\n')
    
    print(f"Puentes locales guardados en {PUENTES_LOCALES_TXT} ✔")



if __name__ == "__main__":
    main()
