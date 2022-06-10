#Menú Programa
# 1.CLIENTES (DNI, AP Y NOMBRE, E-MAIL)
#       1.ALTA CLIENTE      
#       2.MOFIFICACION CLIENTE 
#       3.BAJA CLIENTE 
#       4.LISTADO DE CLIENTES
#       9.VOLVER AL MENU PPAL
# 2.PRODUCTOS
#       1.ALTA NUEVO PRODUCTO
#       2.MODIFICACION PRODUCTO
#       3.BAJA PRODUCTO
# 3.STOCK
#       1.ALTA NUEVO MATERIAL
#       2.MODIFICACION COSTO MATERIAL
#       3.ACTUALIZACION STOCK MATERIAL
#       4.REPORTE DE MATERIALES EN STOCK
#       5.REPORTE DE MATERIALES SIN STOCK
#       9.VOLVER AL MENU PPAL
# 4.PEDIDOS
#       1.ALTA NUEVO PEDIDO (DNI, PRODUCTO, CANTIDAD)
#       2.LISTADO DE PEDIDOS POR CLIENTE
#       3.LISTADO DE PEDIDOS POR FECHA
#       9.VOLVER AL MENU PPAL
# 9.SALIR


def mainMenu():
    print("MENU PRINCIPAL\n","\t1.CLIENTES\n""\t2.PRODUCTOS\n""\t3.STOCK\n""\t4.PEDIDOS\n""\t9.SALIR\n")
    option=int(input("Ingrese una opción del Menú:\n"))
    while True:
        if option == 1:
            print("llamar a menu clientes")
            option=int(input("Ingrese una opción del Menú:\n"))
        elif option == 2:
            print("llamar a menu productos")
            option=int(input("Ingrese una opción del Menú:\n"))
        elif option == 3:
            print("llamar a menu stock")
            option=int(input("Ingrese una opción del Menú:\n"))
        elif option == 4:
            print("llamar a menu materiales")
            option=int(input("Ingrese una opción del Menú:\n"))   
        elif option == 9:
            print("¿Está seguro que desea abandonar el Sistema?\n")
            optionExit=(input("Presione 'S' para Salir o 'N' para seguir trabajando:  "))
            if optionExit.upper()=="N":
                print("MENU PRINCIPAL\n","\t1.CLIENTES\n""\t2.PRODUCTOS\n""\t3.STOCK\n""\t4.PEDIDOS\n""\t9.SALIR\n")
                option=int(input("Ingrese una opción del Menú:\n"))
            elif optionExit.upper()=="S":
                break
            else:
                optionExit=(input("Presione 'S' para Salir o 'N' para seguir trabajando:  "))
        else: 
            print("no es una opcion de menu valida")
            print("MENU PRINCIPAL\n","\t1.CLIENTES\n""\t2.PRODUCTOS\n""\t3.STOCK\n""\t4.PEDIDOS\n""\t9.SALIR\n")
            option=int(input("Ingrese una opción del Menú:\n"))
    exit


mainMenu()