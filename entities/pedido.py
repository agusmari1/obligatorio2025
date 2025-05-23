from cliente import Cliente
from maquina import Maquina
from requerimiento import Requerimiento
from datetime import datetime

class Pedido:
    def __init__(self,cliente,maquina):
        self._cliente=cliente
        self._maquina=maquina
        self._fecha_recepcion=datetime.now()
        self._fecha_entrega=None #despues decidimos si el pedido se puede entregar o no
    
    @property
    def estado(self):
        return self.estado
    @property
    def fecha_recepcion(self):
        return self._fecha_recepcion
    @property
    def fecha_entrega(self):
        return self._fecha_entrega
    @property
    def precio_final(self):
        return self._precio_final
   
        if self._puede_entregarse():


    def _puede_entregarse(self):
        for req in self._maquina.requerimientos: #recorre los requerimientos de la maquina(cada requerimiento es:una pieza y cuentas necesita)
             if req.pieza.cantidad_disponible <req.cantidad: # cuantas hay en stock<cuantas necesita la maquina
                return False
        return True

        
            
        



