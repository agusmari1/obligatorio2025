from cliente import Cliente,ClienteParticular,Empresa
from maquina import Maquina
from pedido import Pedido
from reposicion import Reposicion
from requerimientos import Requerimiento
from datetime import datetime
from pieza import Pieza
import math

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
    
    def registro_maquina(self, maquina):
        self._maquinas.append(maquina)

    def registro_reposicion(self,pieza, cantidad_lotes):
        reposicion = Reposicion(pieza, cantidad_lotes)
        self._reposiciones.append(reposicion)
        self.actualizar_pedidos_pendientes()

    def actualizar_pedidos_pendientes(self):
        pendientes_entregados = []
        for pedido in self._pedidos_pendientes:
            if pedido._puede_entregarse():
                pedido._estado="entregado"
                pedido._fecha_entrega=datetime.now()
                pedido.actualizar_stock()
                self._pedidos_entregados.append(pedido)
                pendientes_entregados.append (pedido)
        for pedido in pendientes_entregados:
                self._pedidos_pendientes.remove(pedido)

    def mostrar_pedidos_entregados(self):
        print("Pedidos entregados:")
        if len(self._pedidos_entregados)==0:
            print("No hay pedidos entregados")
        else:
            for pedido in self._pedidos_entregados:
                pedido.mostrar_datos()
                print("----------")

    def mostrar_pedidos_pendientes(self):
        print("Pedidos pendientes: ")
        if len(self._pedidos_pendientes)==0:
            print("No hay pedidos pendientes")
        else:
            for pedido in self._pedidos_pendientes:
                pedido.mostrar_datos()
                print("----------")

    def obtener_piezas(self):
        return self._piezas
     
    def mostrar_clientes(self):
        clientes_todos=[]
        for cliente in self._clientes:
            if isinstance(cliente,ClienteParticular):
                datos= [cliente._nombre, cliente._telefono, cliente._correo_electronico, cliente._cedula, "Cliente Particular"]
            elif isinstance(cliente,Empresa):
               datos= [cliente._nombre, cliente._telefono, cliente._correo_electronico, cliente._RUT, cliente._pagina_web, "Empressa"]
            clientes_todos.append(datos)
            #polimorfismo se refiere a las dos de manera distinta
        return clientes_todos
    
    def mostrar_piezas(self):
        for pieza in self._piezas:
            pieza.mostrar_datos()
            print("----------")

    def pedido_listar_demanda_piezas(self):
        for pieza in self._piezas:
            total_necesario=0
            for pedido in self._pedidos_pendientes:
                maquina=pedido.maquina
                for req in maquina._requerimientos:
                    if req.pieza==pieza:
                        total_necesario+=req.cantidad

            faltan=total_necesario-pieza.cantidad_disponible
            if faltan<0:
                faltan=0
            lotes=0
            if faltan>0:
                lotes=math.ceil(faltan/pieza.unidades_en_lote)
            
                    
            print("Pieza:", pieza.descripcion)
            print("Disponible:", pieza.cantidad_disponible)
            print("Cantidd en lote:", pieza.unidades_en_lote)
            print("Faltan:", faltan)
            print("Lotes a comprar:", lotes)
            print("--------------")

    def mostrar_maquina(self):
        for maquina in self._maquinas:
            puede_fabricarse=True
            for req in maquina._requerimientos:
                if req.cantidad > req.pieza.cantidad_disponible:
                        puede_fabricarse = False
                        break
            print(f"Maquina:",maquina._descripcion)

            if puede_fabricarse:
                print("Maquina disponible a la venta")
                   
            else:
                 print("Maquina no disponible para la venta")

    def costo_produccion_total(self):
        costo_produccion=0
        precio_venta=0
        for pedido in self._pedidos_entregados:
            maquina=pedido._maquina
            costo_produccion+=maquina.costo_produccion

            precio_venta+=pedido.calcular_precio()

        ganancia_bruta=precio_venta-costo_produccion
        impuesto=ganancia_bruta*0.25
        ganancia_neta=ganancia_bruta-impuesto

    
        print(f"Costo total: ${costo_produccion}")
        print(f"Precio venta total: ${precio_venta}")
        print(f"Ganancia bruta: ${ganancia_bruta}")
        print(f"Impuesto (25% IRAE): ${impuesto}")
        print(f"Ganancia neta: ${ganancia_neta}")
      
        
    


            


                   



