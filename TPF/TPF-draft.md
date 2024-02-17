# Teoría de Algoritmos II (75.30)
## Trabajo Práctico Final

[107205 - Eliana Harriet](https://github.com/ElianaHarriet)

### Origen de los datos

![aosiaf](src/images/asoiaf.jpg)

Los datos utilizados para la realización del trabajo práctico fueron obtenidos del repositorio de GitHub [mathbeveridge/asoiaf](https://github.com/mathbeveridge/asoiaf/blob/master/data/asoiaf-all-edges.csv). Puntualmente, se utilizó el csv que genera el grafo con todas las aristas a lo largo de todos los libros de la saga (exactamente el archivo al que dirige el link).  
Tal como dice el README del repositorio, una arista conecta dos personajes cada vez que sus nombres (o apodos) aparecían con una diferencia de hasta 15 palabras entre sí en uno de los libros de "Canción de hielo y fuego". El peso de la arista corresponde al número de interacciones.  

### A song of ice and fire
A Song of Ice and Fire es una saga de novelas de fantasía épica escrita por el autor estadounidense George R. R. Martin. Si bien la saga se encuentra inconclusa, hasta el momento el tronco principal de la historia se compone de 5 libros: A Game of Thrones, A Clash of Kings, A Storm of Swords, A Feast for Crows y A Dance with Dragons. A lo largo de dichos libros se narra una historia en donde hubo lugar a muchos giros importantes en la historia, como cambios de bando, asesinatos, traiciones y demas eventos que permite una red de personajes lo suficientemente compleja como para ser analizada.  

![Mapa del mundo conocido](src/images/tkw.jpg)

### Objetivo
La saga de A Song of Ice and Fire cuenta con una gran cantidad de personajes y sucesos, derivando en una baja probabilidad de preveer que sucederá en el futuro. Sin embargo, es posible analizar la red de personajes y sus interacciones para obtener información sobre la misma.  
De esta forma, el objetivo del trabajo práctico es analizar la red de personajes de la saga a fin de obtener información relevante ya sea a modo compañamiento de la lectura de los libros o para obtener información extra que pudo haber pasado desapercibida.

> **Aviso de Spoilers**: El trabajo práctico contiene información sobre los libros de la saga, por lo que se recomienda no leerlo si no se leyeron todos los libros publicados hasta el momento.

---

## Análisis de la red de personajes

![Grafo coloreado según grados](src/images/graph_by_connections.png)

Se trata de un grafo no dirigido con 796 nodos (personajes) y 2823 aristas (apariciones cercanas en los libros). Además, la densidad de la red es de 0.009, lo cual nos demuestra que la red es bastante dispersa.  

Al momento de calcular información respectiva a los grados del grafo se puede obtener lo siguiente:
```
 -> Minimum degree: 1
 -> Maximum degree: 122
 -> Average degree: 7.093
 -> Median degree: 3.0
```
Se puede observar que el grado promedio es mayor al grado mediano, lo que indica que la distribución de los grados no es simétrica. Esto significa que la mitad de los nodos tienen un grado menor o igual a 3, lo cual es bastante bajo y, sumado a que el promedio de grados es de 7, se puede ver la disparidad entre las conexiones de los personajes.  

El diámetro de la red es de 9, algo llamativo para una red tan grande de personajes. En los libros se plantea que el mundo es muy grande y que los personajes se encuentran muy lejos unos de otros (lo cual se condice con la densidad obtenida), además de aparentar tener burbujas bastante aisladas y tenemos el dato recién obtenido sobre la gran cantidad de nodos poco conectados. Sin embargo, el diámetro de la red es muy bajo, lo que indica que cada conexión en sí adquiera mayor importancia, permitiendo que la información viaje de un lado a otro con relativa facilidad.  

## Las casas de Westeros y agrupaciones de personajes

![Houses](src/images/houses.jpg)

### Análisis de clusters en la red

Al principio de la saga se nos plantean distintas casas, cada una con sus características, fortalezas, miembros ubicaciones y alianzas. Uno podría pensar que las casas son un grupo de personajes que se encuentran muy conectados entre sí, pero la realidad es que no es así, a medida que avanza la historia la única constante es ir perdiendo o separando miembros de las casas. Esto último puede verse en el siguiente gráfico:  

![Modularity clases by gephy](src/images/graph_by_clusters.png)
El grafo presentado es un grafo coloreado según el cluster al que pertenece cada personaje, siendo la cantidad de grupos y el grupo a asignar determinado por el algoritmo de Louvain (hecho mediante herramientas de gephi).  
La gran cantidad de colores no sorprende, en principio uno puede pensar que se debe a la gran cantidad de personajes que la saga presenta, o a la extensión del mapa sobre el que ocurre. Pero viendo un poco más allá, no sólo se ven los personajes agrupacos por cercanía a lo largo de la historia, sino que también se puede ver como cada color puede representar un centro importante sobre el que se desarrolla la historia.  

La siguiente es una lista de los nodos más importantes por grupo:
```
Number of groups: 15
Average number of nodes per group: 53.067
Max number of nodes per group: 197
Min number of nodes per group: 2
::Groups::
Group 1 (53 nodes)
        Top 10 nodes:
         - Jaime-Lannister
         - Brienne-of-Tarth
         - Randyll-Tarly
         - Addam-Marbrand
         - Podrick-Payne
         - Vargo-Hoat
         - Hyle-Hunt
         - Cleos-Frey
         - Shagwell
         - Lyle-Crakehall
Group 2 (197 nodes)
        Top 10 nodes:
         - Tyrion-Lannister
         - Cersei-Lannister
         - Sansa-Stark
         - Eddard-Stark
         - Joffrey-Baratheon
         - Robert-Baratheon
         - Tywin-Lannister
         - Petyr-Baelish
         - Varys
         - Tommen-Baratheon
Group 3 (114 nodes)
        Top 10 nodes:
         - Jon-Snow
         - Samwell-Tarly
         - Mance-Rayder
         - Jeor-Mormont
         - Aemon-Targaryen-(Maester-Aemon)
         - Janos-Slynt
         - Eddison-Tollett
         - Bowen-Marsh
         - Pypar
         - Tormund
Group 4 (87 nodes)
        Top 10 nodes:
         - Daenerys-Targaryen
         - Barristan-Selmy
         - Jorah-Mormont
         - Hizdahr-zo-Loraq
         - Drogo
         - Quentyn-Martell
         - Daario-Naharis
         - Irri
         - Viserys-Targaryen
         - Belwas
Group 5 (66 nodes)
        Top 10 nodes:
         - Arya-Stark
         - Sandor-Clegane
         - Gregor-Clegane
         - Ilyn-Payne
         - Meryn-Trant
         - Amory-Lorch
         - Oberyn-Martell
         - Gendry
         - Beric-Dondarrion
         - Yoren
Group 6 (134 nodes)
        Top 10 nodes:
         - Catelyn-Stark
         - Robb-Stark
         - Theon-Greyjoy
         - Bran-Stark
         - Rodrik-Cassel
         - Roose-Bolton
         - Asha-Greyjoy
         - Edmure-Tully
         - Ramsay-Snow
         - Luwin
Group 7 (65 nodes)
        Top 10 nodes:
         - Stannis-Baratheon
         - Renly-Baratheon
         - Davos-Seaworth
         - Melisandre
         - Selyse-Florent
         - Wyman-Manderly
         - Shireen-Baratheon
         - Axell-Florent
         - Cressen
         - Godry-Farring
Group 8 (21 nodes)
        Top 10 nodes:
         - Doran-Martell
         - Arianne-Martell
         - Areo-Hotah
         - Arys-Oakheart
         - Tyene-Sand
         - Garin-(orphan)
         - Obara-Sand
         - Andrey-Dalt
         - Sylva-Santagar
         - Gerold-Dayne
Group 9 (11 nodes)
        Top 10 nodes:
         - Alleras
         - Pate-(novice)
         - Armen
         - Leo-Tyrell
         - Mollander
         - Roone
         - Marwyn
         - Walgrave
         - Gormon-Tyrell
         - Quill
Group 10 (32 nodes)
        Top 10 nodes:
         - Victarion-Greyjoy
         - Aeron-Greyjoy
         - Balon-Greyjoy
         - Euron-Greyjoy
         - Rodrik-Harlaw
         - Moqorro
         - Nute
         - Hotho-Harlaw
         - Baelor-Blacktyde
         - Red-Oarsman
Group 11 (3 nodes)
        Nodes:
         - Gared
         - Waymar-Royce
         - Will-(prologue)
Group 12 (2 nodes)
        Nodes:
         - Horas-Redwyne
         - Hobber-Redwyne
Group 13 (2 nodes)
        Nodes:
         - Florian-the-Fool
         - Jonquil
Group 14 (7 nodes)
        Nodes:
         - Gerold-Hightower
         - Arthur-Dayne
         - Lewyn-Martell
         - Oswell-Whent
         - Jonothor-Darry
         - Smiling-Knight
         - Simon-Toyne
Group 15 (2 nodes)
        Nodes:
         - Nyessos-Vhassar
         - Malaquo-Maegyr
```

- El grupo 1 se caracteriza por ser personajes de la zona de los ríos, en donde se desarrolla la historia de Jaime Lannister y Brienne de Tarth. Entre ellos, se pueden ver personajes de Harrenhal, lugar en donde se desarrolla uno de los puntos más críticos de Jaime y Brienne.  
- El grupo 2 se caracteriza por ser personajes de Desembarco del Rey, en donde se desarrolla la historia de la casa Lannister y la casa Baratheon. Es un grupo muy extenso debido a la alta cantidad de personajes que se encuentran en la capital, de los cuales muchos son de importancia y se encuentran asentados sin moverse por los siete reinos.  
- El grupo 3 se caracteriza por ser personajes de la Guardia de la Noche, en donde se desarrolla la historia de Jon Snow. Es un grupo relativamente extenso debido a la alta cantidad de personajes que se encuentran en el Muro y más allá del mismo. Si bien sus personajes no se mantienen en el muro debido a la expedición de Jon Snow, se puede ver como muchos de ellos se mantienen en el grupo debido a su relación con el mismo o por moverse en conjunto.  
- El grupo 4 se caracteriza por ser personajes de Essos, en donde se desarrolla la historia de Daenerys Targaryen. Si bien es un grupo má extenso que el promedio, no llega a ser tan grande como los anteriores debido a la larga travesía que emprende Daenerys, además de los asesinatos y traiciones que terminan por modificar sucesivamente al grupo.  
- El grupo 5 se caracteriza por ser personajes de distintas partes, muchos del centro-norte de Westeros, en donde se desarrolla la historia de Arya Stark. Si bien es un grupo de personajes en constante movimiento, es un grupo que casualmente vuelve a conectar a algunos de sus personajes a lo largo de la historia, o incluso conecta parsonajes con conocidos en común cerrando triángulos de forma muy particular.  
- El grupo 6 se caracteriza por ser personajes del norte de Westeros, en donde se desarrolla la historia de la casa Stark. Es un grupo extenso debido a que se trata de la coalición de Robb Stark, en donde se encuentran personajes de distintas casas que se unen a la causa de Robb como rey en el norte.  
- El grupo 7 se caracteriza por ser personajes de Rocadragón, en donde se desarrolla la historia de otra parte de la casa Baratheon, en particular de Stannis Baratheon. Es un grupo caracterizado por seguir a Stannis debido a ser la coalición de Stannis como rey de los siete reinos. A diferencia del grupo anterior, esta coalición no es muy diversa en casas y no tiene gran relación con personajes del exterior a menos que se trate de personajes que se unan o relacionen con Stannis.  
- El grupo 8 se caracteriza por ser personajes de Dorne, en donde se desarrolla la historia de la casa Martell. Es un grupo pequeño debido a que la casa Martell no tiene gran relación con el resto de las casas, y se encuentra en una posición geográfica que la mantiene aislada del resto de los reinos. Además, no aparece mucho tiempo en la historia.  
- El grupo 9 se caracteriza por ser personajes de la Ciudadela, en donde se desarrolla la historia de Samwell Tarly.  
- El grupo 10 se caracteriza por ser personajes de las Islas del Hierro, en donde se desarrolla la historia de la casa Greyjoy. Es un grupo que une a una única casa y sus aliados más cercanos, por lo que no es un grupo extenso.
- El grupo 11 se caracteriza por ser personajes de la Guardia de la Noche, particularmente son los tres personajes del prólogo del primer libro.  
- Del grupo 12 al 15 se caracterizan por ser personajes de la historia de Westeros, pero que no tienen gran relación con el resto de los personajes debido a ser personajes chicos que no tienen gran importancia en la historia.

Para ver la relación entre clusters, y dar mejor contexto a lo recién explicado, se hizo un nuevo grafo resultante de convertir a cada grupo en un nodo y conectarlos entre sí. Para el peso de las aristas se utilizó la suma de los pesos de las aristas que conectan a los nodos de cada grupo. El resultado es el siguiente:  
![clusters_graph](src/images/clusters_weighted.png)
En lugar de numerar los grupos, se puso como nombre del nodo al personaje con mayor cantidad de interacciones del grupo. Además, el grafo está presentado de forma que los vértices más anchos son los que tienen mayor peso y los nodos más grandes son los que tienen mayor grado.  
![clusters_graph_cantrality](src/images/clusters_weighted__eigenvector_centrality.png)
En esta versión del grafo se puede ver como un grupo de vértices tienen medida similar, esta se corresponde con la métrica de eigenvecor centrality, la cual es una medida de prestigio e influencia de un determinado nodo por sobre la red.  
Se puede ver que, si bien el grupo de los Lannister es el que tiene mayor grado, no es el que tiene mayor prestigio, sino que hay un conjunto de grupos con prestigio semejante. Esto permite que la historia continúe sin tener un grupo de personajes que se destaque por sobre el resto o que tenga mayor _suerte_ en el resultado de sus movimientos, sino que se trata de una red compleja en donde cada personaje y grupo tiene su importancia y su influencia en la historia sin haber un claro ganador del trono de hierro.

### Análisis particular: Los hermanos Stark

Para ver un poco más en detalle, vamos a analizar la primer casa que nos presentan en la saga, los Stark:
Esta casa es una familia noble del norte de Westeros, que gobierna en Invernalia y cuyo emblema es un lobo huargo. Dada la ubicación de la misma, se podría pensar que los miembros de la misma se encuentran muy conectados entre sí y desconectados del resto de los personajes, dado lo lejos que se encuentran de la capital y lo fuerte que resulta el invierno en el norte. Sin embargo, esto no es así, y tomaremos como ejemplo a los hermanos Stark:
- Robb Stark: es el hijo mayor de Eddard Stark y Catelyn Tully. Es el heredero de Invernalia y el Norte.
- Sansa Stark: es la segunda hija de Eddard Stark y Catelyn Tully.
- Arya Stark: es la tercera hija de Eddard Stark y Catelyn Tully.
- Bran Stark: es el cuarto hijo de Eddard Stark y Catelyn Tully.
- Rickon Stark: es el hijo menor de Eddard Stark y Catelyn Tully.
- Jon Snow: en principio es el hijo bastardo de Eddard Stark y una mujer desconocida.  

Al momento de ubicar a estos seis hermanos en el grafo podemos verlos de la siguiente forma:  
![stark-bros](src/images/stark.png)  
En donde el ancho de la arista representa la cantidad de interacciones entre los personajes y el color del nodo es el cluster al que pertenece.  
Se puede ver cómo los seis hermanos están en cuatro clusters distintos, lo cual nos indica que no se encuentran muy conectados entre sí. Además, se puede ver que algunas aristas son bastante delgadas, lo cual nos indica que no se encuentran muy conectados algunos pares de hermanos entre sí.  
Siguiendo sobre la trayectoria de estos hermanos, vamos a mencionar un punto clave al principio de la historia: la muerte de Eddard Stark y cómo llegaron los hermanos a la misma:  
Tras la visita del rey Robert Baratheon a Invernalia, Eddard Stark es nombrado Mano del Rey y se ve obligado a viajar a Desembarco del Rey junto a sus hijas Sansa y Arya. Por otro lado, Jon Snow se une a la Guardia de la Noche y se dirige al Muro. Robb, Bran y Rickon se quedan en Invernalia, Robb debido a que es el heredero de Invernalia y el Norte, y Bran y Rickon por ser muy jóvenes. Esto nos deja con los siguientes clusters:
- Arya y Sansa en Desembarco del Rey
- Bran, Rickon y Robb en Invernalia
- Jon Snow en el Muro  

Pero tras la muerte de Eddard Stark, la posición de Arya y Sansa se ve comprometida, por lo que Arya se ve obligada a huir de Desembarco del Rey y Sansa queda prisionera de la familia Lannister. La casa Stark intentará a lo largo de la historia recuperar a sus hijas, sin embargo este grafo es una clara demostración de cómo no sólo no fue posible, sino que además las hermanas se fueron separando cada vez más. Veamos las conexiones de cada una de ellas:  
![Sansa](src/images/sansa.png)
Este es el grafo de conexiones de Sansa Stark, en donde se puede ver que sus conexiones pertenecen mayoritariamente a un mismo cluster, lo cual nos indica que se encuentra muy conectada a un grupo de personajes en particular. Entre estos personajes, se puede ver una mayor presencia de personajes de la casa Lannister, lo cual se condice con la situación de Sansa en Desembarco del Rey y muestra como el retorno a su familia es un hecho con cada vez menos posibilidades debido al poco poder que tiene por sobre su entorno.  
![Arya](src/images/arya.png)
Este es el grafo de conexiones de Arya Stark, en donde se puede ver que sus conexiones se encuentran más dispersas que las de Sansa, en estas conexiones se puede ver una buena cantidad de personajes de Westeros, pero muchos otros de Essos, lo cual se condice con la situación de Arya, que tras la muerte de su padre se ve obligada a huir de Desembarco del Rey y ronda por Westeros y luego Essos. Además, se puede ver como muchos de los personajes tienen un grado bajo, lo cual indica que no son personajes muy importantes en la historia, lo cual se condice con la situación de Arya, que se encuentra huyendo de los Lannister y no tiene un lugar fijo en el mundo.  

Respecto a cada una de las subredes, vamos a eliminar a Sansa y Arya de ambas para realizar algunos cálculos:

|                                     | Entorno de Sansa | Entorno de Arya |
|-------------------------------------|------------------|-----------------|
| **Grado medio**                     | 11.865           | 8.819           |
| **Grado medio con pesos**           | 264.919          | 183.012         |
| **Diámetro de la red**              | 4                | 5               |
| **Densidad de la red**              | 0.163            | 0.108           |
| **Coeficiente medio de clustering** | 0.712            | 0.617           |
| **Longitud media de camino**        | 2.117            | 2.191           |

Con estas métricas se pueden notar dos diferencias cruciales entre ambas redes:

- **Importancia de los nodos** (métricas a tener en cuenta: grado medio, grado medio con pesos)  
Viendo los grados promedio de ambas redes se ve una diferencia muy grande, siendo los personajes del entorno de Sansa unos personajes de gran importancia. Esto puede traducirse a personajes con relativo gran poder, al ver los nombres se puede ver que en su mayoría son Lannisters, lo cual valida la hipótesis. De esta forma, se puede ver que el entorno de Sansa es un entorno de personajes peligroso en el cual cada decisión que tome Sansa puede ser crucial para su futuro y la supervivencia a lo largo de la historia.  
Es una gran diferencia con las métricas para el entorno de Arya, en donde se puede ver un grado promedio mucho más bajo, pudiendo entonces dar más posibilidades a Arya de influir en su entorno y tomar decisiones más asertivas.  
- **Conectividad** (métricas a tener en cuenta: diámetro de la red, densidad de la red, coeficiente medio de clustering, longitud media de camino)
En estas métricas no hay diferencias tan grandes como las anteriores, pero se puede destacar la diferencia en el coeficiente medio de clustering. Ésta métrica es más baja en el entorno de Arya, lo cual nos permite pensar que es más probable que Arya se encuentre con personajes que no se conocen entre sí, lo cual, sumado al resto de métricas, va a permitir que Arya se mueva con mayor facilidad por el mundo sin encontrarse con personajes que puedan reconocerla. De esta forma, de cometer un error es más probable que Arya pueda escapar de sus consecuencias directas sobre el entorno cercano.  

Sumando ambas características, se puede ver que el entorno de Sansa se caracteriza por tener un grueso de personajes de alta importancia, mientras que el entorno de Arya se caracteriza por poder moverse entre los hilos de la historia pudiendo no ser reconocida por los personajes que se encuentre. Es así como Sansa termina siendo un títere de su entorno, teniendo que meditar sin mucho éxito cada movimiento, mientras que Arya resulta un ser más libre que a lo largo de la historia aprende a jugar con los pesos de su entorno manejando cada peligro que se le presenta.  

## Análisis de los personajes individualmente

### Métricas sobre el grafo completo

Al momento de analizar los personajes individualmente hay distintas métricas a tomar en cuenta. En principio, se puede analizar el grado de cada personaje, lo cual nos indica la cantidad de interacciones que tiene el personaje con otros personajes, pero no nos indica la importancia de los personajes con los que interactúa o si estos personajes a su vez pueden estar conectados a otros de importancia y contribuir a la influencia del personaje en cuestión.   
Para esto, se pueden analizar distintas métricas de centralidad e importancia. En particular, se analizarán distintas métricas de forma gráfica directamente sobre la red, y luego se analizará más a fondo aquellos personajes que se destaquen en las métricas.  

**::Grados::**  
El grado de un nodo es la cantidad de aristas que lo conectan con otros nodos. En el caso de la red de personajes, el grado de un personaje es la cantidad de interacciones que tiene con otros personajes.
![Grafo coloreado según grados](src/images/graph_by_connections.png)
Se puede ver como destacan los siguientes personajes:
1. Tyrion Lannister
2. Jon Snow
3. Jaime Lannister
4. Cersei Lannister
5. Stannis Baratheon
6. Arya Stark
7. Catelyn Stark
8. Eddard Stark
9. Sansa Stark
10. Robb Stark

**::Grados con pesos::**  
El grado con pesos de un nodo es la suma de los pesos de las aristas que lo conectan con otros nodos. En el caso de la red de personajes, el grado con pesos de un personaje es la suma de las interacciones que tiene con otros personajes.
![Grafo coloreado según grados con pesos](src/images/degrees_by_weights.png)
Se puede ver como destacan los siguientes personajes:
1. Tyrion Lannister
2. Jon Snow
3. Cersei Lannister
4. Joffrey Baratheon
5. Edddard Stark
6. Daenerys Targaryen
7. Jaime Lannister
8. Sansa Stark
9. Bran Stark
10. Robert Baratheon

Aquí sorprende cómo es que aparece Bran, pero al analizarlo más a fondo se puede ver que es debido a que Bran tiene una gran cantidad de interacciones con los personajes de su entorno, pero no tiene interacciones con personajes de otros entornos. 

**::Betweenness centrality::**  
Es una medida de centralidad en un grafo basada en los caminos más cortos, esta medida para cada nodo es la cantidad de caminos más cortos que pasan por el mismo.  
![betweenness](src/images/betweenness_centrality.png)  
Se puede ver como destacan los siguientes personajes:
1. Jon Snow
2. Tyrion Lannister
3. Daenerys Targaryen
4. Theon Greyjoy
5. Stanis Baratheon
6. Jaime Lannister
7. Cersei Lannister
8. Arya Stark
9. Eddard Stark
10. Robert Baratheon

Estos personajes se destacan por ser personajes que se mueven mucho a lo largo de la historia, y que además tienen un rol importante en la misma. Las únicas excepciones son Theon Greyjoy y Cersei Lannister, que si bien no se mueven tanto como los demás, tienen un rol importante en la historia.  

**::Eigenvector centrality::**  
Es una medida de influencia de un nodo en una red. Los puntajes relativos se asignan a todos los nodos de la red en base al concepto de que las conexiones a nodos de alto puntaje contribuyen más al puntaje del nodo en cuestión que las conexiones iguales a nodos de bajo puntaje. Un puntaje alto de eigenvector significa que un nodo está conectado a muchos nodos que a su vez tienen puntajes altos.  
![eigenvector](src/images/eigenvector_centrality.png)
Se puede ver como destacan los siguientes personajes:
1. Tyrion Lannister
2. Cersei Lannister
3. Jaime Lannister
4. Joffrey Baratheon
5. Sansa Stark
6. Robert Baratheon
7. Eddard Stark
8. Stannis Baratheon
9. Catelyn Stark
10. Robb Stark

Estos personajes se destacan por su alto poder político o militar, en todos los casos son personajes que ocuparon el trono de hierro (Joffrey, Robert), son herederos al mismo o se proclaman rey (Stannis, Robb), tuvieron una fuerte influencia sobre un rey (Cersei, Jaime, Eddard, Catelyn), o son instrumentos de poder (Sansa). En el caso de Tyrion, tiene un alto poder político debido a ser un Lannister, pero además tiene un alto poder militar debido a su rol como estratega y tener muy poco para perder.  

### Métricas sobre un grafo selecto
A continuación se analizarán las métricas sobre un grafo selecto, en particular, los personajes con mayor presencia e importancia en la historia. Para ello se tomaron todas las métricas anteriores para hacer un filtrado de los nodos menos importantes y quedarse con los más relevantes. La idea principal es ver cómo se dan las métricas anteriores dentro de una red de sólo personajes de alta importancia.

**::Grados::**
![Grafo coloreado según grados](src/images/most_important.png)
Se puede ver como destacan los siguientes personajes:
1. Tyrion Lannister
2. Robert Baratheon
3. Cersei Lannister
4. Eddard Stark
5. Jaime Lannister
6. Joffrey Baratheon
7. Stannis Baratheon
8. Robb Stark
9. Sansa Stark
10. Tywin Lannister

**::Grados con pesos::**
![Grafo coloreado según grados con pesos](src/images/selected_degrees_by_weights.png)
Se puede ver como destacan los siguientes personajes:  
1. Tyrion Lannister
2. Cersei Lannister
3. Jon Snow
4. Joffrey Baratheon
5. Eddard Stark
6. Robert Baratheon
7. Sansa Stark
8. Robb Stark
9. Stannis Baratheon
10. Jaime Lannister

**::Betweenness centrality::**
![betweenness](src/images/selected_betweenness_centrality.png)
Se puede ver como destacan los siguientes personajes:  
1. Tyrion Lannister
2. Robert Baratheon
3. Stannis Baratheon
4. Jon Snow
5. Eddard Stark
6. Joffrey Baratheon
7. Barristan Selmy
8. Jaime Lannister
9. Daenerys Targaryen
10. Tywin Lannister

**::Eigenvector centrality::**
![eigenvector](src/images/selected_eigenvector_centrality.png)
Se puede ver como destacan los siguientes personajes:  
1. Tyrion Lannister
2. Robert Baratheon
3. Cersei Lannister
4. Jaime Lannister
5. Edddard Stark
6. Joffrey Baratheon
7. Sansa Stark
8. Stannis Baratheon
9. Robb Stark
10. Tywin Lannister

De esta forma podemos sacar las siguientes conclusiones:
- **Tyrion Lannister** es el personaje con más relevancia en la historia, en todas las métricas se encuentra en el primer puesto (con una sóla excepción para BC del grafo completo). Esto demuestra que Tyrion es un personaje con muchos lazos, y que además estos lazos son con personajes de alta relevancia. Sumado a esto, su inteligencia le da un rol de estratega capaz de cambiar el curso de la historia con sus decisiones y de recuperar el rumbo en caso de un cambio de curso inesperado y desfavorable.  
- **Jon Snow** es un personajes con no muchas conexiones de importancia, pero las que tiene son reiteradas a lo largo de la historia (se ve en el cambio de métricas de grados entre el grafo completo y el grafo selecto).
- Los hermanos **Jaime** y **Cersei** son influyentes en la historia, manteniendo un rango de importancia similar a pesar de estar en dos escenarios diferentes. Cersei se encuentra en Desembarco del Rey, mientras que Jaime se encuentra escapando del entorno de Robb Stark como prisionero de guerra protegido por Brienne de Tarth. Esto invita a pensar que no sólo son personajes influyentes, sino que sus situaciones pueden no ser tan diferentes como aparentan: Cersei en realidad es prisionera de su alta posición, sin poder ejercer realmente el poder debido a las consideraciones de su entorno por sobre las mujeres, mientras que Jaime a lo largo de la historia comienza a acomodarse en su posición y ganando libertades a medida que afrenta junto a Brienne los peligros que se le presentan.  
- **Arya Stark** es un personaje muy capaz, esto se ve debido a la gran cantidad de conexiones y avance a lo largo de la historia. Volviéndose un personaje de importancia por mérito propio y no por conexiones de alta importancia. Esto además es una ventaja, ya que tener conexiones de importancia puede resultar peligroso, de esta forma Arya puede moverse con mayor libertad.
- **Sansa Stark** de forma opuesta a Arya, aparece en mayores tops de las métricas. Esto permite ver cómo Sansa es un elemento de la política manejado por su difícil entorno, en donde cada movimiento que hace puede ser crucial para su supervivencia.
- **Catelyn** y **Robb Stark** son personajes que se mantienen en distintos tops de las métricas, pero no en todos. Esto da contexto a las conexiones necesarias para que Robb se convierta en rey en el norte, pero también da contexto a la muerte de Robb y Catelyn, ya que no son personajes que se encuentren en todos los tops de las métricas. Esto permite ver cómo la muerte de Robb y Catelyn es un hecho de alta importancia para sus casas enemigas y el por qué fue planeado con tanto cuidado para evitar _salpicarse_.
- **Stannis Baratheon** es un personaje que se encuentra en los tops de las métricas, pero no en todos. Esto permite ver cómo Stannis es un personaje que se encuentra en una posición de poder, pero que no tiene la influencia suficiente para ser un personaje de mayor importancia. Esto da contexto a por qué le es tan difícil a Stannis conseguir aliados para su causa y acercarse al trono de hierro.
- **Eddard Stark** y **Robert Baratheon** son personajes que se encuentran en los tops de las métricas, pero no en todos. Esto permite ver cómo son personajes que se encuentran en una posición de alto poder, pero efímero. Ya que ambos mueren al principio de la historia, pero sus muertes son el punto de partida de la misma.
- **Joffrey Baratheon**, **Theon Greyjoy** y **Tywin Lannister** son personajes que se encuentran en los tops de las métricas, pero no en todos. Esto se debe a que son personajes que tuvieron poder o influencia en determindos momentos de la historia. En el caso particular de Twin, se puede ver cómo su influencia surge dentro del grafo selecto, esto se debe a que su influencia se da a partir de la muerte de Eddard Stark y por sobre un grupo selecto de personajes (por sobre todo su hija Cersei). Esto permite ver cómo Tywin es un estratega bajo las sombras, muy simliar a Tyrion, pero con una influencia más enfocada sobre los personajes cercanos al trono (incluso fue mano del rey en su momento).
- **Daenerys Targaryen** es un personaje que se encuentra en algunos tops. Esto se debe a que su historia se mantiene alejada de Westeros en la gran mayoria de la historia, incluso muchos no saben su nombre. De esta forma, Daenerys es un personaje de alto poder e influencia sólo dentro de su entorno y ocasionalmente por fuera del mismo.

## Comparación con redes generadas de forma aleatoria

**Erdös-Rényi** es un modelo de red aleatoria en donde se generan aristas entre los nodos con una probabilidad p.  
**Preferential Attachment** es un modelo de red aleatoria en donde se generan aristas entre los nodos con una probabilidad proporcional al grado de los nodos.  
**Distancia del coseno** es una medida de similitud entre dos vectores en un espacio multidimensional. En el caso de las redes, se utiliza para medir la similitud entre dos anonymous walks.  

Para comparar la red de personajes con redes generadas de forma aleatoria, se generaron dos redes aleatorias, una con el modelo de Erdös-Rényi y otra con el modelo de Preferential Attachment. Luego se generaron anonymous walks sobre las redes aleatorias y se compararon con los anonymous walks sobre la red de personajes utilizando la distancia del coseno.  
A continuación se muestran dos resultados obtenidos para anonymous walks de 4 nodos (se intentó correr con más pero la pc no aguantó).  
```
Grafo cargado ✔
Simulación de un modelado de Erdös-Rényi ✔
Simulación de un modelado de Preferential Attachment (ley de potencias) ✔
Representación de anonymous walks de la red original (largo de 4 nodos) ✔
Representación de anonymous walks del modelado de Erdös-Rényi (largo de 4 nodos) ✔
Representación de anonymous walks del modelado de Preferential Attachment (largo de 4 nodos) ✔
Distancia coseno entre la red original y el modelado de Erdös-Rényi: 0.0005318079958945843
Distancia coseno entre la red original y el modelado de Preferential Attachment: 0.0006976753088120402
```
```
Grafo cargado ✔
Simulación de un modelado de Erdös-Rényi ✔
Simulación de un modelado de Preferential Attachment (ley de potencias) ✔
Representación de anonymous walks de la red original (largo de 4 nodos) ✔
Representación de anonymous walks del modelado de Erdös-Rényi (largo de 4 nodos) ✔
Representación de anonymous walks del modelado de Preferential Attachment (largo de 4 nodos) ✔
Distancia coseno entre la red original y el modelado de Erdös-Rényi: 0.0005400330220748373
Distancia coseno entre la red original y el modelado de Preferential Attachment: 0.0008448615728700037
```

En ambos casos se tratan de simulaciones con una diferencia entre 0.0005 y 0.001, lo cual indica que las redes generadas de forma aleatoria son similares a la red de personajes. Esto indica dos cosas:  
- La red de personajes dista de ser una red aleatoria, ya que la diferencia si bien es chica no es sumamente baja (como un caso de redes de aeropuertos analizada en un trabajo anterior, en donde la diferencia era de una magnitud de 10^-5).
- Las simulaciones generadas no son del todo incorrectas, ya que tampoco es una diferencia grande la obtenida, de esta forma ambas podrían usarse como aproximaciones a la red de personajes.
- Las redes generadas con Erdös-Rényi obtuvieron menores diferencias que las generadas con Preferential Attachment, esto indica que la red de personajes se asemeja más a una red en donde los nodos se conectan de forma aleatoria que a una red en donde los nodos se conectan de forma proporcional a la cantidad de conexiones que ya tienen.

### Extra sobre las redes generadas

Para ver un poco más en profundidad el comportamiento de la red de personajes, vamos a tomar el grafo de personajes selectos creado anteriormente y vamos a compararlo con las redes generadas de forma aleatoria.

```
Grafo cargado ✔
Simulación de un modelado de Erdös-Rényi ✔
Simulación de un modelado de Preferential Attachment (ley de potencias) ✔
Representación de anonymous walks de la red original (largo de 4 nodos) ✔
Representación de anonymous walks del modelado de Erdös-Rényi (largo de 4 nodos) ✔
Representación de anonymous walks del modelado de Preferential Attachment (largo de 4 nodos) ✔
Distancia coseno entre la red original y el modelado de Erdös-Rényi: 0.0021994336823688565
Distancia coseno entre la red original y el modelado de Preferential Attachment: 0.00026055661266732866
```
```
Grafo cargado ✔
Simulación de un modelado de Erdös-Rényi ✔
Simulación de un modelado de Preferential Attachment (ley de potencias) ✔
Representación de anonymous walks de la red original (largo de 4 nodos) ✔
Representación de anonymous walks del modelado de Erdös-Rényi (largo de 4 nodos) ✔
Representación de anonymous walks del modelado de Preferential Attachment (largo de 4 nodos) ✔
Distancia coseno entre la red original y el modelado de Erdös-Rényi: 0.0024188339101061107
Distancia coseno entre la red original y el modelado de Preferential Attachment: 0.0002524831705156272
```

Para la red de personajes selectos se obtuvieron mejoras para el caso de Preferential Attachment, reduciendo la distancia coseno al grafo original, en cuanto a Erdös-Rényi se obtuvieron distancias mayores, lo cual indica que esta forma de simulación es menos eficaz para la red. De esto se puede concluir que dentro de los personajes más importantes, los personajes de mayor importancia (con mayor cantidad de conexiones) son más propensos a generar nuevas conexiones a lo largo de la historia.

## Epidemias en Game of Thrones

En la saga de Game of Thrones hay varias enfermedades que afectan a los personajes, en particular, hay dos enfermedades que afectan a la población de Westeros: la viruela y la peste gris (o psoriagris). La viruela es una enfermedad que afecta a la población de Desembarco del Rey, mientras que la peste gris afecta a la población de Meereen.  
En ambos casos son enfermedades que aparecen como temáticas secundarias, resultándo sólo preocupaciones para los personajes principales de la trama. De hecho, el personaje más importante en padecer psoriagris es Shireen Baratheon, la hija de Stannis Baratheon, pero es un caso en donde la enfermedad se detuvo y no avanzó a mayores.  
Dada la ausencia de una enfermedad de alta importancia en la trama, se decidió analizar cómo sería el comportamiento de la red ante una epidemia. Para ello se setearon las siguientes variables:  

- Probabilidad de infectarse ante un contacto con un infectado: 2.5%
- Probabilidad de recuperarse: 0.5%
- Probabilidad de morir: 0.25%
- Se asume que una vez recuperado, el personaje no puede volver a infectarse
- Se asume que una vez muerto, el personaje no puede seguir infectando a otros
- Se tomó una cantidad de iteraciones máxima de 100, frenando la simulación en este punto o al no haber más infectados (lo que ocurra primero)

Para la simulación se tomaron 4 personajes ejemplo: Arya Stark, Tyrion Lannister, Daenerys Targaryen y Varys. Los primeros dos son personajes que se mueven mucho a lo largo de la historia, Tyrion encontrándose con personajes de mayor renombre, mientras que Arya va disminuyendo la importancia de sus conexiones a lo largo de la saga. Daenerys es un personaje que se encuentra en un entorno muy particular, en donde no se encuentra con personajes de Westeros, pero sí hay algunos que se mueven entre ambos continentes, pero mitiendo así la transmisión de la epidemia. Varys no se mueve mucho a lo largo de la historia, además no tiene tanto renombre como los tres personajes anteriores, pero se encuentra en contacto con personajes de alta importancia en Desembarco del Rey, lo cual lo hace un personaje de interés para la simulación.  

> **Nota:**
> La simulación se hizo sobre una red que acumula todas las interacciones de los personajes a lo largo de la historia, por lo que asume a todos los vecinos de un personaje como posibles para infectar. Lo cual no es del todo correcto dado que hay personajes con contactos en puntas muy diferentes del mapa.  
> Entonces se puede decir que la aproximación puede funcionar si se toma a la epidemia como una enfermedad que se tiene de por vida y da tiempo a que los personajes se muevan lo suficiente como para que los nuevos infectados se den en un entorno posible.  
> Por esto mismo se eligieron personajes que se mueven lo suficiente a lo largo de la historia, y además una tasa de recuperación y muerte baja, para que la enfermedad no se detenga con facilidad.

A continuación se muestran los resultados obtenidos para la simulación de la epidemia:  

**Arya Stark**  
![Epidemia caso Arya Stark](src/images/epidemy-arya.png)
Métricas al momento de la captura:  
- Infectados: 53.52%
- Recuperados: 23.12%
- Muertos: 11.93%
- No infectados: 11.43%

**Tyrion Lannister**  
![Epidemia caso Tyrion Lannister](src/images/epidemy-tyrion.png)
Métricas al momento de la captura:
- Infectados: 48.37%
- Recuperados: 26.63%
- Muertos: 12.44%
- No infectados: 12.56%

**Daenerys Targaryen**  
![Epidemia caso Daenerys Targaryen](src/images/epidemy-daenerys.png)
Métricas al momento de la captura:
- Infectados: 48.49%
- Recuperados: 24.62%
- Muertos: 14.7%
- No infectados: 12.19%

**Varys**  
![Epidemia caso Varys](src/images/epidemy-varys.png)
Métricas al momento de la captura:
- Infectados: 49.37%
- Recuperados: 25.25%
- Muertos: 13.07%
- No infectados: 12.31%

De estos resultados se puede ver cómo la enfermedad se propaga con facilidad, sin haber mayores diferencias entre los personajes. Esto se debe a que la enfermedad se propaga con facilidad, y que además la red tiene un diámetro bajo. De esta forma, la enfermedad puede llegar con facilidad a un personaje con alta cantidad de conexiones y desde ahí propagarse con facilidad.  

Para sacar algo de mayor provecho de la simulación, se decidió analizar un caso en donde la enfermedad se detiene con facilidad (ya sea muriendo o recuperándose) y tomar personajes más variados. De esta forma se eligieron los personajes:

- Tyrion Lannister
- Varys
- Daenerys Targaryen
- Obara Sand

Y se setearon las siguientes variables:

- Probabilidad de infectarse ante un contacto con un infectado: 2.5%
- Probabilidad de recuperarse: 5%
- Probabilidad de morir: 2.5%
- Se asume que una vez recuperado, el personaje no puede volver a infectarse
- Se asume que una vez muerto, el personaje no puede seguir infectando a otros
- Se tomó una cantidad de iteraciones máxima de 20, frenando la simulación en este punto o al no haber más infectados (lo que ocurra primero)

A continuación se muestran los resultados obtenidos:  

**Tyrion Lannister**
![Epidemia caso Tyrion Lannister](src/images/epidemy2-tyrion.png)
Métricas al momento de la captura:  
- Infectados: 21.36%
- Recuperados: 17.34%
- Muertos: 7.79%
- No infectados: 53.51%

Además, si se saca a los no infectados se obtiene:
- Infectados: 45.95%
- Recuperados: 37.3%
- Muertos: 16.75%

**Varys**
![Epidemia caso Varys](src/images/epidemy2-varys.png)
Métricas al momento de la captura:  
- Infectados: 20.48%
- Recuperados: 12.31%
- Muertos: 6.03%
- No infectados: 61.18%

Además, si se saca a los no infectados se obtiene:
- Infectados: 52.75%
- Recuperados: 31.72%
- Muertos: 15.53%

**Daenerys Targaryen**
![Epidemia caso Daenerys Targaryen](src/images/epidemy2-daenerys.png)
Métricas al momento de la captura:
- Infectados: 18.22%
- Recuperados: 12.56%
- Muertos: 4.52%
- No infectados: 64.7%

Además, si se saca a los no infectados se obtiene:
- Infectados: 51.6%
- Recuperados: 35.59%
- Muertos: 12.81%

**Obara Sand**
![Epidemia caso Obara Sand](src/images/epidemy2-obara.png)
Métricas al momento de la captura:
- Infectados: 17.71%
- Recuperados: 3.89%
- Muertos: 1.88%
- No infectados: 76.52%

Además, si se saca a los no infectados se obtiene:
- Infectados: 75.4%
- Recuperados: 16.58%
- Muertos: 8.02%

De estos resultados se puede ver cómo el desarrollo de la epidemia varía según el personaje inicial, siendo determinante para la velocidad de la extensión de la misma. Además, notar que en caso de alcanzar en algún punto a un personaje de importancia, la velocidad de propagación de la enfermedad se dispara, por lo que no sólo es importante el personaje inicial, sino también el entorno en el que se encuentra. Para validar esto último se puede ver que se obtuvieron resultados similares para Daenerys y Varys, siendo Daenerys un personaje con mayor grado que Varys, pero estando algo más apartada del nucleo de Desembarco del Rey (ciudad en donde se encuentra gran parte de los personajes con mayor cantidad de conexiones).  
Los cambios en el avance de la epidemia según el personaje seleccionado son dos:  
- **Velocidad de infección**: Se puede ver cómo la cantidad de no infectados varía en los casos Tyrion, Daenerys-Varys, Obara. Esto se debe a la cantidad de conexiones que la enfermedad puede encontrar, es decir, las oportunidades de la misma para expandirse.
- **Desarrollo de la enfermedad por sobre cada personaje**: Se puede ver cómo la cantidad de recuperados y muertos varía en los distintos casos. Esto se debe al tiempo que tiene la enfermedad para evolucionar en cada personaje y finalmente el mismo recuperarse o morir. En los casos en donde la enfermedad es más lenta, se puede ver que la cantidad de recuperados o muertos en función de los infectados es menor debido a que los contagios son más recientes.

Estas situaciones permiten que se den escenarios completamente diferentes en la historia. En uno en donde la enfermedad se propaga con facilidad será crucial encontrar una forma de detenerla cuanto antes, pero se podrá conocer con facilidad el caracter de la misma (tiempo de desarrollo hasta la recuperación/muerte y probabilidad de recuperación/muerte). Mientras que en el otro caso, la enfermedad se propaga con mayor dificultad, pero es necesario esperar mayor tiempo para conocer el caracter de la misma.  
Esto incluiría variantes a la historia, en donde una enfermedad con dificultades para expandirse sobre la red se ve favorable, pero recaería en los personajes decidir si arriesgar o no tiempo para conocer el caracter de cómo evolucionará, por el otro lado, una enfermedad que se propaga con facilidad sobre la red requerirá de una rápida respuesta para evitar que se propague con facilidad, pero se podrá conocer con facilidad el caracter de la misma (con el costo humano que esto conlleva).  

## Predicción de interacciones

A continuación se utilizará un plugin de Gephi para predecir interacciones entre los personajes. La idea es ver cómo podría comportarse la red en un futuro mediante la predicción de aristas en la red. Para esto, se utilizó la red de personajes selectos para obtener sólo aristas de relevancia.  
Respecto a los algoritmos a utilizar, se usaron tanto _Preferential Attachment_ como _Common Neighbours_ para ver cómo se comportan los algoritmos en la red. La red tiene 537 aristas, y se crearán 50 aristas más (aproximadamente el 10% de las aristas actuales) para ver cómo se comportan los algoritmos.  

**Common Neighbours**  
Se crearon las siguientes aristas:
- Arya-Stark - Stannis-Baratheon  
- Bran-Stark - Stannis-Baratheon  
- Bran-Stark - Jaime-Lannister  
- Brienne-of-Tarth - Eddard-Stark  
- Brienne-of-Tarth - Petyr-Baelish  
- Arya-Stark - Brienne-of-Tarth  
- Arya-Stark - Renly-Baratheon  
- Rodrik-Cassel - Stannis-Baratheon  
- Bran-Stark - Tywin-Lannister  
- Jon-Snow - Petyr-Baelish  
- Bran-Stark - Brienne-of-Tarth  
- Catelyn-Stark - Pycelle  
- Pycelle - Robb-Stark  
- Jon-Arryn - Sansa-Stark  
- Robert-Baratheon - Theon-Greyjoy  
- Gregor-Clegane - Renly-Baratheon  
- Petyr-Baelish - Theon-Greyjoy  
- Cersei-Lannister - Theon-Greyjoy  
- Joffrey-Baratheon - Theon-Greyjoy  
- Sansa-Stark - Theon-Greyjoy  
- Brienne-of-Tarth - Theon-Greyjoy  
- Renly-Baratheon - Theon-Greyjoy  
- Jon-Snow - Renly-Baratheon  
- Brienne-of-Tarth - Jon-Snow  
- Jon-Snow - Tywin-Lannister  

**Preferential Attachment**  
Se crearon las siguientes aristas:
- Arya-Stark - Stannis-Baratheon  
- Robert-Baratheon - Theon-Greyjoy  
- Jon-Snow - Tywin-Lannister  
- Bran-Stark - Jaime-Lannister  
- Bran-Stark - Stannis-Baratheon  
- Bran-Stark - Tywin-Lannister  
- Cersei-Lannister - Theon-Greyjoy  
- Joffrey-Baratheon - Theon-Greyjoy  
- Sansa-Stark - Theon-Greyjoy  
- Jon-Snow - Petyr-Baelish  
- Barristan-Selmy - Stannis-Baratheon  
- Petyr-Baelish - Theon-Greyjoy  
- Barristan-Selmy - Tywin-Lannister  
- Barristan-Selmy - Robb-Stark  
- Brienne-of-Tarth - Eddard-Stark  
- Sandor-Clegane - Stannis-Baratheon  
- Arya-Stark - Renly-Baratheon  
- Arya-Stark - Barristan-Selmy  
- Jon-Snow - Renly-Baratheon  
- Barristan-Selmy - Jon-Snow  
- Barristan-Selmy - Catelyn-Stark  
- Barristan-Selmy - Bran-Stark  
- Barristan-Selmy - Theon-Greyjoy  
- Renly-Baratheon - Theon-Greyjoy  
- Sandor-Clegane - Tywin-Lannister  

Algunas cosas a notar:
- No se predijeron nuevos enlaces para Tyrion Lannister, lo cual podría indicar que el personaje ya tiene una cantidad de conexiones suficiente como para no necesitar más.
- Se predijeron nuevas conexiones para personajes con una cantidad media de conexiones, lo cual indica que algunos personajes tienen lugar a seguir creciendo.
- Se predijeron conexiones para personajes ya muertos, lo cual indica posibles caminos alternos que podría haber seguido la historia.

Se puede ver como entre ambos algoritmos hay repeticiones, vamos a tomar esas repeticiones como medida de alta probabilidad que tal interacción ocurra en el futuro en la saga, las cuales son:
- Arya-Stark - Stannis-Baratheon  
- Bran-Stark - Stannis-Baratheon  
- Bran-Stark - Jaime-Lannister  
- Brienne-of-Tarth - Eddard-Stark  
- Arya-Stark - Renly-Baratheon  
- Bran-Stark - Tywin-Lannister  
- Jon-Snow - Petyr-Baelish  
- Robert-Baratheon - Theon-Greyjoy  
- Petyr-Baelish - Theon-Greyjoy  
- Cersei-Lannister - Theon-Greyjoy  
- Joffrey-Baratheon - Theon-Greyjoy  
- Sansa-Stark - Theon-Greyjoy  
- Renly-Baratheon - Theon-Greyjoy  
- Jon-Snow - Renly-Baratheon  
- Jon-Snow - Tywin-Lannister  

De estas conexiones vamos a eliminar las que contengan personajes muertos, ya que no tienen sentido en el contexto de la saga. Personajes muertos: Eddeard Stark, Robert Baratheon, Renly Baratheon, Tywin Lannister, Joffrey Baratheon. Stannis Baratheon no se encuentra en la lista de personajes muertos dado que su muerte no fue confirmada, por lo que podría hacer una reaparición.  
- Arya-Stark - Stannis-Baratheon  
- Bran-Stark - Stannis-Baratheon  
- Bran-Stark - Jaime-Lannister  
- Jon-Snow - Petyr-Baelish  
- Petyr-Baelish - Theon-Greyjoy  
- Cersei-Lannister - Theon-Greyjoy  
- Sansa-Stark - Theon-Greyjoy  

Respecto al grupo de aristas **[Petyr-Baelish - Theon-Greyjoy | Cersei-Lannister - Theon-Greyjoy | Sansa-Stark - Theon-Greyjoy]**: El último status de Theon en la saga es como prisionero de Ramsay Bolton, por lo que podría ser utilizado para re-capturar a Sansa Stark. Con tal fin podría haber una alianza entre Petyr Baelish y Cersei Lannister para recuperar a Sansa, ya que ambos tienen intereses en la misma y entonces interactuar con Theon para tal fin.  

El resto de aristas no tienen un contexto claro para que ocurran dado que en muchos casos son personajes que se encuentran lejanos, pero podrían ser interesantes de ver cómo se desarrollan en la historia. De entre ellos sería curiosa una interacción entre Bran Stark y Jaime Lannister, ya que ambos tienen una historia en común, pero no se encuentran desde el primer libro.  


<!-- # ***Beep boop, estoy trabajando en esto*** 👇🏻 -->

<!-- ## analizar la red según los libros (ver la oportunidad de comparar la evolución entre distintos libros) -->

<!-- ## análisis siguendo x personajes -->

<!-- ## análisis por dentro de un cluster -->

