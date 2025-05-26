from cliente import Cliente,ClienteParticular, Empresa
from maquina import Maquina
from requerimientos import Requerimiento
from datetime import datetime

class Pedido:
    def __init__(self,cliente,maquina):
        self._cliente=cliente
        self._maquina=maquina
        self._fecha_recepcion=datetime.now()
        self._fecha_entrega=None #despues decidimos si el pedido se puede entregar o no
    
        self._precio_final=self.calcular_precio()

        if self._puede_entregarse():
            self._estado="entregado"
            self._fecha_entrega=self._fecha_recepcion
            self.actualizar_stock()
        else:
            self._estado="pendiente"
        
    def calcular_precio(self):

        if self._cliente.tipo_cliente=="cliente particular":
            precio=self._maquina.costo_produccion *1.5
        else:
            precio=self._maquina.costo_produccion * 1.5
            precio = precio * 0.8

        return precio



    @property
    def estado(self):
        return self._estado
    @property
    def fecha_recepcion(self):
        return self._fecha_recepcion
    @property
    def fecha_entrega(self):
        return self._fecha_entrega
    @property
    def precio_final(self):
        return self._precio_final
   
    


    def _puede_entregarse(self):
        for req in self._maquina.requerimientos: #recorre los requerimientos de la maquina(cada requerimiento es:una pieza y cuentas necesita)
               if req.pieza.cantidad_disponible <req.cantidad: # cuantas hay en stock<cuantas necesita la maquina
                   return False
        return True
    
    def mostrar_datos(self):
        print("Cliente:", self._cliente.nombre)
        print("Tipo:", self._cliente.tipo_cliente())
        print("Máquina:", self._maquina.descripcion)
        print("Estado:", self._estado)
        print("Fecha recepción:", self._fecha_recepcion)
        print("Fecha entrega:", self._fecha_entrega)
        print("Precio final: $", self._precio_final)
