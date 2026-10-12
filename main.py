from clientes import agregar_cliente
clientes = []

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
            agregar_cliente(clientes)



        elif opcion == "2":
            print("Listar Clientes")   

            if len(clientes) == 0:
                print("No hay clientes registrados.")
            else:
                for cliente in clientes:
                    print(f"Código: {cliente['codigo']}, Nombre: {cliente['nombre']}, Dirección: {cliente['direccion']}, Plan: {cliente['plan']}, Precio: {cliente['precio']}, Estado: {cliente['estado']}")

        elif opcion == "3":
            print("Buscar Cliente")
            codigo_buscar = input("Ingrese el código del cliente a buscar: ")
            encontrado = False
            for cliente in clientes:
                if cliente["codigo"] == codigo_buscar:
                    encontrado = True
                    print("Cliente encontrado:")
                    print(f"Nombre: {cliente['nombre']}")
                    print(f"Dirección: {cliente['direccion']}")
                    print(f"Plan: {cliente['plan']}")
                    print(f"Precio: Q{cliente['precio']}")
                    print(f"Estado: {cliente['estado']}")
                    break

            if encontrado == False:
                print("No existe ningún cliente con ese código.")


        elif opcion == "4":
            print("Eliminar Cliente")
            codigo_eliminar = input("Ingrese el código del cliente a eliminar: ")
            encontrado = False

            for cliente in clientes:
                if cliente["codigo"] == codigo_eliminar:
                    encontrado = True
                    print(f"Cliente encontrado: {cliente['nombre']}")
                    break

            if encontrado == True:
                confirmar = input("¿Desea eliminar este cliente? (si/no): ").lower()

                if confirmar == "si":
                    clientes.remove(cliente)
                    print("Cliente eliminado correctamente.")
                else:
                    print("Eliminación cancelada.")
            else:
                print("No existe ningún cliente con ese código.")


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
        else:
            print("Opción inválida. Intente nuevamente .")  




