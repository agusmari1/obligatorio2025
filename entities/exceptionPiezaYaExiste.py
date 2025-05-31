class PiezaRepetida(Exception):
    def __init__(self):
        super().__init__("la pieza ya existe")