from requerimientos import Requerimiento

class Maquina:
    _codigo_unico=0
    def __init__(self,descripcion):
        Maquina._codigo_unico+=1
        self._codigo= Maquina._codigo_unico

        self._descripcion=descripcion
        self._requerimientos=[]
        self._costo_produccion=0.0

    @property
    def codigo(self):
        return self._codigo
    
    @property
    def descripcion(self):
        return self._descripcion
    @property
    def requerimientos (self):
        return self._requerimientos
    
    @property
    def costo_produccion (self):
        return self._costo_produccion
    
    def agregar_requerimiento(self,requerimiento):
        self._requerimientos.append(requerimiento)
        self._actualizar_costo()
    
    def _actualizar_costo(self):
        total=0
        for elemento in self._requerimientos:
            pieza=elemento.pieza
            cantidad=elemento.cantidad
            subtotal= pieza.costo_adquisicion*cantidad
            total+=subtotal
        self._costo_produccion=total

    def actualizar_stock(self):
        for req in self._requerimientos:
            pieza=req.pieza
            cantidad=req.cantidad
            pieza.cantidad_disponible-=cantidad

    def mostrar_datos(self):
        print("Descripción:",self._descripcion)
        print("Costo producción:",self._costo_produccion)
        print("Va a requerir")
        for req in self._requerimientos:
            print("-",req.cantidad, "-",req.pieza.descripcion)