# from cliente import ClienteParticular, Empresa
# from maquina import Maquina
# from pedido import Pedido
# from pieza import Pieza
# from reposicion import Reposicion
# from requerimiento import Requerimiento
# from sistema import Sistema

menu_principal = [["1.Registrar:"],
        ["           1.Pieza"],
        ["           2.Maquina"],
        ["           3.Cliente"],
        ["           4.Pedido"],
        ["           5.Reposicion"],
        ["           6.Salir"],
        ["2. Listar:"],
        ["           1.Clientes"],
        ["           2.Pedidos"],
        ["           3.Maquinas"],
        ["           4.Piezas"],
        ["           5.Contabilidad"],
        ["           6.Salir"],
        ["3.Salir del Sistema"]]

menu_registrar = [["Registrar:"],
        ["               1.Pieza"],
        ["               2.Maquina"],
        ["               3.Cliente"],
        ["               4.Pedido"],
        ["               5.Reposicion"],
        ["               6.Salir"]]


menu_listar =[["Listar:"],
        ["           1.Clientes"],
        ["           2.Pedidos"],
        ["           3.Maquinas"],
        ["           4.Piezas"],
        ["           5.Contabilidad"],
        ["           6.Salir"]]


for linea in menu_principal:
    print(linea[0])

print ("-----------------------------")

opcion1_2_3= int(input("Ingrese la opcion que desea ejecutar:registrar, listar o salir:"))

if opcion1_2_3 == 1:
    opcion_registrar ()
elif opcion1_2_3 == 2:
    listar ()
elif opcion1_2_3 == 3:
    print ("Saliste del sistema")
    
def opcion_NOvalida (opcion1_2_3):
    if (opcion1_2_3<1) or (opcion1_2_3>3):
        return True
    else:
        return False
    
while opcion_NOvalida(opcion1_2_3):
    print ("El valor ingresado no es valido")
    opcion1_2_3 = int(input("Ingrese los valores1,2 o 3: "))

def opcion_registrar ():
    for linea in menu_registrar:
        print (linea[0])




    

    


