from cliente import Cliente,ClienteParticular,Empresa
from maquina import Maquina
from pedido import Pedido
from reposicion import Reposicion
from requerimientos import Requerimiento
from datetime import datetime
from pieza import Pieza

class Sistema:
    def __init__(self):
        self._clientes=[]
        self._maquinas=[]
        self._pedidos_pendientes=[]
        self._pedidos_entregados=[]
        self._piezas=[]
        self._reposiciones=[]

    def registro_clientes(self,cliente):
        self._clientes.append(cliente)
    
    def registro_pedido(self,cliente,maquina):
        pedido=Pedido(cliente,maquina)
        if pedido.estado=="pendiente":
            self._pedidos_pendientes.append(pedido)
        else:
            self._pedidos_entregados.append(pedido)
    
    def registro_pieza (self, descripcion, costo_adquisicion, unidades_en_lote, cantidad_disponible = 0):
        pieza = Pieza(descripcion,costo_adquisicion,unidades_en_lote,cantidad_disponible)
        self._piezas.append(pieza)
    
    def registro_maquina(self, descripcion,requerimientos):
        self._maquinas.append(descripcion,requerimientos)

    def registro_reposicion(self,pieza, cantidad_lotes):
        reposicion = Reposicion(pieza, cantidad_lotes)
        self._reposiciones.append(reposicion)
        self.actualizar_pedidos_pendientes()

    def actualizar_pedidos_pendientes(self):
        for pedido in self._pedidos_pendientes:
            if pedido._puede_entregarse():
                pedido._estado="entregado"
                pedido._fecha_entrega=datetime.now()
                pedido.actualizar_stock()
                self._pedidos_entregados.append(pedido)
                self._pedidos_pendientes.remove(pedido)

    def mostrar_pedidos_entregados(self):
        print("Pedidos entregados")
        if len(self._pedidos_entregados)==0:
            print("No hay pedidos entregados")
        else:
            for pedido in self._pedidos_entregados:
                pedido.mostrar_datos()
                print("----------")

    def mostrar_pedidos_pendientes(self):
        print("Pedidos pendientes")
        if len(self._pedidos_pendientes)==0:
            print("No hay pedidos pendientes")
        else:
            for pedido in self._pedidos_pendientes:
                pedido.mostrar_datos()
                print("----------")

    def obtener_piezas(self):
        return self._piezas
     
    def mostrar_clientes(self):
        for cliente in self._clientes:
            cliente.mostrar_datos()
            print("----------") #polimorfismo se refiere a las dos de manera distinta

    def mostrar_piezas(self):
        for pieza in self._piezas:
            pieza.mostrar_datos()
            print("----------")

    def mostrar_maquinas(self):
        for maquina in self._maquinas:
            maquina.mostrar_datos()
            print("----------")