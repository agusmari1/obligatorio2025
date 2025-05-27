# import sys 
# sys.path.append(r'C:\\Users\\Usuario\\OneDrive - Universidad de Montevideo\\Documentos\\GitHub\\obligatorio2025')

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from sistema import Sistema
from maquina import Maquina
from pieza import Pieza
from cliente import Cliente, ClienteParticular, Empresa

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
        requerimientos=[]
        piezas_disponibles=sistema.obtener_piezas()
        if len (piezas_disponibles)==0:
            print("No hay piezas disponibles")
        else: 
            continuar="si"
            while continuar=="si":
                for pieza in piezas_disponibles:
                    print(f"{pieza.codigo}: {pieza.descripcion}")
                    cantidad=int(input("que cantidad de esa pieza necesitás"))
                    codigo=int(input("ingrese un codigo para su pieza"))
                    
                    pieza_seleccionada=None
                    for p in piezas_disponibles:
                        if p.codigo==codigo:
                            pieza_seleccionada=p
                            break
                        
                        if pieza_seleccionada:
                            req=Requerimiento(pieza_seleccionada,cantidad)
                            requerimientos.append(req)
                            continuar=input("deseas agregar otra pieza (si/no)")
                        else:
                            print("Codigo no valido")
                        
                        nueva_maquina=Maquina(descripcion)
                        for req in requerimientos:
                            nueva_maquina.agregar_requerimiento(req)

                        sistema.registro_maquina(nueva_maquina)




                                   
            


# REGISTRAR UN CLIENTE
    elif objetoAregistrar ==3:
        print ("Se va a registrar un cliente")
        tipo_cliente=input("cliente particular o Empresa")
        nombre=input("seleccione el nombre")
        telefono=input("seleccione el telefono")
        correo_electrónico=input("indique el correo electrónico")
        if tipo_cliente=="particular":
            cedula=input("ingrese la cedula")
            nuevo_cliente= ClienteParticular(nombre,telefono,correo_electrónico,cedula)

        else:
            pagina_web=input("ingrese la pagina web")
            RUT=input("ingrese el rut")
            nuevo_cliente=Empresa(nombre,telefono,correo_electrónico,RUT,pagina_web)

        sistema.registro_clientes(nuevo_cliente)

# REGISTRAR UN PEDIDO
    elif objetoAregistrar == 4:
        print ("Se va a registrar un pedido")
        sistema.registro_pedido(nuevo_cliente,Maquina)

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
       







    

    


