# Módulo de Ordenamiento (Integrante 3 Pedro Andres)

# DATOS DE PRUEBA
clientes = [
    {"codigo": 1001, "nombre": "Carlos", "direccion": "Malacatan", "plan": "30 Mbps", "precio": 450, "estado" : "Activo"},
    {"codigo": 1012, "nombre": "Ana", "direccion" : "San Marcos", "plan" : "10 Mbps", "precio": 200, "estado": "Activo"},
    {"codigo": 1003, "nombre": "Andrea", "direccion": "Coatepeque", "plan": "20 Mbps", "precio": 300, "estado": "Activo"},
    {"codigo": 1004, "nombre": "Luis", "direccion": "Malacatán", "plan": "50 Mbps", "precio": 600, "estado": "Activo"}
]

# Funcion 1: Mostrar Tablas de Clientes 

def mostrar_clientes(lista):
    """Muestra la lista de clientes en un formato de tabla"""
    print(f"{'CODIGO':<8} {'NOMBRE':<12} {'PLAN':<10} {'PRECIO':<10} {'ESTADO':<8}")
    print("-" * 50)
    for c in lista:
        print(f"{c['codigo']:<8} {c['nombre']:<12} {c['plan']:<10} Q{c['precio']:<9.2f} {c['estado']:<8}")
        print("-" * 50)

# Funcion 2: Algoritmo de ordenamiento burbuja (BUBBLE SORT)
# Ordena manualmente de menor a mayor por el precio del plan contratado

def ordenar_clientes_burbuja(lista):
    """ Ordena la lista de clientes según el precio del plande menor a mayor utilizando el Algoritmo Burbuja."""
    n = len(lista)
    #Reccorido por todos los elementos 
    for i in range(n):
        # Ultimos i elementos ya estan ordenados
        for j in range (0, n-i-1):
            # comparamos el precio del cliente actual con el siguiente
            if lista[j]["precio"] > lista[j + 1]["precio"]:
                #Intercambio manula
                temp = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = temp

#3. Explicación del Algoritmo Burbuja

#Ciclo exterior (for i in range(n - 1)): Define cuántas pasadas completas haremos sobre la lista.

#Ciclo interior (for j in range(0, n - i - 1)): Compara vecinos adyacentes uno a uno.

#Condición (if lista[j]["precio"] > lista[j + 1]["precio"]): Si el precio del cliente de la izquierda es mayor que el de la derecha, los intercambiamos.

#Intercambio (Swap): Usamos una variable temporal temp para cambiar las posiciones sin perder datos.


# PRUEBA Y EJECUCIÓN DEL MÓDULO

if __name__ == "__main__":
    print("          DEMOSTRACIÓN DE ORDENAMIENTO BURBUJA           ")

    print("--- ESTADO INICIAL DE CLIENTES (DESORDENADO) ---")
    mostrar_clientes(clientes)

    print("\nEjecutando algoritmo de ordenamiento por precio...")
    ordenar_clientes_burbuja(clientes)

    print("\n--- ESTADO FINAL DE CLIENTES (ORDENADO POR PRECIO) ---")
    mostrar_clientes(clientes)
