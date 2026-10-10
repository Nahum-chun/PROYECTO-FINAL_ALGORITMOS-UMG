# Módulo de ordenes y estadísticas

# datos de prueba para adaptar a los datos del compañero nahum, con esto emepezare a adaptar el codigo en base a el, luego lo borro.
clientes = [
    {"codigo": "1001", "nombre": "Juan Perez", "direccion": "Zona 1", "plan": "10 Mbps", "precio": 200.0, "estado": "activo"},
    {"codigo": "1002", "nombre": "Ana Gomez", "direccion": "Zona 10", "plan": "50 Mbps", "precio": 450.0, "estado": "activo"},
    {"codigo": "1003", "nombre": "Carlos Lopez", "direccion": "Zona 5", "plan": "20 Mbps", "precio": 300.0, "estado": "inactivo"}
]

ordenes = []

#Creacion de la funcion registrar orden de trabajo y validacion de codigo abonado...dificiiiilismo
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

#Creacion de funcion ver ordenes de trabjajo y el formato limpio
def Ver_ordenes():
    print("\n--- LISTADO DE ORDENES DE TRABAJO ---")
    if len(ordenes) == 0:
        print("No hay ordenes de trabajo registradas.")
    else:
        for orden in ordenes:
            print(f"Abonado: {orden[0]} | Falla: {orden[1]} | Tecnico: {orden[2]} | Estado: {orden[3]}")

def Mostrar_estadisticas():
    print("\n========= ESTADISTICAS DEL SISTEMA =========")
    
    if len(clientes) == 0:
        print("No hay clientes registrados en el sistema para calcular estadisticas.")
        return

    activos = 0
    suspendidos = 0
    ingreso_total = 0
    
    # recorrido para contar estados y acumular ingresos
    for cliente in clientes:
        if cliente[5] == "Activo":
            activos += 1
        elif cliente[5] == "Suspendido":
            suspendidos += 1
            
        ingreso_total += cliente[4]  # en la posicion 4 esta el precio del plan
        
    promedio_cliente = ingreso_total / len(clientes)

    print(f"Clientes registrados: {len(clientes)}")
    print(f"Clientes activos: {activos}")
    print(f"Clientes suspendidos: {suspendidos}")
    print(f"Ingreso mensual: Q{ingreso_total:.2f}")
    print(f"Promedio por cliente: Q{promedio_cliente:.2f}")

# prueba temporal. lo borrare al final
Registrar_orden()
Ver_ordenes()
Mostrar_estadisticas()