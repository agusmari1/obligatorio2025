
sistema = Sistema() 

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
    if objetoAregistrar == 1:
        pass
    elif objetoAregistrar == 2:
        pass
    elif objetoAregistrar ==3:
        pass
    elif objetoAregistrar == 4:
        pass
    elif objetoAregistrar == 5:
        pass
        
    

def opcion_listar (menu_listar):
    for linea in menu_listar:
        print (linea[0])
    print ("----------------")


while opcion_NOvalida(opcion1_2_3):
    print ("El valor ingresado no es valido")
    opcion1_2_3 = int(input("Ingrese los valores1,2 o 3: "))


if opcion1_2_3 == 1:
    opcion_registrar (menu_registrar)
elif opcion1_2_3 == 2:
    opcion_listar (menu_listar)
elif opcion1_2_3 == 3:
    print ("Saliste del sistema")
else:
    opcion_NOvalida (opcion1_2_3)


    def desplegar_menu(menu_principal):
        for linea in menu_principal:
            print(linea[0])
        print ("-----------------------------")
    opcion1_2_3= int(input("Ingrese la opcion que desea ejecutar:registrar, listar o salir:"))

    def opcion_no_valida(opcion1_2_3):
        if (opcion1_2_3<1)or (opcion1_2_3>3):
            return True
        else:
            return False
        
    def opcion_registrar(menu_registrar):
        for linea in menu_registrar:
            print(linea[0])
        print ("-----------------------------")
        opcion_a_registar=int(input("Ingrese una opción"))
        def registrar_pieza():
            descripción=input("ingrese la descripción del objeto")
            costo_adquisicion=input("ingrese el costo de adquisición del objeto")
            unidades_en_lote=input("ingrese la cantidad de unidades del lote del objeto")
            cantidad_disponible=input("ingrese la cantidad disponible del objeto")
        def registrar_maquina():
            descripcion=input("ingrese una descripcion de la maquina")
        if opcion_a_registar==1:
            print ("Se va a registar una nueva pieza")
            registrar_pieza()

        if opcion_a_registar==2:
            print ("Se va a registar una nueva pieza")
            registrar_maquina()
          






    

    


