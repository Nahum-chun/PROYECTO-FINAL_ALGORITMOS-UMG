# Modulo de Interfaz Grafica 
# Inregrante 3 Pedro Andres
import tkinter as tk
from tkinter import ttk, messagebox

#Datos de prueba para la vista previa de la interfaz grafica

clientes_Prueba = [
    {"codigo": 1001, "nombre": "Carlos", "direccion": "Malacatan", "plan": "30 Mbps", "precio": 450, "estado" : "Activo"},
    {"codigo": 1012, "nombre": "Ana", "direccion" : "San Marcos", "plan" : "10 Mbps", "precio": 200, "estado": "Activo"},
    {"codigo": 1003, "nombre": "Andrea", "direccion": "Coatepeque", "plan": "20 Mbps", "precio": 300, "estado": "Activo"},
    {"codigo": 1004, "nombre": "Luis", "direccion": "Malacatán", "plan": "50 Mbps", "precio": 600, "estado": "Activo"}
]

def crear_interfaz():
    ventana = tk.Tk()
    ventana.title("NetControl ISP - PANEL DE CONTROL")
    ventana.geometry("650x450")
    ventana.config(bg="#f0f0f0")

    #Encabezado
    header = tk.Frame(ventana, bg="#1e293b")
    header.pack(fill=tk.X)

lbl_titulo = tk.Label(header, text="NETCONTROL ISP", font=("Helvetica", 16, "bold"), fg="white", bg="#1e293b")

