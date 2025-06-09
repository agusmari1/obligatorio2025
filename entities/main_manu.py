from sistema import Sistema
from cliente import Cliente, ClienteParticular, Empresa
from pedido import Pedido
from requerimientos import Requerimiento
from reposicion import Reposicion
from maquina import Maquina
from pieza import Pieza
from exceptionClienteYaexiste import ClienteRepetido
from exceptionPiezaYaExiste import PiezaRepetida
from exceptionDigitos import Digitos



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
        while True:
            try:
                objetoAregistrar = int(input("Ingrese una opcion: "))
                break
            except ValueError:
                print("Trata de ingresar un numero")
                for linea in menu_registrar:
                    print (linea[0])
                print ("----------------------------")
   
#REGISTRAR UNA PIEZA 
        if objetoAregistrar == 1:
            print ("Se va a registrar una nueva pieza")
            while True:
                try:
                    descripcion = input("Ingrese la descripcion de la pieza: ")
                    for pieza in sistema._piezas:
                        if pieza.descripcion==descripcion:
                            raise PiezaRepetida()
                    if descripcion=="":
                        raise ValueError() #la descripcion no puede ser vacia 
                    break
                except PiezaRepetida as e:
                    print(e)
                except ValueError as e:
                    print(e)
            while True:
                try:
                    costo_adquisicion= float(input("Ingrese el costo de adquisición de la pieza: "))
                    if costo_adquisicion < 0:
                        print ("El costo no puede ser menor a 0")
                        raise ValueError
                    break
                except ValueError:
                    print("Se debe ingresar un numero positivo")
            while True:
                    try:
                        cantidad_lotes= int(input("Ingrese la cantidad de lotes de la pieza: "))
                        if cantidad_lotes < 0:
                            print ("Debe ingresar un numero entero positivo")
                            raise ValueError
                        break
                    except ValueError:
                        print("Vuelva a ingresar un numero")
            while True:
                    try:
                        unidades_en_lote= int(input("Ingrese la cantidad de piezas por lote: "))
                        if unidades_en_lote <= 0:
                            raise ValueError
                        break
                    except ValueError:
                        print("Se deben ingresar solo numeros positivos")
            
            cantidad_disponible = cantidad_lotes*unidades_en_lote
            sistema.registro_pieza(descripcion, costo_adquisicion, unidades_en_lote, cantidad_disponible)
            print("Se registro correctamente")
            
        
#REGISTRAR UNA MAQUINA
        elif objetoAregistrar == 2:
            print ("Se va a registrar una nueva maquina")
            while True:
                try:
                    descripcion = input("Ingrese la descripcion de la maquina: ")
                    if descripcion=="":
                            raise ValueError("Ingrese una descripción")
                    break
                except ValueError as e:
                    print (e)
            requerimientos=[]
            piezas_originales =sistema.obtener_piezas()
            piezas_disponibles = []
            for pieza in piezas_originales:
                piezas_disponibles.append(pieza)
            if len (piezas_disponibles)==0:
                print("No hay piezas disponibles")
                print ("------------------------")
            else: 
                cancelar_registro = False
                continuar = "si"
                while continuar=="si":
                    if len(piezas_disponibles) == 0:
                        cancelar_registro = True
                        break
                    print ("Piezas disponibles: ")
                    for pieza in piezas_disponibles:
                        print (pieza.codigo, "-", pieza.descripcion)
                    while True:
                            try:
                                codigo=int(input("Ingrese el codigo de la pieza que necesita: "))
                                break
                            except ValueError:
                                print ("Se deben ingresar numeros no letras")

                    pieza_seleccionada = None

                    for pieza in piezas_disponibles:
                        if pieza.codigo == codigo:
                            pieza_seleccionada = pieza
                            break
                    while pieza_seleccionada is None:
                        print ("No se encontro una pieza con ese codigo")

                        while True:
                            try:
                                codigo = int(input("Ingrese un codigo valido: "))
                                break
                            except ValueError:
                                print("Ingrese solamente numeros")

                        for pieza in piezas_disponibles:
                            if pieza.codigo == codigo:
                                pieza_seleccionada = pieza
                                break

                    if pieza_seleccionada is not None:
                        print (pieza)

                        while True:
                            try:
                                cantidad=int(input("Que cantidad de esa pieza necesitás: "))
                                if cantidad < 0:
                                    raise ValueError ("La cantidad debe ser un numero positivo")
                                break
                            except ValueError:
                                print("Solo se aceptan numeros, no letras")

                        req=Requerimiento(pieza_seleccionada,cantidad)
                        requerimientos.append(req)
                        piezas_disponibles.remove(pieza_seleccionada)
                        print ("Deseas agregar otra pieza: ")
                        print ("                        1. Si")
                        print ("                        2. No")

                        while True:
                            try:
                                continuar= int(input("Ingrese una opcion: "))
                                if continuar != 1 and continuar !=2:
                                    print ("Se debe ingresar la opcion 1/2")
                                    raise ValueError
                                break
                            except ValueError:
                                print ("No se aceptan letras")

                        while continuar is not None:
                            if continuar == 1:
                                continuar = "si"
                                break
                            elif continuar == 2:
                                continuar = None
                            else: 
                                print ("Elija 1/2")
                                while True:
                                    try:
                                        continuar= int(input("Ingrese una opcion valida: "))
                                        if continuar != 1 and continuar !=2:
                                            print ("Se debe ingresar la opcion 1/2")
                                            raise ValueError
                                        break
                                    except ValueError:
                                        print ("No se aceptan letras")

                                    
                
                if cancelar_registro == True or len(requerimientos)==0:
                    print("No hay mas piezas disponibles")
                    print ("No se registro la maquina")
                    print ("------------------------")
                else:
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
            while True:
                try:
                    tipo_cliente= int(input("Seleccione la opcion 1 o 2: "))
                    break
                except ValueError:
                    print("Ingrese el numero 1/2")
            if tipo_cliente== 1:

                nombre=input("Seleccione el nombre: ")

                while True:
                    try:

                        cedula=input("Ingrese la cedula: ") #necesitas guardarlo como un string para calular el len
                        if cedula.isdigit()==False:
                            raise ValueError()
                        
                        for cliente in sistema._clientes:
                            if isinstance(cliente,ClienteParticular) and cliente.cedula==cedula:
                                raise ClienteRepetido("Ya existe un cliente con esa cedula")
                            
                          
                        if len(cedula)!=8:
                            raise Digitos()
                        
                            
                        break

                    except ClienteRepetido as e:
                        print (e)
                        print ("Vuelve a registrar la cedula")

                    except ValueError:
                        print("Error: la cédula debe contener solo números.")
                        print("Vuelve a registrar la cédula")
                    except Digitos as e:
                        print(e)
    
                while True:
                    try:
                        telefono= input("Seleccione el telefono: ")

                        nuevo_telefono=str(telefono)
                        if nuevo_telefono[0]!="0" and nuevo_telefono[1]!="9":
                            print("El telefono debe empezar con 09")
                            raise ValueError()
                           
                        elif telefono.isdigit()==False:
                            raise ValueError()
                            print("El telefono deben ser solo numeros")
                        elif len((str(telefono)))!= 9:
                            print("El telefono deben ser solo numeros")
                            raise Digitos("El numero debe contener 9 digitos")
                        break
                    except Digitos as e:
                        print (e)
                    except ValueError as e:
                        print(e)
                    
                       
                while True:
                        correo_electrónico=input("Indique el correo electrónico: ")
                        if "@" not in correo_electrónico:
                            print ("El correo electrónico debe tener un @")
                        else:
                            break
              
                nuevo_cliente= ClienteParticular(nombre,telefono,correo_electrónico,cedula)
                sistema.registro_clientes(nuevo_cliente)
                print ("Se ha registrado el cliente")
                print ("---------------------------")
                

            # REGISTRAR CLIENTE EMPRESA
            elif tipo_cliente==2:
                # NOMBRE EMPRESA
                nombre=input("Seleccione el nombre: ")
                # TELEFONO EMPRESA
                while True:
                    try:
                        telefono=input("Seleccione el telefono: ")
                        nuevo_telefono=str(telefono)
                        if nuevo_telefono[0]!="0" and nuevo_telefono[1]!="9":
                            print("El telefono debe empezar con 09")
                            raise ValueError()
                        elif telefono.isdigit()==False:
                            raise ValueError()
                        elif len((str(telefono)))!= 9:
                            raise Digitos("El numero debe contener 9 digitos")
                        break
                    except Digitos as e:
                        print (e)
                    except ValueError:
                        print("El telefono deben ser solo numeros")
                # MAIL EMPRESA
                correo_electrónico=input("Indique el correo electrónico: ")

                # RUT EMPRESA
                while True:
                    
                    try:
                        RUT =input("Ingrese el rut: ")
                        if RUT.isdigit()==False:
                            raise ValueError()
                        for cliente in sistema._clientes:
                            if isinstance(cliente,Empresa) and cliente.RUT==RUT:
                                raise ClienteRepetido()
                        if len(str(RUT)) != 12: #Para transformar algo a string ponemos str para ver el largo
                            raise Digitos ("El Rut debe tener 12 digitos")
                        
                        break
                    
                    except ClienteRepetido as e:
                        print (e)
                    except Digitos as e:
                        print (e)
                    except ValueError:
                        print("Error: el RUT debe contener solo números.")
                        print("Vuelve a registrar el RUT")

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
                print("Clientes disponibles: ")
                for i in range (len(sistema._clientes)):
                    cliente = sistema._clientes [i]
                    print (i + 1, " - ", cliente.nombre, "-", cliente.tipo_cliente())
                while True:
                    try:
                        indice_cliente = int(input("Seleccione el numero de cliente que realiza el pedido: "))
                        if indice_cliente <= 0 or indice_cliente > len(sistema._clientes):
                            raise ValueError
                        cliente_seleccionado = sistema._clientes [(indice_cliente -1)]
                        break
                    except ValueError:
                        print ("Ingrese uno de los numeros que se muestran en pantalla")
                
                if len(sistema._maquinas) == 0:
                    print ("No hay maquinas registradas")
                    print ("---------------------------")
                else:
                    print ("Maquinas disponibles: ")
                    i = 1
                    for maquina in sistema._maquinas:
                        puede_fabricarse = True
                        for req in maquina._requerimientos:
                            if req.cantidad > req.pieza.cantidad_disponible:
                                puede_fabricarse = False
                                break
                        if puede_fabricarse:
                            estado = "Disponible"
                        else:
                            estado = "No hay disponibilidad"
                        print (i, " - ", maquina.descripcion, "-estado: ", estado) #como cada maquina es un objeto, aca solo usamos el atributo descripcion que es el que nos interesa
                        i+= 1
                    while True:
                        try:
                            indice_maquina = int(input("Ingrese el numero de la maquina a pedir: "))
                            if indice_maquina<=0 or indice_maquina > len(sistema._maquinas):
                                raise ValueError
                            maquina_seleccionada = sistema._maquinas [(indice_maquina -1)]
                            break
                        except ValueError:
                            print ("Ingrese uno de los numeros que se muestran en pantalla")

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
            if len(sistema._piezas) == 0:
                print ("No hay piezas para reponer")
                print("-----------------------------")
            else:
                print ("Piezas disponibles:")
                for pieza in sistema._piezas:
                    print (pieza.codigo, "-", pieza.descripcion , " - cantidad por lote: ", pieza.unidades_en_lote, "- costo por pieza:", pieza.costo_adquisicion)
                while True:
                    try:
                        codigo_pieza_a_reponer = int(input("Ingrese el codigo de la pieza que desea reponer: "))
                        break
                    except ValueError:
                        print("Solo se aceptan numeros")
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
#OPCION NO VALIDA       
        else:
            print (("Ingrese un numero del 1 al 6"))
        

        
# OPCION LISTAR
def opcion_listar (menu_listar):
    while True:
        for linea in menu_listar:
            print (linea[0])
        print ("-----------------------")
        while True:
            try:
                objetoAListar = int(input("Ingrese la opcion que desea listar: "))
                break
            except ValueError:
                print("Intente de ingresar un numero: ")
                for linea in menu_listar:
                    print (linea[0])
                print ("-----------------------")
                
    #LISTAR CLIENTES
        if objetoAListar == 1:
            listaclientes = sistema.mostrar_clientes()
            print("Clientes Registrados: ")
            print ("                       ")
            print ("Nombre  | Telefono | Correo | Cedula/ RUT | Web | Tipo de Cliente")
            for cliente in listaclientes:
                if len (cliente) == 5:
                    print (cliente[0], " | ", cliente [1]," | ", cliente[2], " | ", cliente [3], " | ", "  -  ", " | " , cliente [4])
                elif len(cliente) == 6:
                    print (cliente[0], " | ", cliente [1]," | ", cliente[2], " | ", cliente [3], " | ", cliente [4], " | " , cliente [5])

            print ("-----------------------------------------------------------------------------------------------")

    # LISTAR PEDIDOS
        elif objetoAListar == 2:
       
            print("Filtrar:")
            print("1.Sí")
            print("2.No")
            while True:
                try:
                    respuesta=int(input("Elija una opción(1/2): "))
                    if respuesta !=1 and respuesta != 2:
                        raise ValueError
                    break
                except ValueError:
                    print("Seleccione 1/2")

            if respuesta==1:
                print("1.Pendientes")
                print("2.Entregados")
                while True:
                    try:
                        respuesta2=int(input("Elija una opción(1/2): "))
                        if respuesta2 != 1 and respuesta2 != 2:
                            raise ValueError
                        break
                    except ValueError:
                        print ("Elija 1/2: ")
                if respuesta2==1:
                    sistema.mostrar_pedidos_pendientes()
                    
                if respuesta2==2:
                   sistema.mostrar_pedidos_entregados()

            elif respuesta==2:
                sistema.mostrar_pedidos_pendientes()
                print("            ")
                sistema.mostrar_pedidos_entregados()
                

    #LISTAR MAQUINAS
        elif objetoAListar ==3:
            lista_maquinas=sistema.mostrar_maquina()

    #LISTAR PIEZAS
        elif objetoAListar== 4:
            lista_objetos= sistema.pedido_listar_demanda_piezas()

    #LISTAR CONTABILIDAD
        elif objetoAListar == 5:
            costos=sistema.costo_produccion_total()        

    #SALIR
        elif objetoAListar == 6:
            break
    #OTRAS
        else:
            print (("Ingrese un numero del 1 al 6"))



#DISTINTAS OPCIONES PARA EL VALOR INGRESADO EN EL MENU PRINCIPAL

while True:
    menu_principal()
    opcion1_2_3=input("Ingrese la opción que desea ejecutar: ")
    try:
        opcion = int(opcion1_2_3)
    except ValueError:
        print("Solo se deben ingresar numeros")
    else:
  
        if opcion == 1:
            opcion_registrar (menu_registrar)
        elif opcion == 2:
            opcion_listar (menu_listar)
        elif opcion== 3:
            print ("Saliste del sistema")
            break
        else:
            print("El valor ingresado no es valido")
            print ("Se debe ingresar 1, 2 o 3")
            print ("-------------------------------")

      

       







    

    


