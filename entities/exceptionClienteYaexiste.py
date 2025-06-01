
class ClienteRepetido(Exception):
    def __init__(self, mensaje = "Ya existe un cliente con esa cedula"):
        super().__init__(mensaje)
         
    
        
       
