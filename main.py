intentos = 3
acceso = False
while intentos > 0:

    user = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")

    if user == "pepe" and contraseña == "5555":
        print("Acceso Correcto")
        acceso = True
        break

    else:
        intentos -= 1
        print(f"Acceso Incorrecto. Le quedan {intentos} intentos.")

if intentos == 0:
    print("Se ha bloqueado el acceso. Intente más tarde.")
    
if acceso == True:
    opcion = ""

    while opcion != "9":
        print("\n ===== NETCONTROL ISP  =====")
        print("1.  Agregar Cliente")
        print("2. lsitar clientes")
        print("3. buscar cliente")
        print("4. eliminar cliente")
        print("5. Registrar Orden de Trabajo")
        print("6. ver ordenes de trabajo")
        print("7. Estadistiacas")
        print("8. ordenar clientes ")
        print("9. Salir")

        opcion = input("seleccione una opción: ")

        if opcion == "1":
            print("Agregar Cliente")

        elif opcion == "2":
            print("Listar Clientes")   

        elif opcion == "3":
            print("Buscar Cliente")

        elif opcion == "4":
            print("Eliminar Cliente")

        elif opcion == "5":
            print("Registrar Orden de Trabajo")

        elif opcion == "6":
            print("Ver Ordenes de Trabajo")

        elif opcion == "7":
            print("Estadisticas")

        elif opcion == "8":
            print("Ordenar Clientes")

        elif opcion == "9":
            print("Saliendo de NetControl ISP...")
            
