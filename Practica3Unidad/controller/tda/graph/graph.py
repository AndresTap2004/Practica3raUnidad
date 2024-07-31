from controller.exception.arrayPositionException import ArrayPositionException
import json
import os 

class Graph():
    def __init__(self):
        self.__grafo = None

        @property
        def num_vertex(self):
            raise NotImplementedError("Por favor implemente este método")

        @property
        def num_edges(self):
            raise NotImplementedError("Por favor implemente este método")
            
        def exist_edges(self, v1, v2):
            raise NotImplementedError("Por favor implemente este método")
        
        def weight_edges(self, v1, v2):
            raise NotImplementedError("Por favor implemente este método")
        
        def insert_edges(self, v1, v2):
            raise NotImplementedError("Por favor implemente este método")
        
        def insert_edges_weight(self, v1, v2, weight):
            raise NotImplementedError("Por favor implemente este método")
        
        def adjacent(self, v1):
            raise NotImplementedError("Por favor implemente este método")

    def __str__(self) -> str:
        out = ""
        for i in range(0, self.num_vertex):
            out += "V" + str(i + 1) + "\n"
            adjs = self.adjacent(i)
            if not adjs.isEmpty:
                for j in range (0, adjs._length):
                    adj = adjs.get(j)
                    out += "ady " + f"V" + str(adj._destination + 1) + " weight " + str(adj._weight) + "\n"
        return out 
        
    def paint_graph(self):
        url = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))+"/static/d3/grafo.js"
        
        js = 'var nodes = new vis.DataSet(['
        for i in range(0, self.num_vertex):
            js += '{id: ' + str(i + 1) + ',label:"' + str(i+1)+'"},' + '\n'
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
        
        