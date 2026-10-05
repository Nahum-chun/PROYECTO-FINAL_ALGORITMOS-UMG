# Listas de prueba temporales
clientes = [
    [1001, "Juan Pérez", "Malacatán", "30 Mbps", 300, "Activo"],
    [1002, "María López", "San Marcos", "10 Mbps", 200, "Suspendido"],
    [1003, "Carlos Gómez", "Tecún Umán", "50 Mbps", 450, "Activo"]
]

ordenes = [
    [1001, "Sin internet", "Carlos", "Pendiente"],
    [1002, "Lentitud", "Ana", "Finalizada"]
]

# Aquí cree la función para registrar ordenes de trabajo.
def Registrar_orden():
    print("\n--- REGISTRAR ORDEN DE TRABAJO ---")
    
    # 1. Aqui pedi los datos de la orden al usuario.
    codigo = int(input("Ingrese código de abonado: "))
    falla = input("Ingrese tipo de falla: ")
    tecnico = input("Ingrese técnico asignado: ")
    
    # 2. Aqui cree la nueva lista de la orden con los datos ingresados y el estado inicial
    nueva_orden = [codigo, falla, tecnico, "Pendiente"]
    
    # 3. Esto es para guardar en la lista de ordenes la nueva orden creada.
    ordenes.append(nueva_orden)
    
    print("Orden registrada con éxito")

# Llamamos a la función para que se ejecute
Registrar_orden()

print("Lista de ordenes actualizada:", ordenes)


#Esto es para hacer las listas y poder verlas.
def Ver_ordenes():
    print("\n--- LISTADO DE ÓRDENES DE TRABAJO ---")
    
    if len(ordenes) == 0:
        print("No hay órdenes registradas.")
    else:
        for orden in ordenes:
            print(f"Abonado: {orden[0]} | Falla: {orden[1]} | Técnico: {orden[2]} | Estado: {orden[3]}")

# Módulo de estadísticas (Opción 7)
def Mostrar_estadisticas():
    print("\n========= ESTADÍSTICAS DEL SISTEMA =========")
    
    activos = 0
    suspendidos = 0
    ingreso_total = 0
    
    # Iniciamos con el primer cliente de la lista
    plan_mas_barato = clientes[0] if len(clientes) > 0 else None
    plan_mas_caro = clientes[0] if len(clientes) > 0 else None
    
    for cliente in clientes:
        if cliente[5] == "Activo":
            activos += 1
        elif cliente[5] == "Suspendido":
            suspendidos += 1
            
        ingreso_total += cliente[4]
        
        # Comparamos precios para encontrar el mínimo y el máximo
        if cliente[4] < plan_mas_barato[4]:
            plan_mas_barato = cliente
        if cliente[4] > plan_mas_caro[4]:
            plan_mas_caro = cliente
            
    promedio_cliente = ingreso_total / len(clientes) if len(clientes) > 0 else 0
            
    print(f"Clientes registrados: {len(clientes)}")
    print(f"Clientes activos: {activos}")
    print(f"Clientes suspendidos: {suspendidos}")
    print(f"Ingreso mensual: Q{ingreso_total:.2f}")
    print(f"Promedio por cliente: Q{promedio_cliente:.2f}")
    
    if plan_mas_barato and plan_mas_caro:
        print(f"Plan más barato: {plan_mas_barato[3]} (Q{plan_mas_barato[4]:.2f})")
        print(f"Plan más caro: {plan_mas_caro[3]} (Q{plan_mas_caro[4]:.2f})")

# Para probar la función
Mostrar_estadisticas()