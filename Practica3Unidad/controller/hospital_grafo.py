from controller.hospitalControl import HospitalControl
from controller.tda.graph.graphLabelNoManaged import GraphLabelNoManaged
import json
import os 
import time

class HospitalGrafo:
    def __init__(self):
        self._grafo = None
        self._nado = HospitalControl()
        
    def create_graph(self):
        # Ruta del archivo JSON
        ruta_actual = os.path.dirname(os.path.dirname(__file__))+"/data"
        json_file_path = os.path.join(ruta_actual, 'grafo.json')
        
        # Lee el archivo JSON
        with open(json_file_path, 'r') as f:
            data = json.load(f)
        
        # Inicializa el grafo
        vertices = len(data['hospital'])
        self._grafo = GraphLabelNoManaged(vertices)
        
        # Etiqueta los vértices
        for item in data['hospital']:
            vertice = item['vertice']
            self._grafo.label_vertex(vertice, str(vertice))
        
        # Añade las aristas con peso
        for item in data['hospital']:
            vertice = item['vertice']
            destinos = item['destino']
            pesos = item['peso']
            
            for destino, peso in zip(destinos, pesos):
                self._grafo.insertar_arista_peso_E(int(vertice), int(destino), float(peso))
        
        try:
            self._grafo.paint_graph_etiquetado()
        except Exception as e:
            print("Error: ", e)
            
    def buscar_camino_corto_djistra(self, start, end):
        hc = HospitalControl()
        ruta_actual = os.path.dirname(os.path.dirname(__file__))+"/data"
        json_file = os.path.join(ruta_actual, 'grafo.json')

        # Cargar el JSON
        with open(json_file, 'r') as f:
            data = json.load(f)["hospital"]
        
        # Crear el grafo
        num_vertices = len(data)
        grafo_no_dirigido = GraphLabelNoManaged(num_vertices)

        lista_hospitales = hc._list()
        
        for i in range(num_vertices):
            grafo_no_dirigido.label_vertex(i, i)
        
        for entry in data:
            vertice = entry["vertice"]
            destinos = entry["destino"]
            pesos = entry["peso"]
            
            for i in range(len(destinos)):
                destino = destinos[i]
                peso = pesos[i]
                grafo_no_dirigido.insertar_arista_peso_E(vertice, destino, float(peso))

        vertice_inicio = start - 1
        vertice_fin = end - 1

        inicio = time.time()
        shortest_path = grafo_no_dirigido.camino_corto_djistra(vertice_inicio, vertice_fin)
        fin = time.time()
        tiempo_djistra = fin - inicio

        if shortest_path is None:
            print(f"No se encontró un camino desde el vértice {vertice_inicio} al vértice {vertice_fin}.")
        else:
            camino_corto = ""
            for vertex in shortest_path:
                camino = lista_hospitales.get(int(vertex))
                camino_corto += str(camino) + " -> "
            print(f"El camino más corto desde '{vertice_inicio}' a '{vertice_fin}' es: {camino_corto[:-4]}")  
            return camino_corto, tiempo_djistra
   
    def buscar_camino_corto_floyd(self, start, end):
        hc = HospitalControl()
        ruta_actual = os.path.dirname(os.path.dirname(__file__))+"/data"
        json_file = os.path.join(ruta_actual, 'grafo.json')

        # Cargar el JSON
        with open(json_file, 'r') as f:
            data = json.load(f)["hospital"]
        
        # Crear el grafo
        num_vertices = len(data)
        grafo_no_dirigido = GraphLabelNoManaged(num_vertices)

        lista_hospitales = hc._list()
        
        for i in range(num_vertices):
            grafo_no_dirigido.label_vertex(i, i)
        
        for entry in data:
            vertice = entry["vertice"]
            destinos = entry["destino"]
            pesos = entry["peso"]
            
            for i in range(len(destinos)):
                destino = destinos[i]
                peso = pesos[i]
                grafo_no_dirigido.insertar_arista_peso_E(vertice, destino, float(peso))

        inicio = time.time()
        next_node = grafo_no_dirigido.floyd_warshall()

        vertice_inicio = start - 1
        vertice_fin = end - 1

        shortest_path = grafo_no_dirigido.camino_corto_floyd(vertice_inicio, vertice_fin, next_node)
        fin = time.time()
        tiempo_floyd = fin - inicio

        if not shortest_path:
            print(f"No se encontró un camino desde el vértice {vertice_inicio} al vértice {vertice_fin}.")
        else:
            camino_corto = ""
            for vertex in shortest_path:
                camino = lista_hospitales.get(int(vertex))
                camino_corto += str(camino) + " -> "
            print(f"El camino más corto desde '{vertice_inicio}' a '{vertice_fin}' es: {camino_corto[:-4]}") 
            return camino_corto, tiempo_floyd