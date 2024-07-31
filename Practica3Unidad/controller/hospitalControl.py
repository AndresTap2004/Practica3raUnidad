from typing import Type
from controller.dao.daoAdapter import DaoAdapter
from model.hospital import Hospital 

class HospitalControl(DaoAdapter):
    def __init__(self):
        super().__init__(Hospital)
        self.__hospital = None

    @property
    def _hospital(self):
        if self.__hospital == None:
            self.__hospital = Hospital()
        return self.__hospital

    @_hospital.setter
    def _hospital(self, value):
        self.__hospital = value

    @property
    def _lista(self):
        return self._list()
    
    def merge(self, pos):
        self._merge(self._hospital, pos)
    
    @property
    def save(self):
        try:
            self._hospital._id = self._lista._length + 1
            self._save(self._hospital)
            return True
        except Exception as e:
            print(f"Error en save es: {e}")
            return False