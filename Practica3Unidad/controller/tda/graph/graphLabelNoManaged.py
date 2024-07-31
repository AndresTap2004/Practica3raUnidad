from controller.tda.graph.graohLabelManaged import GraphLabelManaged
from controller.exception.arrayPositionException import ArrayPositionException
from controller.hospitalControl import HospitalControl
from math import nan
import os
import json
import heapq
from controller.tda.linked.linkedList import LinkedList

class GraphLabelNoManaged(GraphLabelManaged):
    def __init__(self, num_vert):
        super().__init__(num_vert)
        self.__grafo = None
        self.graph = {}

    def inserta_arista_E(self, label1, label2):
        self.insertar_arista_peso_E(label1, label2, nan)

    def insertar_arista_peso_E(self, label1, label2, weight):
        v1 = self.getVertex(label1)
        v2 = self.getVertex(label2)
        if v1 == -1:
            v1 = self.num_vertex
            self.label_vertex(v1, label1)
        if v2 == -1:
            v2 = self.num_vertex
            self.label_vertex(v2, label2)
        self.insert_edges_weight(v1, v2, weight)
        self.insert_edges_weight(v2, v1, weight)

        if v1 not in self.graph:
            self.graph[v1] = LinkedList()
        if v2 not in self.graph:
            self.graph[v2] = LinkedList()
        self.graph[v1].add((v2, weight))
        self.graph[v2].add((v1, weight))


    #* Algoritmo Djistra
    def dijkstra(self, start):
        distances = {node: float('inf') for node in self.graph}
        distances[start] = 0
        min_heap = [(0, start)] 
        visited = set()
        parent = {}

        while min_heap:
            current_dist, current_node = heapq.heappop(min_heap) 

            if current_node in visited:
                continue

            visited.add(current_node)

            neighbors = self.graph.get(current_node, LinkedList()).toArray
            for neighbor, weight in neighbors:
                if neighbor in visited:
                    continue

                new_distance = current_dist + weight
                if new_distance < distances.get(neighbor, float('inf')):
                    distances[neighbor] = new_distance
                    parent[neighbor] = current_node
                    heapq.heappush(min_heap, (new_distance, neighbor))  

        return parent


    def camino_corto_djistra(self, start, end):
        parent = self.dijkstra(start)
        
        path = LinkedList()
        step = end
        while step is not None:
            path.add(step)
            step = parent.get(step)
        
        tamanio = path._length
        path_array = path.toArray
        new_path = LinkedList()
        for i in range(tamanio-1, -1, -1):
            new_path.add(path_array[i])
        return new_path.toArray


    #* Algoritmo Floyd
    def floyd_warshall(self):
        num_vertices = len(self.graph)
        
        dist = [[float('inf')] * num_vertices for _ in range(num_vertices)]
        next_node = [[None] * num_vertices for _ in range(num_vertices)]
        
        for u in self.graph:
            dist[u][u] = 0
            neighbors = self.graph[u].toArray
            for neighbor_tuple in neighbors:
                v, weight = neighbor_tuple
                dist[u][v] = weight
                next_node[u][v] = v
        
        for k in range(num_vertices):
            for i in range(num_vertices):
                for j in range(num_vertices):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
                        next_node[i][j] = next_node[i][k]
        
        return next_node


    def camino_corto_floyd(self, start, end, next_node):
        path = LinkedList()
        if next_node[start][end] is None:
            return path
        
        while start != end:
            path.add(start)
            start = next_node[start][end]
            if start is None:
                return LinkedList()
        path.add(end)
        tamanio = path._length
        path_array = path.toArray
        invertir = path_array[::-1]
        new_path = LinkedList()
        for i in range(tamanio):
            new_path.add(path_array[i])
        return new_path.toArray

    def paint_graph_etiquetado(self):
        hospital = HospitalControl()
        lista = hospital._lista
        print(lista)
        url = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))+"/static/d3/grafo.js"
        
        js = 'var nodes = new vis.DataSet(['
        for i in range(0, self.num_vertex):
            hospital = lista.get(i)
            js += '{id: ' + str(i + 1) + ',label:"' + str(hospital)+'"},' + '\n'
        js += ']);'
        js += "\n"

        js += 'var edges = new vis.DataSet(['
        for i in range(0, self.num_vertex):
            ini = (i + 1)
            adjs = self.adjacent(i)
            if not adjs.isEmpty:
                for j in range (0, adjs._length):
                    adj = adjs.get(j)
                    des = str(adj._destination + 1)
                    js += '{from:' + str(i + 1) + ',to:' + str(des) + ', label:"' + str(adj._weight) + '"},' + "\n"       

        js += ']);'
        js += "\n"
        js += "var container = document.getElementById('mynetwork'); var data = {nodes: nodes, edges: edges}; var options = {}; var network = new vis.Network(container, data, options);"
        a = open(url, 'w')
        a.write(js)
        a.close()
