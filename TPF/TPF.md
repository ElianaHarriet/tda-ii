# Teoría de Algoritmos II (75.30)
## Trabajo Práctico Final

### Integrantes
- [107205 - Eliana Harriet](https://github.com/ElianaHarriet)
- [107754 - Marcos Bat Mentzel](https://github.com/marcosbatm)

### Origen de los datos
Los datos utilizados para la realización del trabajo práctico fueron obtenidos del repositorio de GitHub [mathbeveridge/asoiaf](https://github.com/mathbeveridge/asoiaf/blob/master/data/asoiaf-all-edges.csv). Puntualmente, se utilizó el csv que genera el grafo con todas las aristas a lo largo de todos los libros de la saga (exactamente el archivo al que dirige el link).  
Tal como dice el README del repositorio, una arista conecta dos personajes cada vez que sus nombres (o apodos) aparecían con una diferencia de hasta 15 palabras entre sí en uno de los libros de "Canción de hielo y fuego". El peso de la arista corresponde al número de interacciones.  

### A song of ice and fire
A Song of Ice and Fire es una saga de novelas de fantasía épica escrita por el autor estadounidense George R. R. Martin. Si bien la saga se encuentra inconclusa, hasta el momento el tronco principal de la historia se compone de 5 libros: A Game of Thrones, A Clash of Kings, A Storm of Swords, A Feast for Crows y A Dance with Dragons. A lo largo de dichos libros se narra una historia en donde hubo lugar a muchos giros importantes en la historia, como cambios de bando, asesinatos, traiciones y demas eventos que permite una red de personajes lo suficientemente compleja como para ser analizada.  

### Objetivo
La saga de A Song of Ice and Fire cuenta con una gran cantidad de personajes y sucesos, derivando en una baja probabilidad de preveer que sucederá en el futuro. Sin embargo, es posible analizar la red de personajes y sus interacciones para obtener información sobre la misma.  
De esta forma, el objetivo del trabajo práctico es analizar la red de personajes de la saga a fin de obtener información relevante ya sea a modo compañamiento de la lectura de los libros o para obtener información extra que pudo haber pasado desapercibida.

> **Aviso de Spoilers**: El trabajo práctico contiene información sobre los libros de la saga, por lo que se recomienda no leerlo si no se leyeron todos los libros publicados hasta el momento.




