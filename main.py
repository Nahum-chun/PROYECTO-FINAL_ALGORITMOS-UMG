
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
            print("Agregar Cliente")
            codigo = input("código del cliente: ").strip()
            while codigo == "":
                print("El código del cliente no puede estar vacío.")
                codigo = input("Ingrese el código del cliente: ").strip()

            codigo_repetido = False

            for cliente in clientes:
                if cliente["codigo"] == codigo:
                    codigo_repetido = True
                    break

            if codigo_repetido:
                print("El código del cliente ya existe.")
                continue

            nombre = input(".nombre del cliente: ").strip()

            while nombre == "":
                print("El nombre del cliente no puede estar vacío.")
                nombre = input("Ingrese el nombre del cliente: ").strip()
            direccion = input("direccion: ").strip()
            while direccion == "":
                print("La dirección del cliente no puede estar vacía.")
                direccion = input("Ingrese la dirección del cliente: ").strip()
            plan = input("Plan contratado: ")
            while plan == "":
                print("El plan contratado no puede estar vacío.")
                plan = input("Ingrese el plan contratado: ")


            
            while True:
                entrada_precio = input("Precio del plan: ").strip()

                try:
                    precio = float(entrada_precio)

                    if precio > 0:
                        break
                    else:
                        print("El precio debe ser mayor que cero.")

                except ValueError:
                    print("Ingrese un precio numérico válido.")
                
            estado = input("Estado del cliente (activo/inactivo): ").strip().lower()

            while estado not in ["activo", "inactivo"]:
                print("Error: El estado debe ser activo o inactivo.")
                estado = input("Ingrese el estado del cliente: ").strip().lower()

            cliente = {
                "codigo": codigo,
                "nombre": nombre,
                "direccion": direccion,
                "plan": plan,
                "precio": precio,
                "estado": estado
            }

            clientes.append(cliente)
            print("Cliente agregado correctamente.")
 



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




