# Módulo de ordenes y estadísticas

# Datos de prueba temporales para la lista de clientes y ordenes. lo debo borrar al final.
clientes = [
    [1001, "Juan Perez", "12345678", "10 Mbps", 200.0, "Activo"],
    [1002, "Ana Gomez", "87654321", "50 Mbps", 450.0, "Activo"],
    [1003, "Carlos Lopez", "11223344", "20 Mbps", 300.0, "Suspendido"]
]

ordenes = []


def Registrar_orden():
    print("\n--- REGISTRAR ORDEN DE TRABAJO ---")
    
    cliente_encontrado = False
    
    while not cliente_encontrado:
        entrada = input("Ingrese codigo de abonado: ")
        
        if entrada.isdigit():
            codigo = int(entrada)
            
            for cliente in clientes:
                if cliente[0] == codigo:
                    cliente_encontrado = True
                    break
            
            if not cliente_encontrado:
                print("Error: El codigo de abonado no existe en la lista de clientes.")
        else:
            print("Error: Debe ingresar un numero entero valido.")

    falla = input("Ingrese tipo de falla: ")
    tecnico = input("Ingrese tecnico asignado: ")
    
    nueva_orden = [codigo, falla, tecnico, "Pendiente"]
    ordenes.append(nueva_orden)
    print("Orden registrada con exito.")

def Ver_ordenes():
    print("\n--- LISTADO DE ORDENES DE TRABAJO ---")
    if len(ordenes) == 0:
        print("No hay ordenes de trabajo registradas.")
    else:
        for orden in ordenes:
            print(f"Abonado: {orden[0]} | Falla: {orden[1]} | Tecnico: {orden[2]} | Estado: {orden[3]}")

# prueba temporal. lo borrare al final
Registrar_orden()
Ver_ordenes()