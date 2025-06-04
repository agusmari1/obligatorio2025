class Digitos (Exception):
    def __init__(self,mensaje="la cedula tiene que tener 8 digitos"):
        super().__init__(mensaje)
