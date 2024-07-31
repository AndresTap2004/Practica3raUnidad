from controller.tda.graph.graphManaged import GraphManaged
from controller.exception.arrayPositionException import ArrayPositionException
from math import nan

class GraphLabelManaged(GraphManaged):
    def __init__(self, num_vert):
        super().__init__(num_vert)
        self.__label = [] 
        self.__labelvertex = {}
        for i in range(0, self.num_vertex):
            self.__label.append(None)
            
    def getVertex(self, label):
        try:
            return self.__labelvertex[str(label)]    
        except Exception as e:
            return -1 
        
    def label_vertex(self, v, label):
        print("Label_vertex")
        print(f"{v} {label}")
        self.__label[v] = label
        self.__labelvertex[str(label)] = v
        print(self.__labelvertex)
        
    def get_label(self, v):
        return self.__label[v] 
    
    def exist_edge_E(self, label1, label2):
        v1 = self.getVertex(label1)
        v2 = self.getVertex(label2)
        if v1 != -1 and v2 != -1:
            return self.exist_edges(v1, v2)
        else:
            return False
        
    def insertar_arista_peso_E(self, label1, label2, weight):
        v1 = self.getVertex(label1)
        v2 = self.getVertex(label2)
        if v1 != -1 and v2 != -1:
            return self.insert_edges_weight(v1, v2, weight)
        else:
            raise ArrayPositionException("Vertice no encontrado")

    def inserta_arista_E(self, label1, label2):
        self.insertar_arista_peso_E(label1, label2, nan) 

    def weight_edges_E(self, label1, label2):
        v1 = self.getVertex(label1)
        v2 = self.getVertex(label2)
        if v1 != -1 and v2 != -1:
            return self.weight_edges(v1, v2)
        else:
            raise ArrayPositionException("Vertice no encontrado")

    def adjacent_E(self, label1):
        v1 = self.getVertex(label1)
        if v1 != -1:
            return self.adjacent(v1)
        else:
            raise ArrayPositionException("Vertice no encontrado")
