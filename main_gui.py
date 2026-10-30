
import tkinter as tk
from tkinter import messagebox

from clientes_gui import ClientesGUI
from ordenes_gui import OrdenesGUI
from estadisticas_gui import EstadisticasGUI


# ==========================================
# NETCONTROL ISP - CONFIGURACION
# ==========================================

USUARIO = "pepe"
CONTRASENA = "5555"
MAX_INTENTOS = 3

intentos = 0

# Lista compartida entre los modulos graficos
clientes = []


# ==========================================
# CONTROL DE VENTANAS
# ==========================================

def abrir_modulo(panel, titulo, clase_modulo):

    # Si la ventana ya existe, traerla al frente
    for ventana in panel.winfo_children():
        if isinstance(ventana, tk.Toplevel):
            if ventana.title() == titulo:
                ventana.deiconify()
                ventana.lift()
                ventana.focus_force()
                return

    # Crear una nueva ventana secundaria
    ventana = tk.Toplevel(panel)
    ventana.title(titulo)
    ventana.geometry("1100x700")

    try:
        clase_modulo(ventana, clientes)
    except Exception:
        ventana.destroy()
        raise

    ventana.lift()


def abrir_clientes(panel):
    abrir_modulo(
        panel,
        "NETCONTROL ISP - Clientes",
        ClientesGUI
    )


def abrir_ordenes(panel):
    abrir_modulo(
        panel,
        "NETCONTROL ISP - Ordenes",
        OrdenesGUI
    )


# ==========================================
# PANEL PRINCIPAL
# ==========================================

def abrir_panel():

    login.withdraw()

    panel = tk.Toplevel(login)
    panel.title("NETCONTROL ISP - Panel Principal")
    panel.geometry("900x600")
    panel.configure(bg="#F1F5F9")

    # Cerrar todo el sistema al salir del panel
    panel.protocol("WM_DELETE_WINDOW", login.destroy)

    tk.Label(
        panel,
        text="NETCONTROL ISP",
        font=("Arial", 26, "bold"),
        bg="#F1F5F9",
        fg="#123B65"
    ).pack(pady=(35, 10))

    tk.Label(
        panel,
        text="Sistema de Administracion de Clientes y Ordenes",
        font=("Arial", 13),
        bg="#F1F5F9",
        fg="#475569"
    ).pack(pady=(0, 25))

    tk.Label(
        panel,
        text="Bienvenido al panel principal",
        font=("Arial", 16, "bold"),
        bg="#F1F5F9",
        fg="#123B65"
    ).pack(pady=15)

    # Boton del modulo de Andres
    tk.Button(
        panel,
        text="GESTION DE CLIENTES",
        command=lambda: abrir_clientes(panel),
        font=("Arial", 13, "bold"),
        bg="#2563EB",
        fg="white",
        width=28,
        height=2,
        cursor="hand2"
    ).pack(pady=10)

    # Boton del modulo de Jose
    tk.Button(
        panel,
        text="ORDENES DE TRABAJO",
        command=lambda: abrir_ordenes(panel),
        font=("Arial", 13, "bold"),
        bg="#0F766E",
        fg="white",
        width=28,
        height=2,
        cursor="hand2"
    ).pack(pady=10)

    # Boton para salir del sistema
    tk.Button(
        panel,
        text="SALIR DEL SISTEMA",
        command=login.destroy,
        font=("Arial", 12, "bold"),
        bg="#DC2626",
        fg="white",
        width=28,
        height=2,
        cursor="hand2"
    ).pack(pady=25)

    panel.lift()
    panel.focus_force()


# ==========================================
# INICIO DE SESION
# ==========================================

def iniciar_sesion():
    global intentos

    usuario = entrada_usuario.get().strip()
    contrasena = entrada_contrasena.get()

    if usuario == USUARIO and contrasena == CONTRASENA:
        abrir_panel()
        return

    intentos += 1
    restantes = MAX_INTENTOS - intentos

    if restantes > 0:
        messagebox.showwarning(
            "Acceso incorrecto",
            f"Credenciales incorrectas. Intentos restantes: {restantes}"
        )
        entrada_contrasena.delete(0, tk.END)

    else:
        messagebox.showerror(
            "Acceso bloqueado",
            "Se agotaron los tres intentos."
        )
        login.destroy()


# ==========================================
# VENTANA DE LOGIN
# ==========================================

login = tk.Tk()
login.title("NETCONTROL ISP - Inicio de Sesion")
login.geometry("430x420")
login.resizable(False, False)
login.configure(bg="#123B65")

tk.Label(
    login,
    text="NETCONTROL ISP",
    font=("Arial", 24, "bold"),
    bg="#123B65",
    fg="white"
).pack(pady=(45, 10))

tk.Label(
    login,
    text="Acceso al sistema",
    font=("Arial", 12),
    bg="#123B65",
    fg="#CBD5E1"
).pack(pady=(0, 30))

tk.Label(
    login,
    text="Usuario",
    bg="#123B65",
    fg="white"
).pack()

entrada_usuario = tk.Entry(
    login,
    font=("Arial", 13),
    width=27
)
entrada_usuario.pack(pady=8)

tk.Label(
    login,
    text="Contrasena",
    bg="#123B65",
    fg="white"
).pack()

entrada_contrasena = tk.Entry(
    login,
    font=("Arial", 13),
    width=27,
    show="*"
)
entrada_contrasena.pack(pady=8)

tk.Button(
    login,
    text="INICIAR SESION",
    command=iniciar_sesion,
    font=("Arial", 12, "bold"),
    bg="#22C55E",
    fg="white",
    width=22,
    cursor="hand2"
).pack(pady=25)

login.bind("<Return>", lambda evento: iniciar_sesion())

entrada_usuario.focus_set()

# Un unico ciclo principal de Tkinter
login.mainloop()
