class Pieza:
    _codigo_unico = 0

    #contructor
    def __init__(self,descripcion,costo_adquisicion,unidades_en_lote,cantidad_disponible=0,):

        Pieza._codigo_unico += 1
        self._codigo= Pieza._codigo_unico

        self._descripcion = descripcion
        self._costo_adquisicion= costo_adquisicion
        self._cantidad_disponible=cantidad_disponible
        self._unidades_en_lote=unidades_en_lote

    #getter

    @property
    def codigo(self):
        return self._codigo
        
    @property
    def descripcion(self):
        return self._descripcion
        
    @property
    def costo_adquisicion(self):
        return self._costo_adquisicion
        
    @property
    def cantidad_disponible(self):
        return self._cantidad_disponible
        
    @property
    def unidades_en_lote(self):
        return self._unidades_en_lote
        
    #setter

    @cantidad_disponible.setter
    def cantidad_disponible(self,nueva_cantidad):
        self._cantidad_disponible=nueva_cantidad
        
    #metodos de accion

    def reponer(self,cantidad_de_lotes):
        self._cantidad_disponible+=cantidad_de_lotes* self._unidades_en_lote

    #metodo de impresion

   
    def pedido_listar_demanda_piezas(self):
        for pieza in self._piezas:
            total_necesario=0
            for pedido in self._pedido:
                if pedido.estado=="pendiente":
                    for req in pedido.requerimientos:
                        if req.pieza==pieza:
                            total_necesario+=req.cantidad

        faltan=total_necesario-pieza.cantidad_disponible
        if faltan<0:
            faltan=0
        if faltan>0:
            lotes=faltan/pieza.unidades_en_lote
            if faltan%pieza.unidades_en_lote!=0:
                lote+=1
            else:
                lote=0

    # def mostrar_datos(self):
    # "Código:", self._codigo)
    #         print("Descripción:", self._descripcion)
    #         print("Costo:", self._costo_adquisicion)
    #         print("Cantidad disponible:", self._cantidad_disponible)
    #         print("Unidades por lote:", self._unidades_en_lote)  
    #        print("Faltan:",faltan)


    def __str__(self):
        return f"{self.codigo}-{self.descripcion}"
 