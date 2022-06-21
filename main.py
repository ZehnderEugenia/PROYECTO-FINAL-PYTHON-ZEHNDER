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
#       4.LISTADO DE PRODUCTOS  
# 3.STOCK
#       1.ALTA NUEVO MATERIAL
#       2.MODIFICACION COSTO MATERIAL
#       3.ACTUALIZACION STOCK MATERIAL
#       4.LISTADO DE MATERIALES EN STOCK
#       5.LISTADO DE MATERIALES SIN STOCK
#       9.VOLVER AL MENU PPAL
# 4.PEDIDOS
#       1.ALTA NUEVO PEDIDO (DNI, PRODUCTO, CANTIDAD)
#       2.LISTADO DE PEDIDOS POR CLIENTE
#       3.LISTADO DE PEDIDOS POR FECHA
#       9.VOLVER AL MENU PPAL
# 9.SALIR


import os
import pandas as pd
import openpyxl

def CustomerRegist():  
    ClientFile = "client.xlsx"
    Cl = pd.read_excel(ClientFile)
    print("Se añadirá un producto")
    newClient = {"Id":"" , "Name":"" , "Email":""}
    newClient["Id"] = str(input("Escribe el dni del nuevo cliente: "))
    newClient["Name"] = str(input("Escribe el nombre del cliente: "))
    newClient["Email"] = str(input("Escribe el imei del cliente: "))
    Cl = Cl.append(newClient, ignore_index=True)
    print(Cl)
    Cl.to_excel("client.xlsx")
     

def ClientMenu():
    print("MENU CLIENTES\n","\t1.ALTA CLIENTE\n""\t2.MODIFICACION CLIENTE\n""\t3.BAJA CLIENTE\n""\t4.LISTADO DE CLIENTES\n""\t9.VOLVER A MENU PRINCIPAL\n")
    option=input("Ingrese una opción del Menú Clientes  :")
    while True:
        if option == "1":
            #print("llamar a menu ALTA CLIENTE")
            CustomerRegist()
            option=input("Ingrese una opción del Menú Clientes:\n")
        elif option == "2":
            print("llamar a menu MODIFICACION CLIENTE")
            option=input("Ingrese una opción del Menú Clientes:\n")
        elif option == "3":
            print("llamar a menu BAJA CLIENTE")
            option=input("Ingrese una opción del Menú Clientes:\n")
        elif option == "4":
            print("llamar a menu LISTADO DE CLIENTES")
            option=input("Ingrese una opción del Menú Clientes:\n")  
        elif option == "9":
            print("MENU PRINCIPAL\n","\t1.CLIENTES\n""\t2.PRODUCTOS\n""\t3.STOCK\n""\t4.PEDIDOS\n""\t9.SALIR\n")
            break
        else: 
            print("no es una opcion de menu válida")
            print("MENU CLIENTES\n","\t1.ALTA CLIENTE\n""\t2.MODIFICACION CLIENTE\n""\t3.BAJA CLIENTE\n""\t4.LISTADO DE CLIENTES\n""\t9.VOLVER A MENU PRINCIPAL\n")
            option=input("Ingrese una opción del Menú Clientes:\n")
    exit    

def ProductMenu():
    print("MENU PRODUCTOS\n","\t1.ALTA NUEVO PRODUCTO\n""\t2.MODIFICACION PRODUCTO\n""\t3.BAJA PRODUCTO\n""\t4.LISTADO DE PRODUCTOS\n""\t9.VOLVER A MENU PRINCIPAL\n")
    option=input("Ingrese una opción del Menú Productos  :")
    while True:
        if option == "1":
            print("llamar a menu ALTA PRODUCTO")
            option=input("Ingrese una opción del Menú Productos:\n")
        elif option == "2":
            print("llamar a menu MODIFICACION PRODUCTO")
            option=input("Ingrese una opción del Menú Productos:\n")
        elif option == "3":
            print("llamar a menu BAJA PRODUCTO")
            option=input("Ingrese una opción del Menú Productos:\n")
        elif option == "4":
            print("llamar a menu LISTADO DE PRODUCTO")
            option=input("Ingrese una opción del Menú Productos:\n")  
        elif option == "9":
            print("MENU PRINCIPAL\n","\t1.CLIENTES\n""\t2.PRODUCTOS\n""\t3.STOCK\n""\t4.PEDIDOS\n""\t9.SALIR\n")
            break
        else: 
            print("no es una opcion de menu válida")
            print("MENU PRODUCTOS\n","\t1.ALTA NUEVO PRODUCTO\n""\t2.MODIFICACION PRODUCTO\n""\t3.BAJA PRODUCTO\n""\t4.LISTADO DE PRODUCTOS\n""\t9.VOLVER A MENU PRINCIPAL\n")
            option=input("Ingrese una opción del Menú Productos:\n")
    exit 

def StockMenu():
    print("MENU STOCK\n","\t1.ALTA NUEVO MATERIAL\n""\t2.MODIFICACION COSTO DE MATERIAL\n""\t3.ACTUALIZACION STOCK MATERIAL\n""\t4.LISTADO DE MATERIALES EN STOCK\n""\t5.LISTADO DE MATERIALES SIN STOCK\n""\t9.VOLVER A MENU PRINCIPAL\n")
    option=input("Ingrese una opción del Menú Stock  :")
    while True:
        if option == "1":
            print("llamar a menu ALTA NUEVO MATERIAL")
            option=input("Ingrese una opción del Menú Stock:\n")
        elif option == "2":
            print("llamar a menu MODIFICACION COSTO DE MATERIAL")
            option=input("Ingrese una opción del Menú Stock:\n")
        elif option == "3":
            print("llamar a menu ACTUALIZACION STOCK MATERIAL")
            option=input("Ingrese una opción del Menú Stock:\n")
        elif option == "4":
            print("llamar a menu LISTADO DE MATERIALES EN STOCK")
            option=input("Ingrese una opción del Menú Stock:\n")
        elif option == "5":
            print("llamar a menu LISTADO DE MATERIALES SIN STOCK")
            option=input("Ingrese una opción del Menú Stock:\n")  
        elif option == "9":
            print("MENU PRINCIPAL\n","\t1.CLIENTES\n""\t2.PRODUCTOS\n""\t3.STOCK\n""\t4.PEDIDOS\n""\t9.SALIR\n")
            break
        else: 
            print("no es una opcion de menu válida")
            print("MENU STOCK\n","\t1.ALTA NUEVO MATERIAL\n""\t2.MODIFICACION COSTO DE MATERIAL\n""\t3.ACTUALIZACION STOCK MATERIAL\n""\t4.LISTADO DE MATERIALES EN STOCK\n""\t5.LISTADO DE MATERIALES SIN STOCK\n""\t9.VOLVER A MENU PRINCIPAL\n")
            option=input("Ingrese una opción del Menú Stock:\n")
    exit       

def OrderMenu():
    print("MENU PEDIDOS\n","\t1.ALTA NUEVO PEDIDO\n""\t2.LISTADO DE PEDIDOS POR CLIENTE\n""\t3.LISTADO DE PEDIDOS POR FECHA\n""\t9.VOLVER A MENU PRINCIPAL\n")
    option=input("Ingrese una opción del Menú Clientes  :")
    while True:
        if option == "1":
            print("llamar a menu ALTA NUEVO PEDIDO")
            option=input("Ingrese una opción del Menú Pedidos:\n")
        elif option == "2":
            print("llamar a menu LISTADO DE PEDIDOS POR CLIENTE")
            option=input("Ingrese una opción del Menú Pedidos:\n")
        elif option == "3":
            print("llamar a menu LISTADO DE PEDIDOS POR FECHA")
            option=input("Ingrese una opción del Menú Pedidos:\n")  
        elif option == "9":
            print("MENU PRINCIPAL\n","\t1.CLIENTES\n""\t2.PRODUCTOS\n""\t3.STOCK\n""\t4.PEDIDOS\n""\t9.SALIR\n")
            break
        else: 
            print("no es una opcion de menu válida")
            print("MENU PEDIDOS\n","\t1.ALTA NUEVO PEDIDO\n""\t2.LISTADO DE PEDIDOS POR CLIENTE\n""\t3.LISTADO DE PEDIDOS POR FECHA\n""\t9.VOLVER A MENU PRINCIPAL\n")
            option=input("Ingrese una opción del Menú Pedidos:\n")
    exit    

def mainMenu():
    print("MENU PRINCIPAL\n","\t1.CLIENTES\n""\t2.PRODUCTOS\n""\t3.STOCK\n""\t4.PEDIDOS\n""\t9.SALIR\n")
    option=input("Ingrese una opción del Menú Principal:\n")
    while True:
        if option == "1":
            #llamar a menu clientes
            ClientMenu()
            option=input("Ingrese una opción del Menú Principal:\n")
        elif option == "2":
            #llamar a menu productos
            ProductMenu()
            option=input("Ingrese una opción del Menú Principal:\n")
        elif option == "3":
            #llamar a menu stock
            StockMenu()
            option=input("Ingrese una opción del Menú Principal:\n")
        elif option == "4":
            #llamar a menu pedidos
            OrderMenu()
            option=input("Ingrese una opción del Menú Principal:\n")
        elif option == "9":
            print("¿Está seguro que desea abandonar el Sistema?\n")
            optionExit=input("Presione 'S' para Salir o 'N' para seguir trabajando:  ")
            if optionExit.upper()=="N":
                print("MENU PRINCIPAL\n","\t1.CLIENTES\n""\t2.PRODUCTOS\n""\t3.STOCK\n""\t4.PEDIDOS\n""\t9.SALIR\n")
                option=input("Ingrese una opción del Menú Principal:\n")
            elif optionExit.upper()=="S":
                break
            else:
                optionExit=input("Presione 'S' para Salir o 'N' para seguir trabajando:  ")
        else: 
            print("no es una opcion de menu valida")
            print("MENU PRINCIPAL\n","\t1.CLIENTES\n""\t2.PRODUCTOS\n""\t3.STOCK\n""\t4.PEDIDOS\n""\t9.SALIR\n")
            option=input("Ingrese una opción del Menú Principal:\n")
    exit

mainMenu()