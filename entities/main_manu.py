from sistema import Sistema
from cliente import Cliente, ClienteParticular, Empresa
from pedido import Pedido
from requerimientos import Requerimiento
from reposicion import Reposicion
from maquina import Maquina
from pieza import Pieza
from exceptionClienteYaexiste import ClienteRepetido
from exceptionPiezaYaExiste import PiezaRepetida

sistema = Sistema() #crear una instancia para poder usar las funciones 

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
def menu_principal ():
    print ("Menu Principal:")
    print ("    1.Registrar")
    print ("    2.Listar")
    print ("    3.Salir del  sistema")
    print ("-----------------------------")
    

#OPCION DISTINTA A 1,2,3
def opcion_NOvalida (opcion1_2_3):
    if (opcion1_2_3<1) or (opcion1_2_3>3):
        return True
    else:
        return False
    

#OPCION REGISTRAR ALGO
def opcion_registrar (menu_registrar):
    while True:
        for linea in menu_registrar:
            print (linea[0])
        print ("----------------------------")
        objetoAregistrar = int(input("Ingrese una opcion: "))
   
#REGISTRAR UNA PIEZA 
        if objetoAregistrar == 1:
            print ("Se va a registrar una nueva pieza")
            while True:
                try:
                    descripcion = input("Ingrese la descripcion de la pieza: ")
                    for pieza in sistema._piezas:
                        if pieza.descripcion==descripcion:
                            raise PiezaRepetida()
                        if descripcion==" ":
                            raise ValueError() #la descripcion no puede ser vacia 
                    break
                except PiezaRepetida as e:
                    print(e)
                except ValueError as ve:
                    print(ve)
            
            costo_adquisicion= float(input("ingrese el costo de adquisición de la pieza: "))
            unidades_en_lote= int(input("ingrese la cantidad de lotes de la pieza: "))
            cantidad_disponible= int(input("Ingrese la cantidad por lote: "))
            sistema.registro_pieza(descripcion, costo_adquisicion, unidades_en_lote, cantidad_disponible)
            
        
#REGISTRAR UNA MAQUINA
        elif objetoAregistrar == 2:
            print ("Se va a registrar una nueva maquina")
            descripcion = input("Ingrese la descripcion de la maquina: ")
            requerimientos=[]
            piezas_disponibles=sistema.obtener_piezas()
            if len (piezas_disponibles)==0:
                print("No hay piezas disponibles")
                print ("------------------------")
            else: 
                continuar = "si"
                while continuar=="si":
                    print ("Piezas disponibles: ")
                    for pieza in piezas_disponibles:
                        print (pieza.codigo, "-", pieza.descripcion)
                    codigo=int(input("Ingrese el codigo de la pieza que necesita: "))
                    pieza_seleccionada = None

                    for pieza in piezas_disponibles:
                        if pieza.codigo == codigo:
                            pieza_seleccionada = pieza
                            break
                    while pieza_seleccionada is None:
                            print ("No se encontro una pieza con ese codigo")
                            codigo = int(input("Ingrese un codigo valido: "))
                            for pieza in piezas_disponibles:
                                if pieza.codigo == codigo:
                                    pieza_seleccionada = pieza
                                    break

                    if pieza_seleccionada is not None:
                            print (pieza)
                            cantidad=int(input("Que cantidad de esa pieza necesitás: "))
                            req=Requerimiento(pieza_seleccionada,cantidad)
                            requerimientos.append(req)
                            piezas_disponibles.remove(pieza_seleccionada)
                    continuar=input("Deseas agregar otra pieza (si/no): ")
                
                                
                        
                nueva_maquina=Maquina(descripcion)
                for req in requerimientos:
                    nueva_maquina.agregar_requerimiento(req)

                sistema.registro_maquina(nueva_maquina)
                print ("Se ha registrado correctamente la maquina")
                print ("----------------------------------------")
                

# REGISTRAR UN CLIENTE
        elif objetoAregistrar ==3:
            print ("Se va a registrar un cliente")
            print ("Tipo de cliente:")
            print ("            1. Cliente Particular")
            print ("            2. Empresa")
            tipo_cliente= int(input("Seleccione la opcion 1 o 2: "))
            
            if tipo_cliente== 1:

                nombre=input("Seleccione el nombre: ")

                while True:

                    cedula=input("Ingrese la cedula: ")

                    try:
                        for cliente in sistema._clientes:
                            if isinstance(cliente,ClienteParticular) and cliente.cedula==cedula:
                                raise ClienteRepetido("Ya existe un cliente con esa cedula")
                        break
                    except ClienteRepetido as e:
                        print (e)
                        print ("Vuelve a registrar la cedula")

                telefono=input("Seleccione el telefono: ")
                correo_electrónico=input("Indique el correo electrónico: ")
            
                nuevo_cliente= ClienteParticular(nombre,telefono,correo_electrónico,cedula)
                sistema.registro_clientes(nuevo_cliente)
                print ("Se ha registrado el cliente")
                print ("---------------------------")
                


            elif tipo_cliente==2:
                nombre=input("Seleccione el nombre: ")
                telefono=input("Seleccione el telefono: ")
                correo_electrónico=input("Indique el correo electrónico: ")
                while True:
                    RUT =input("Ingrese el rut: ")
                    try:
                        for cliente in sistema._clientes:
                            if isinstance(cliente,Empresa) and cliente.RUT==RUT:
                                raise ClienteRepetido()
                        break
                    
                    except ClienteRepetido as e:
                        print (e)

                pagina_web=input("Ingrese la pagina web: ")
                nuevo_cliente=Empresa(nombre,telefono,correo_electrónico,RUT ,pagina_web)
                sistema.registro_clientes(nuevo_cliente)
                print ("Se ha registrado la empresa")
                print ("---------------------------")
                

            else:
                print("Ese tipo de cliente no existe")
                print ("----------------------------")
                

# REGISTRAR UN PEDIDO
        elif objetoAregistrar == 4:
            print ("Se va a registrar un pedido")
            if len(sistema._clientes) == 0: #Si no hay clientes, no puede haber pedido
                print("No hay clientes registrados")
                print("---------------------------")
            else:
                print("Clientes dispomibles: ")
                for i in range (len(sistema._clientes)):
                    cliente = sistema._clientes [i]
                    print (i + 1, " - ", cliente.nombre, "-", cliente.tipo_cliente())
                indice_cliente = int(input("Seleccione el numero de cliente que realiza el pedido: "))
                cliente_seleccionado = sistema._clientes [(indice_cliente -1)]
                if len(sistema._maquinas) == 0:
                    print ("No hay maquinas registradas")
                    print ("---------------------------")
                else:
                    print ("Maquinas disponibles: ")
                    for i in range(len(sistema._maquinas)):
                        maquina = sistema._maquinas [i] # cada elemento de la lista es un objeto maquina
                        print (i + 1, " - ", maquina.descripcion) #como cada maquina es un objeto, aca solo usamos el atributo descripcion que es el que nos interesa
                    indice_maquina = int(input("Ingrese el numero de la maquina a pedir: "))
                    maquina_seleccionada = sistema._maquinas [(indice_maquina -1)]
                    sistema.registro_pedido(cliente_seleccionado, maquina_seleccionada)
            # se acaba de registar un pedido
            #ahora lo que se va a hacer es buscar ese pedido registrado para ver si queda pendiente o no
                    pedido_hecho = None
                    for pedido in sistema._pedidos_entregados:
                        if pedido._cliente == cliente_seleccionado and pedido._maquina == maquina_seleccionada:
                            pedido_hecho = pedido
                            break
                    for pedido in sistema._pedidos_pendientes:
                        if pedido._cliente == cliente_seleccionado and pedido._maquina == maquina_seleccionada:
                            pedido_hecho = pedido
                            break
                    print ("Estado del pedido: ")
                    if pedido_hecho is not None:
                        if pedido_hecho.estado == "entregado":
                            print ("Fue entregado correctamente")
                            print ("-------------------")
                        else:
                            print ("El estado del pedido quedo pendiente por falta de stock")
                            print ("------------------------------------------------------")
            


#REGISTRAR UNA REPOSICION
        elif objetoAregistrar == 5:
            print ("Piezas disponibles:")
            for pieza in sistema._piezas:
                print (pieza.codigo, "-", pieza.descripcion , " - cantidad por lote - ", pieza.unidade_en_lote)
            codigo_pieza_a_reponer = int(input("Ingrese el codigo de la pieza que desea reponer: "))
            pieza_encontrada = None
            for pieza in sistema._piezas:
                if pieza.codigo == codigo_pieza_a_reponer:
                    pieza_encontrada = pieza
                    break
                    
            if pieza_encontrada is not None:
                cantidad_lotes = int(input("Ingrese la cantidad de lotes que se van a reponer: "))
                sistema.registro_reposicion (pieza_encontrada, cantidad_lotes)
                costo_reposicion = cantidad_lotes*pieza_encontrada.unidades_en_lote*pieza_encontrada.costo_adquisicion
                print ("Reposicion registrada correctamenrte")
                print ("Costo de la reposic[on: ", costo_reposicion)
                print ("Actualizacion de stock de la pieza: ", pieza_encontrada.cantidad_disponible)
                print ("-------------------------------------------")
                
            else:
                print ("No se encontró ninguna pieza con ese codigo")
                print ("-------------------------------------------")

#SAlIR DE REGISTRAR
        elif objetoAregistrar == 6:
            print ("Se vuelve al menu principal")
            print ("-----------------------------")
            break
            
        else:
            objetoAregistrar = int(input("Ingrese un numero del 1 al 6"))
        

        
    
def opcion_listar (menu_listar):
    for linea in menu_listar:
        print (linea[0])
    print ("-----------------------")
    objetoAListar = int(input("INgrese la opcion que desea listar"))
    if objetoAListar == 1:
        listaclientes = sistema.mostrar_clientes
    if objetoAListar == 2:
        pass
    if objetoAListar ==3:
        pass
    if objetoAListar== 4:
        pass
    if objetoAListar == 5:
        pass




#DISTINTAS OPCIONES PARA EL VALOR INGRESADO

while True:
    menu_principal()
    opcion1_2_3=int(input("Ingrese la opción que desea ejecutar: "))
  
    if opcion1_2_3 == 1:
            opcion_registrar (menu_registrar)
    elif opcion1_2_3 == 2:
            opcion_listar (menu_listar)
    elif opcion1_2_3== 3:
            print ("Saliste del sistema")
            break
    else:
        print("El valor ingresado no es valido")
        print ("Se debe ingresar 1, 2 o 3")
        print ("-------------------------------")

      

       







    

    


