
class ClienteRepetido(Exception):
    def _init__(self):
        pass
        print("El cliente ya existe")
        nueva_cedula=input("vuelva a ingresar la cedula")
        self.cedula=nueva_cedula
