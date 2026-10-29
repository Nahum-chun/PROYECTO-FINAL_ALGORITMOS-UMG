
import tkinter as tk
from tkinter import messagebox


USUARIO = "pepe"
CONTRASENA = "5555"
MAX_INTENTOS = 3

intentos = 0


def abrir_panel():
    login.destroy()

    panel = tk.Tk()
    panel.title("NETCONTROL ISP - Panel Principal")
    panel.geometry("900x550")
    panel.configure(bg="#F1F5F9")

    titulo = tk.Label(
        panel,
        text="NETCONTROL ISP",
        font=("Arial", 26, "bold"),
        bg="#F1F5F9",
        fg="#123B65"
    )
    titulo.pack(pady=35)

    subtitulo = tk.Label(
        panel,
        text="Sistema de Administracion de Clientes y Ordenes",
        font=("Arial", 13),
        bg="#F1F5F9"
    )
    subtitulo.pack()

    tk.Label(
        panel,
        text="Bienvenido al panel principal",
        font=("Arial", 16),
        bg="#F1F5F9"
    ).pack(pady=60)

    panel.mainloop()


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

entrada_usuario = tk.Entry(login, font=("Arial", 13), width=27)
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

login.mainloop()
