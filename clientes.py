def agregar_cliente(clientes):
    print("Agregar cliente")

    codigo = input("Código del cliente: ").strip()

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
        return

    nombre = input("Nombre del cliente: ").strip()

    while nombre == "":
        print("El nombre del cliente no puede estar vacío.")
        nombre = input("Ingrese el nombre del cliente: ").strip()

    direccion = input("Dirección: ").strip()

    while direccion == "":
        print("La dirección del cliente no puede estar vacía.")
        direccion = input("Ingrese la dirección del cliente: ").strip()

    plan = input("Plan contratado: ").strip()

    while plan == "":
        print("El plan contratado no puede estar vacío.")
        plan = input("Ingrese el plan contratado: ").strip()

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