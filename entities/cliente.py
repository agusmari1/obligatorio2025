from abc import ABC
class Cliente(ABC):
    
    _id_unico=0
    def __init__ (self,nombre,telefono,correo_electrónico):
        Cliente._id_unico+=1
        self._identidad=Cliente._id_unico
        self._nombre=nombre
        self._telefono=telefono
        
        self._correo_electronico=correo_electrónico

    @property
    def nombre(self):
            return self._nombre
    @property
    def telefono(self):
            return self._telefono
    @property
    def correo_electronico(self):
            return self._correo_electronico
    
    def tipo_cliente(self):
          pass
    
class ClienteParticular(Cliente):
        def __init__(self,nombre,telefono,correo_electrónico,cedula):
            super().__init__(nombre,telefono,correo_electrónico)
            self._cedula=cedula

        @property
        def cedula(self):
            return self._cedula
        
        @cedula.setter
        def cedula(self, nueva_cedula):
            self._cedula = nueva_cedula
        
        def tipo_cliente(self):
              return "cliente particular"
  
class Empresa(Cliente):
    def __init__(self,nombre,telefono,correo_electrónico,RUT,pagina_web):
        super().__init__(nombre,telefono,correo_electrónico)
        self._RUT=RUT
        self._pagina_web=pagina_web
    
    def tipo_cliente(self):
        return "Empresa"

    @property
    def RUT(self):
        return self._RUT
    
    @property
    def pagina_web(self):
        return self._pagina_web
    

    def _puede_entregarse(self):
        for req in self._maquina.requerimientos: #recorre los requerimientos de la maquina(cada requerimiento es:una pieza y cuentas necesita)
            if req.pieza.cantidad_disponible <req.cantidad: # cuantas hay en stock<cuantas necesita la maquina
                return False
        return True

   
   