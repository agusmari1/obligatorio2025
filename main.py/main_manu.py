
menu = [["1.Registrar:"],
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

registrar = [["Registrar:"],
        ["           1.Pieza"],
        ["           2.Maquina"],
        ["           3.Cliente"],
        ["           4.Pedido"],
        ["           5.Reposicion"],
        ["           6.Salir"]]


listar =[["Listar:"],
        ["           1.Clientes"],
        ["           2.Pedidos"],
        ["           3.Maquinas"],
        ["           4.Piezas"],
        ["           5.Contabilidad"],
        ["           6.Salir"]]
for linea in menu:
    print(linea[0])

opcion1_2_3= int(input("Ingrese la opcion que desea ejecutar:registrar, listar o salir:"))

def opcion_Novalida (opcion1_2_3):
    if (opcion1_2_3 <1) or (opcion1_2_3>3):
        return True
    else:
        return False
    
while opcion_Novalida (opcion1_2_3):
    opcion1_2_3 = int (input ("Ingreselos valores1,2 o 3: "))

if opcion1_2_3 == 1:
    for linea in registrar:
        print (linea[0])
    opcion = int(input("Ingrese el numero de lo que desea registrar"))
    

    


