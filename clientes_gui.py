
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
 # Buscador grafico de clientes
        buscador = tk.Frame(ventana, bg="#F1F5F9")
        buscador.pack(fill="x", padx=25, pady=5)

        tk.Label(
            buscador,
            text="Buscar por codigo:",
            bg="#F1F5F9",
            font=("Arial", 10, "bold")
        ).pack(side="left", padx=5)

        self.entrada_buscar = tk.Entry(
            buscador,
            font=("Arial", 11),
            width=20
        )
        self.entrada_buscar.pack(side="left", padx=5)

        tk.Button(
            buscador,
            text="BUSCAR",
            command=self.buscar_cliente,
            bg="#2563EB",
            fg="white"
        ).pack(side="left", padx=5)

        tk.Button(
            buscador,
            text="MOSTRAR TODOS",
            command=self.actualizar_tabla,
            bg="#64748B",
            fg="white"
        ).pack(side="left", padx=5)

        tk.Button(
            ventana,
            text="ELIMINAR CLIENTE SELECCIONADO",
            command=self.eliminar_cliente,
            bg="#DC2626",
            fg="white",
            font=("Arial", 10, "bold"),
            width=32
        ).pack(pady=10)



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


    def buscar_cliente(self):
        codigo = self.entrada_buscar.get().strip()

        if not codigo:
            messagebox.showwarning(
                "Busqueda",
                "Ingrese un codigo para buscar."
            )
            return

        for cliente in self.clientes:
            if cliente["codigo"] == codigo:
                for fila in self.tabla.get_children():
                    self.tabla.delete(fila)

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

                messagebox.showinfo(
                    "Cliente encontrado",
                    f"Cliente: {cliente['nombre']}"
                )
                return

        messagebox.showwarning(
            "Sin resultados",
            "No existe un cliente con ese codigo."
        )   
        
    def eliminar_cliente(self):
        seleccion = self.tabla.selection()

        if not seleccion:
            messagebox.showwarning(
                "Seleccion requerida",
                "Seleccione un cliente de la tabla."
            )
            return

        valores = self.tabla.item(seleccion[0], "values")
        codigo = str(valores[0])

        cliente = next(
            (
                c for c in self.clientes
                if str(c["codigo"]) == codigo
            ),
            None
        )

        if cliente is None:
            messagebox.showerror(
                "Error",
                "No se encontro el cliente."
            )
            return

        confirmar = messagebox.askyesno(
            "Confirmar eliminacion",
            f"Desea eliminar al cliente {cliente['nombre']}?"
        )

        if not confirmar:
            return

        self.clientes.remove(cliente)
        self.actualizar_tabla()

        messagebox.showinfo(
            "Cliente eliminado",
            "El cliente fue eliminado correctamente."
        )


if __name__ == "__main__":
    clientes = []

    ventana = tk.Tk()
    ClientesGUI(ventana, clientes)
    ventana.mainloop()
