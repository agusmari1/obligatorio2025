from datetime import datetime
from pieza import Pieza

class Reposicion:
    def __init__(self,pieza,cantidad_lotes):
        self._pieza=pieza
        self._cantidad_lotes=cantidad_lotes
        self.fecha=self.obtener_fecha_actual()
        self._pieza.reponer(cantidad_lotes)

    @property
    def pieza(self):
        return self._pieza
    
    @property
    def cantidad_lotes(self):
        return self._cantidad_lotes
    
    @property
    def fecha(self):
        return self._fecha

    @property 
    def costo_total(self):
        return self._pieza.costo_adquisicion * self.cantidad_lotes * self.pieza.unidades_en_lote
    
    def obtener_fecha_actual(self): #no ponemos property porque no es una propiedad permanente del objeto y no guarda ningun valor.
        return datetime.now()
    
      