
from clientes import agregar_cliente, listar_clientes, buscar_cliente, eliminar_cliente

# Lista compartida de clientes
clientes = []

# Inicio de sesión
intentos = 3
acceso = False

while intentos > 0:

    usuario = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")

    if usuario == "pepe" and contraseña == "5555":
        print("\nAcceso correcto. Bienvenido a NetControl ISP.")
        acceso = True
        break

    else:
        intentos -= 1
        print(f"Acceso incorrecto. Le quedan {intentos} intentos.")

if intentos == 0:
    print("Se ha bloqueado el acceso. Intente más tarde.")


# Menú principal
if acceso == True:

    opcion = ""

    while opcion != "9":

        print("\n========== NETCONTROL ISP ==========")
        print("1. Agregar cliente")
        print("2. Listar clientes")
        print("3. Buscar cliente")
        print("4. Eliminar cliente")
        print("5. Registrar orden de trabajo")
        print("6. Ver órdenes de trabajo")
        print("7. Estadísticas")
        print("8. Ordenar clientes")
        print("9. Salir")
        print("====================================")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            agregar_cliente(clientes)

        elif opcion == "2":
            listar_clientes(clientes)

        elif opcion == "3":
            buscar_cliente(clientes)

        elif opcion == "4":
            eliminar_cliente(clientes)

        elif opcion == "5":
            print("\nRegistrar orden de trabajo")
            print("Módulo pendiente de integración.")

        elif opcion == "6":
            print("\nVer órdenes de trabajo")
            print("Módulo pendiente de integración.")

        elif opcion == "7":
            print("\nEstadísticas")
            print("Módulo pendiente de integración.")

        elif opcion == "8":
            print("\nOrdenar clientes")
            print("Módulo pendiente de integración.")

        elif opcion == "9":
            print("\nSaliendo de NetControl ISP...")
            print("Gracias por utilizar nuestro sistema.")

        else:
            print("\nOpción inválida. Intente nuevamente.")
