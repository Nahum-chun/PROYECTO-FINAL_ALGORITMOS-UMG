
from clientes import agregar_cliente, listar_clientes, buscar_cliente, eliminar_cliente
from Modulo_Ordenes import Registrar_orden, Ver_ordenes, Mostrar_estadisticas, ordenes
from Modulo_de_Interfaz_Grafica  import crear_interfaz

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
            Registrar_orden(clientes)

        elif opcion == "6":
            Ver_ordenes()

        elif opcion == "7":
            Mostrar_estadisticas(clientes)

        elif opcion == "8":
            crear_interfaz(clientes, ordenes)

        elif opcion == "9":
            print("\nSaliendo de NetControl ISP...")
            print("Gracias por utilizar nuestro sistema.")

        else:
            print("\nOpción inválida. Intente nuevamente.")
