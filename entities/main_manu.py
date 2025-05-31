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
    for linea in menu_registrar:
        print (linea[0])
    print ("-----------------")
    objetoAregistrar = int(input("Ingrese una opcion: "))
    while True:
      
#REGISTRAR UNA PIEZA 
        if objetoAregistrar == 1:
            print ("Se va a registrar una nueva pieza")
            while True:
                try:
                    descripcion = input("Ingrese la descripcion de la pieza")
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
            cantidad_disponible= int(input("Ingrese la cantidad: "))
            sistema.registro_pieza(descripcion, costo_adquisicion, unidades_en_lote, cantidad_disponible)
            break
        
#REGISTRAR UNA MAQUINA
        elif objetoAregistrar == 2:
            print ("Se va a registrar una nueva maquina")
            descripcion = input("Ingrese la descripcion de la maquina")
            requerimientos=[]
            piezas_disponibles=sistema.obtener_piezas()
            if len (piezas_disponibles)==0:
                print("No hay piezas disponibles")
            else: 
                continuar = "si"
                while continuar=="si":
                    print ("Piezas disponibles: ")
                    for pieza in piezas_disponibles:
                        print (pieza.codigo, "-", pieza.descripcion)
                    codigo=int(input("ingrese el codigo de la pieza que necesita"))
                    pieza_seleccionada = None

                    for pieza in piezas_disponibles:
                        if pieza.codigo == codigo:
                            pieza_seleccionada = pieza
                            break
                    while pieza_seleccionada is None:
                            print ("no se encontro una pieza con ese codigo")
                            codigo = int(input("Ingrese un codigo valido"))
                            for pieza in piezas_disponibles:
                                if pieza.codigo == codigo:
                                    pieza_seleccionada = pieza
                                    break

                    if pieza_seleccionada is not None:
                            print (pieza)
                            cantidad=int(input("que cantidad de esa pieza necesitás"))
                            req=Requerimiento(pieza_seleccionada,cantidad)
                            requerimientos.append(req)
                    continuar=input("deseas agregar otra pieza (si/no)")
                
                                
                        
                nueva_maquina=Maquina(descripcion)
                for req in requerimientos:
                    nueva_maquina.agregar_requerimiento(req)

                sistema.registro_maquina(nueva_maquina)
                print ("Se ha registrado correctamente la maquina")
                break

# REGISTRAR UN CLIENTE
        elif objetoAregistrar ==3:
            print ("Se va a registrar un cliente")
            tipo_cliente=input("cliente particular o Empresa")
            
            if tipo_cliente=="particular":
                while True:
                    nombre=input("seleccione el nombre")
                    cedula=input("ingrese la cedula")
                    telefono=input("seleccione el telefono")
                    correo_electrónico=input("indique el correo electrónico")
                    try:
                        for cliente in sistema._clientes:
                            if isinstance(cliente,ClienteParticular) and cliente.cedula==cedula:
                                raise ClienteRepetido()
                        break
                    except ClienteRepetido as e:
                        print (e)
                        
                    
            
                nuevo_cliente= ClienteParticular(nombre,telefono,correo_electrónico,cedula)
                sistema.registro_clientes(nuevo_cliente)
                break


            elif tipo_cliente=="Empresa":

                while True:
                    nombre=input("seleccione el nombre")
                    telefono=input("seleccione el telefono")
                    correo_electrónico=input("indique el correo electrónico")
                    RUT=input("ingrese el rut")

                    try:
                        
                        for cliente in sistema._clientes:
                            if isinstance(cliente,Empresa) and cliente.RUT==RUT:
                                raise ClienteRepetido()
                        break
                    
                    except ClienteRepetido as e:
                        print (e)
                pagina_web=input("ingrese la pagina web")
                nuevo_cliente=Empresa(nombre,telefono,correo_electrónico,RUT,pagina_web)
                sistema.registro_clientes(nuevo_cliente)
                break

            else:
                print("Ese tipo de cliente no existe")
                break

            #se registra el cliente pero no entiemdo porque cuando pongo la cedula repetida o algo repetido me aparece error ya me fije mil veces y no encuentro el error , tengo que preguntar, pero el resto anda impecable

# REGISTRAR UN PEDIDO
        elif objetoAregistrar == 4:
            print ("Se va a registrar un pedido")
            sistema.registro_pedido(nuevo_cliente,Maquina)

#REGISTRAR UNA REPOSICION
        elif objetoAregistrar == 5:
            print ("Piezas disponibles:")
            for pieza in sistema._piezas:
                print (pieza.codigo, "-", pieza.descripcion)
            codigo_pieza_a_reponer = int(input("Ingrese el codigo de la pieza que desea reponer"))
            pieza_encontrada = None
            for pieza in sistema._piezas:
                if pieza.codigo == codigo:
                    pieza_encontrada = pieza
                    break
                    
            if pieza_encontrada is not None:
                cantidad_lotes = int(input("Ingrese la cantidad de lotes que se van a reponer:"))
                sistema.registro_reposicion (pieza_encontrada, cantidad_lotes)
                print ("Reposicion registrada correctamenrte")
                break
            else:
                print ("No se encontró ninguna pieza con ese codigo")

#SAlIR DE REGISTRAR
        elif objetoAregistrar == 6:
            print ("Se vuelve al menu principal")
            
        else:
            objetoAregistrar = int(input("Ingrese un numero del 1 al 6"))
        

        
    
def opcion_listar (menu_listar):
    for linea in menu_listar:
        print (linea[0])
    print ("----------------")
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
        opcion1_2_3 = int(input("Ingrese los valores1,2 o 3: "))


      

       







    

    


