# Modulo de Interfaz Grafica 
# Inregrante 3 Pedro Andres
import tkinter as tk
from tkinter import ttk, messagebox

try:
    from main_Módulo_de_Ordenamiento import ordenar_clientes_burbuja
except ImportError:
    # Función de respaldo si el archivo se ejecuta de forma independiente
    def ordenar_clientes_burbuja(lista):
        n = len(lista)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if lista[j]["precio"] > lista[j + 1]["precio"]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]

#Datos de prueba para la vista previa de la interfaz grafica

clientes_Prueba = [
    {"codigo": 1001, "nombre": "Carlos", "direccion": "Malacatan", "plan": "30 Mbps", "precio": 450, "estado" : "Activo"},
    {"codigo": 1012, "nombre": "Ana", "direccion" : "San Marcos", "plan" : "10 Mbps", "precio": 200, "estado": "Activo"},
    {"codigo": 1003, "nombre": "Andrea", "direccion": "Coatepeque", "plan": "20 Mbps", "precio": 300, "estado": "Activo"},
    {"codigo": 1004, "nombre": "Luis", "direccion": "Malacatán", "plan": "50 Mbps", "precio": 600, "estado": "Activo"}
]

def crear_interfaz(clientes=None, ordenes=None):
    if clientes is None:
        clientes = clientes_Prueba
    if ordenes is None:
        ordenes = []

    ventana = tk.Tk()
    ventana.title("NetControl ISP - PANEL DE CONTROL")
    ventana.geometry("650x450")
    ventana.config(bg="#f0f0f0")

    #Encabezado
    header = tk.Frame(ventana, bg="#1e293b")
    header.pack(fill=tk.X)

    lbl_titulo = tk.Label(header, text="NETCONTROL ISP", font=("Helvetica", 16, "bold"), fg="white", bg="#1e293b")
    lbl_titulo.pack(side="left", padx=15, pady=10)

    #Contenedor Principal
    main_frame = tk.Frame(ventana, bg="#f0f2f5")
    main_frame.pack(fill="both", expand=True, padx=20, pady=15)

    #Calculo dinamico de totales e ingresos 
    total_clientes = len(clientes)
    total_ordenes = len(ordenes)
    total_ingresos = sum(c["precio"] for c in clientes) if clientes else 0

    #Tarjetas de Resumen 
    cards_frame = tk.Frame(main_frame, bg="#f0f2f5")
    cards_frame.pack(fill="x", pady=10 )

    lbl_c1 = tk.Label(cards_frame, text=f"👤 Clientes: {total_clientes}", font=("Helvetica", 10, "bold"), bg="#ffffff", relief="solid", bd=1)
    lbl_c1.pack(side="left", expand=True, fill="x", padx=5, ipadx=10, ipady=8 )

    lbl_c2 = tk.Label(cards_frame, text=f"📋 Órdenes: {total_ordenes}", font=("Helvetica", 10, "bold"), bg="#ffffff", relief="solid", bd=1)
    lbl_c2.pack(side="left", expand=True, fill="x", padx=5, ipadx=10, ipady=8)

    lbl_c3 = tk.Label(cards_frame, text=f"💰 Ingresos: Q{total_ingresos:,}", font=("Helvetica", 10, "bold"), bg="#ffffff", relief="solid", bd=1)
    lbl_c3.pack(side="left", expand=True, fill="x", padx=5, ipadx=10, ipady=8)

    #Tabla de Clientes 
    tabla_frame = tk.Frame(main_frame, bg="#ffffff", relief="solid", bd=1)
    tabla_frame.pack(fill="both", expand=True, pady=10)

    columnas = ("codigo", "nombre", "plan", "precio", "estado")
    tabla = ttk.Treeview(tabla_frame, columns=columnas, show="headings", height=6)

    tabla.heading("codigo", text="Código")
    tabla.heading("nombre", text="Nombre")
    tabla.heading("plan", text="Plan")
    tabla.heading("precio", text="Precio")
    tabla.heading("estado", text="Estado")

    tabla.column("codigo", width=80, anchor="center")
    tabla.column("nombre", width=150, anchor="w")
    tabla.column("plan", width=100, anchor="center")
    tabla.column("precio", width=100, anchor="center")
    tabla.column("estado", width=100, anchor="center")

    def cargar_datos_tabla(lista_datos):
        for fila in tabla.get_children():
            tabla.delete(fila)
        for c in lista_datos:
            precio_fmt = f"Q{c['precio']:.2f}" if isinstance(c['precio'], (int, float)) else str(c['precio'])
            tabla.insert("", "end", values=(c["codigo"], c["nombre"], c["plan"], precio_fmt, c["estado"]))

    # cargar inicial con los datos recibidos 
    cargar_datos_tabla(clientes)

    tabla.pack(fill="both", expand=True, padx=5, pady=5)

    # Botón de Acción
    def ejecutar_ordenamiento():
        clientes_ordenados = clientes.copy()
        ordenar_clientes_burbuja(clientes_ordenados)
        cargar_datos_tabla(clientes_ordenados)
        messagebox.showinfo("Algoritmo", "Clientes ordenados por precio exitosamente (Menor a Mayor).")

    btn_frame = tk.Frame(main_frame, bg="#f0f2f5")
    btn_frame.pack(fill="x", pady=5)

    btn_ordenar = tk.Button(
        btn_frame, 
        text="🔄 Ordenar por Precio (Burbuja)", 
        bg="#2563eb", 
        fg="white", 
        font=("Helvetica", 10, "bold"), 
        command=ejecutar_ordenamiento
    )
    btn_ordenar.pack(side="right", padx=5)

    ventana.mainloop()

if __name__ == "__main__":
    crear_interfaz(clientes_Prueba, [])

