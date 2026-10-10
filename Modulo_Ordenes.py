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
    """Solicita y valida los datos para crear una nueva orden de trabajo."""
    print("\n--- REGISTRAR ORDEN DE TRABAJO ---")
    
    cliente_encontrado = False
    
    while not cliente_encontrado:
        entrada = input("Ingrese codigo de abonado: ").strip()
        
        if entrada.isdigit():
            codigo = entrada
            
            for cliente in clientes:
                if cliente["codigo"] == codigo:
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
    """Despliega la lista de todas las ordenes de trabajo registradas."""
    print("\n--- LISTADO DE ORDENES DE TRABAJO ---")
    if len(ordenes) == 0:
        print("No hay ordenes de trabajo registradas.")
    else:
        for orden in ordenes:
            print(f"Abonado: {orden[0]} | Falla: {orden[1]} | Tecnico: {orden[2]} | Estado: {orden[3]}")


def Mostrar_estadisticas():
    """Calcula y muestra resumenes financieros, de clientes y de ordenes del sistema."""
    print("\n========= ESTADISTICAS DEL SISTEMA =========")
    
    if len(clientes) == 0:
        print("No hay clientes registrados en el sistema para calcular estadisticas.")
        return

    activos = 0
    inactivos = 0
    ingreso_total = 0.0
    
    plan_mas_barato = clientes[0]
    plan_mas_caro = clientes[0]
    
    for cliente in clientes:
        if cliente["estado"] == "activo":
            activos += 1
        elif cliente["estado"] == "inactivo":
            inactivos += 1
            
        ingreso_total += cliente["precio"]
        
        if cliente["precio"] < plan_mas_barato["precio"]:
            plan_mas_barato = cliente
        if cliente["precio"] > plan_mas_caro["precio"]:
            plan_mas_caro = cliente
            
    promedio_cliente = ingreso_total / len(clientes)

    ordenes_pendientes = 0
    ordenes_finalizadas = 0
    
    for orden in ordenes:
        if orden[3] == "Pendiente":
            ordenes_pendientes += 1
        elif orden[3] == "Finalizada":
            ordenes_finalizadas += 1

    print(f"Clientes registrados: {len(clientes)}")
    print(f"Clientes activos: {activos}")
    print(f"Clientes inactivos: {inactivos}")
    print(f"Ingreso mensual: Q{ingreso_total:.2f}")
    print(f"Promedio por cliente: Q{promedio_cliente:.2f}")
    print(f"Plan mas barato: {plan_mas_barato['plan']} (Q{plan_mas_barato['precio']:.2f})")
    print(f"Plan mas caro: {plan_mas_caro['plan']} (Q{plan_mas_caro['precio']:.2f})")
    print(f"Ordenes pendientes: {ordenes_pendientes}")
    print(f"Ordenes finalizadas: {ordenes_finalizadas}")
# prueba temporal. lo borrare al final
Registrar_orden()
Ver_ordenes()
Mostrar_estadisticas()