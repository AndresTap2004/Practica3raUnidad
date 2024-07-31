class Busqueda_Binaria:
    
    def busqueda_binaria_atribute(self, array, attribute, value):
        valor_encontrado = []
        left = 0
        rigth = len(array) - 1
        
        while left <= rigth:
            middle = (left + rigth) // 2
            
            if getattr(array[middle], attribute) == value:
                valor_encontrado.append(array[middle])
                return valor_encontrado
            elif getattr(array[middle], attribute) < value:
                left = middle + 1
            else:
                rigth = middle - 1
        
        return -1
    
    def busqueda_binaria_number(self, array, value):
        valor_encontrado = []
        left = 0
        right = len(array) - 1
        
        while left <= right:
            middle = (left + right) // 2
            if array[middle] == value:
                valor_encontrado.append(array[middle])
                return valor_encontrado
            elif array[middle] < value:
                left = middle + 1
            else:
                right = middle - 1
        return -1