from pieza import Pieza

class Requerimiento:
    def __init__(self,pieza,cantidad):
        self._pieza=pieza
        self._cantidad=cantidad

    @property
    def pieza(self):
        return self._pieza
    
    @property
    def cantidad(self):
        return self._cantidad
   