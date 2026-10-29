
import tkinter as tk
from tkinter import ttk, messagebox


class ClientesGUI:
    def __init__(self, ventana, clientes):
        self.ventana = ventana
        self.clientes = clientes

        self.ventana.title("NETCONTROL ISP - Clientes")
        self.ventana.geometry("950x620")
        self.ventana.configure(bg="#F1F5F9")

        titulo = tk.Label(
            ventana,
            text="GESTION DE CLIENTES",
            font=("Arial", 22, "bold"),
            bg="#F1F5F9",
            fg="#123B65"
        )
        titulo.pack(pady=20)

        formulario = tk.LabelFrame(
            ventana,
            text="Registrar nuevo cliente",
            font=("Arial", 11, "bold"),
            bg="#F1F5F9",
            padx=15,
            pady=15
        )
        formulario.pack(fill="x", padx=25, pady=10)

        self.campos = {}

        etiquetas = [
            ("codigo", "Codigo"),
            ("nombre", "Nombre"),
            ("direccion", "Direccion"),
            ("plan", "Plan contratado"),
            ("precio", "Precio del plan")
        ]

        for fila, (clave, texto) in enumerate(etiquetas):
            tk.Label(
                formulario,
                text=texto,
                bg="#F1F5F9"
            ).grid(row=fila, column=0, sticky="w", pady=5)

            entrada = tk.Entry(formulario, width=45)
            entrada.grid(row=fila, column=1, padx=10, pady=5)

            self.campos[clave] = entrada

        tk.Label(
            formulario,
            text="Estado",
            bg="#F1F5F9"
        ).grid(row=5, column=0, sticky="w")

        self.estado = ttk.Combobox(
            formulario,
            values=["activo", "inactivo"],
            state="readonly",
            width=42
        )
        self.estado.grid(row=5, column=1, padx=10, pady=5)
        self.estado.set("activo")

        tk.Button(
            formulario,
            text="GUARDAR CLIENTE",
            command=self.agregar_cliente,
            bg="#16A34A",
            fg="white",
            font=("Arial", 10, "bold"),
            width=22
        ).grid(row=6, column=1, pady=15)

        columnas = (
            "codigo", "nombre", "direccion",
            "plan", "precio", "estado"
        )

        contenedor = tk.Frame(ventana)
        contenedor.pack(fill="both", expand=True, padx=25, pady=10)

        self.tabla = ttk.Treeview(
            contenedor,
            columns=columnas,
            show="headings"
        )

        encabezados = {
            "codigo": "Codigo",
            "nombre": "Nombre",
            "direccion": "Direccion",
            "plan": "Plan",
            "precio": "Precio",
            "estado": "Estado"
        }

        for columna in columnas:
            self.tabla.heading(
                columna,
                text=encabezados[columna]
            )
            self.tabla.column(columna, width=140)

        barra = ttk.Scrollbar(
            contenedor,
            orient="vertical",
            command=self.tabla.yview
        )
        self.tabla.configure(yscrollcommand=barra.set)

        self.tabla.pack(side="left", fill="both", expand=True)
        barra.pack(side="right", fill="y")

        self.actualizar_tabla()

    def agregar_cliente(self):
        datos = {
            clave: entrada.get().strip()
            for clave, entrada in self.campos.items()
        }

        if any(valor == "" for valor in datos.values()):
            messagebox.showwarning(
                "Datos incompletos",
                "Todos los campos son obligatorios."
            )
            return

        if any(
            cliente["codigo"] == datos["codigo"]
            for cliente in self.clientes
        ):
            messagebox.showwarning(
                "Codigo duplicado",
                "Ya existe un cliente con ese codigo."
            )
            return

        try:
            precio = float(datos["precio"])
        except ValueError:
            messagebox.showerror(
                "Precio incorrecto",
                "Ingrese un precio numerico valido."
            )
            return

        if precio <= 0:
            messagebox.showerror(
                "Precio incorrecto",
                "El precio debe ser mayor que cero."
            )
            return

        cliente = {
            "codigo": datos["codigo"],
            "nombre": datos["nombre"],
            "direccion": datos["direccion"],
            "plan": datos["plan"],
            "precio": precio,
            "estado": self.estado.get()
        }

        self.clientes.append(cliente)

        self.actualizar_tabla()

        for entrada in self.campos.values():
            entrada.delete(0, tk.END)

        self.estado.set("activo")

        messagebox.showinfo(
            "Registro exitoso",
            "Cliente agregado correctamente."
        )

    def actualizar_tabla(self):
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)

        for cliente in self.clientes:
            self.tabla.insert(
                "",
                "end",
                values=(
                    cliente["codigo"],
                    cliente["nombre"],
                    cliente["direccion"],
                    cliente["plan"],
                    f"Q{cliente['precio']:.2f}",
                    cliente["estado"]
                )
            )


if __name__ == "__main__":
    clientes = []

    ventana = tk.Tk()
    ClientesGUI(ventana, clientes)
    ventana.mainloop()
