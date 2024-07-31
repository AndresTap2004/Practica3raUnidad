
class Hospital:
    
    def __init__(self): 
        self.__id = 0
        self.__nombre = ""
        self.__direccion = "s/n"
        self.__horario = "s/n"
        self.__lng = 0.0
        self.__lat = 0.0

    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _nombre(self):
        return self.__nombre

    @_nombre.setter
    def _nombre(self, value):
        self.__nombre = value

    @property
    def _direccion(self):
        return self.__direccion

    @_direccion.setter
    def _direccion(self, value):
        self.__direccion = value

    @property
    def _horario(self):
        return self.__horario

    @_horario.setter
    def _horario(self, value):
        self.__horario = value

    @property
    def _lng(self):
        return self.__lng

    @_lng.setter
    def _lng(self, value):
        self.__lng = value

    @property
    def _lat(self):
        return self.__lat

    @_lat.setter
    def _lat(self, value):
        self.__lat = value

    def __str__(self) -> str:
        # return f"{str(self._id)} {self._nombre}"
        return f"{self._nombre}"
    
    @property
    def serializable(self):
        return {
            'id': self._id,
            'nombre': self._nombre,
            'direccion': self._direccion,
            'horario': self._horario,
            'lng': self._lng,
            'lat': self._lat
        }

    def deserializar(data):
        hospital = Hospital()
        hospital._id = data['id']
        hospital._nombre = data['nombre']
        hospital._direccion = data['direccion']
        hospital._horario = data['horario']
        hospital._lng = data['lng']
        hospital._lat = data['lat']
        return hospital