from entities. import Sistema
from entities.maquina import Maquina
from entities.pieza import Pieza

sistema = Sistema() #crear una instancia para poder usar las funciones 
#por que en este caso si y en los otros que llamamos a otras clases no?

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

# IMPRIMIR EL MENU
for linea in menu_principal:
    print(linea[0])
   
print ("-----------------------------")
#INGRESE LA OPCION 
opcion1_2_3= int(input("Ingrese la opcion que desea ejecutar:registrar, listar o salir:"))

def opcion_NOvalida (opcion1_2_3):
    if (opcion1_2_3<1) or (opcion1_2_3>3):
        return True
    else:
        return False

def opcion_registrar (menu_registrar):
    for linea in menu_registrar:
        print (linea[0])
    print ("-----------------")
    objetoAregistrar = int(input("Ingrese una opcion: "))

#REGISTRAR UNA PIEZA 
    if objetoAregistrar == 1:
        print ("Se va a registrar una nueva pieza")
        descripcion = input("Ingrese la descrpcion de la pieza")
        costo_adquisicion= float(input("ingrese el costo de adquisición de la pieza"))
        unidades_en_lote= int(input("ingrese la cantidad de unidades de la pieza"))
        cantidad_disponible= int(input("Ingrese la cantidad"))
        sistema.registro_pieza(descripcion, costo_adquisicion, unidades_en_lote, cantidad_disponible)

#REGISTRAR UNA MAQUINA
    elif objetoAregistrar == 2:
        print ("Se va a registrar una nueva maquina")
        descripcion = input("Ingrese la descripcion de la maquina")
    
# REGISTRAR UN CLIENTE
    elif objetoAregistrar ==3:
        print ("Se va a registrar un cliente")

# REGISTRAR UN PEDIDO
    elif objetoAregistrar == 4:
        print ("Se va a registrar un peido")

#REGISTRAR UNA REPOSICION
    elif objetoAregistrar == 5:
        print ("Piezas disponibles:")
        for piezas in sistema._piezas:
            print (pieza.codigo)

        pieza_a_reponer = input("Ingrese el nombre de la pieza que desea reponer")
        cantidad_lotes_a_reponer = int(input("Ingrese la cantidad de lotes que se van a reponer"))
        sistema.registro_reposicion (pieza_a_reponer,cantidad_lotes_a_reponer)

        
    
def opcion_listar (menu_listar):
    for linea in menu_listar:
        print (linea[0])
    print ("----------------")


while opcion_NOvalida(opcion1_2_3):
    print ("El valor ingresado no es valido")
    opcion1_2_3 = int(input("Ingrese los valores1,2 o 3: "))

#DISTINTAS OPCIONES PARA EL VALOR INGRESADO
if opcion1_2_3 == 1:
    opcion_registrar (menu_registrar)
elif opcion1_2_3 == 2:
    opcion_listar (menu_listar)
elif opcion1_2_3 == 3:
    print ("Saliste del sistema")
else:
    opcion_NOvalida (opcion1_2_3)
       







    

    


