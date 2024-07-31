from typing import TypeVar, Generic, Type
from controller.tda.linked.linkedList import LinkedList
import os.path
import json
import os 

T = TypeVar("T")
class DaoAdapter(Generic[T]):
    atype: T
    def __init__(self, atype: T):
        self.atype = atype
        self.lista = LinkedList()
        self.file = atype.__name__.lower()+".json"
        self.URL = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))+"/data/"

    def _list(self) -> T:
        try:
            if os.path.isfile(self.URL+self.file):
                f = open(self.URL+self.file, "r")
                datos = json.load(f)
                self.lista.clear
                for data in datos:
                    a = self.atype.deserializar(data)
                    self.lista.add(a, self.lista._length)
                f.close()
            return self.lista
        except Exception as e:
            print(f"Error en list es: {e}")
    
    def _save(self, data: T) -> T:
        try:
            self._list()
            self.lista.add(data, self.lista._length)
            a = open(self.URL+self.file, "w")
            a.write(self.__tranform__())
            a.close()
        except Exception as e:  
            print(f"Error en save es: {e}")
   
    def _merge(self, data: T, pos) -> T:
        try:
            self._list()
            self.lista.edit(data, pos)
            a = open(self.URL+self.file, "w")
            a.write(self.__tranform__())
            a.close()
        except Exception as e:
            print(f"Error en merge es: {e}")

    def to_dict(self):
        aux = []
        self._list()
        for i in range(0, self.lista._length):
            # aux.append(json.dumps(self.lista.get(i).serializable))
            aux.append(self.lista.get(i).serializable)
        return aux
    
    def to_dic_lista(self, lista):
        aux = []
        arreglo = lista.toArray
        for i in range(0, lista._length):
            aux.append(arreglo[i].serializable)
        return aux

    def __tranform__(self):
        try:
            aux = "["
            for i in range(0, self.lista._length):
                if i < self.lista._length - 1:
                    aux += str(json.dumps(self.lista.get(i).serializable))+","
                else:
                    aux += str(json.dumps(self.lista.get(i).serializable))
            aux += "]"
            return aux
        except Exception as e:
                print(f"Error en transform es: {e}")
                
