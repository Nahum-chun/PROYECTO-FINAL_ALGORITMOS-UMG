
import tkinter as tk
from tkinter import ttk, messagebox

from Modulo_Ordenes import ordenes


class OrdenesGUI:

    def __init__(self, ventana, clientes):
        self.ventana = ventana
        self.clientes = clientes

        ventana.title("NETCONTROL ISP - Ordenes de trabajo")
        ventana.geometry("850x550")
        ventana.configure(bg="#eef2f7")

        titulo = tk.Label(
            ventana,
            text="GESTION DE ORDENES DE TRABAJO",
            font=("Arial", 17, "bold"),
            bg="#eef2f7"
        )
        titulo.pack(pady=20)

        formulario = tk.Frame(ventana, bg="#eef2f7")
        formulario.pack(pady=10)

        etiquetas = [
            "Codigo de abonado",
            "Tipo de falla",
            "Tecnico asignado"
        ]

        self.campos = {}

        for fila, etiqueta in enumerate(etiquetas):
            tk.Label(
                formulario,
                text=etiqueta,
                bg="#eef2f7"
            ).grid(row=fila, column=0, padx=10, pady=8, sticky="w")

            entrada = tk.Entry(formulario, width=35)
            entrada.grid(row=fila, column=1, padx=10, pady=8)

            self.campos[etiqueta] = entrada

        tk.Button(
            ventana,
            text="REGISTRAR ORDEN",
            command=self.registrar_orden,
            bg="#1769aa",
            fg="white",
            font=("Arial", 11, "bold"),
            padx=20,
            pady=8
        ).pack(pady=15)

        contenedor = tk.Frame(ventana)
        contenedor.pack(fill="both", expand=True, padx=25, pady=10)

        columnas = ("codigo", "falla", "tecnico", "estado")

        self.tabla = ttk.Treeview(
            contenedor,
            columns=columnas,
            show="headings"
        )

        encabezados = {
            "codigo": "Abonado",
            "falla": "Falla reportada",
            "tecnico": "Tecnico",
            "estado": "Estado"
        }

        for columna in columnas:
            self.tabla.heading(
                columna,
                text=encabezados[columna]
            )
            self.tabla.column(columna, width=160)

        self.tabla.pack(fill="both", expand=True)
        tk.Button(
            ventana,
            text="FINALIZAR ORDEN SELECCIONADA",
            command=self.finalizar_orden,
            bg="#198754",
            fg="white",
            font=("Arial", 11, "bold"),
            padx=20,
            pady=8
        ).pack(pady=10)

        self.actualizar_tabla()

    def registrar_orden(self):
        codigo = self.campos["Codigo de abonado"].get().strip()
        falla = self.campos["Tipo de falla"].get().strip()
        tecnico = self.campos["Tecnico asignado"].get().strip()

        if not codigo or not falla or not tecnico:
            messagebox.showwarning(
                "Datos incompletos",
                "Debe completar todos los campos."
            )
            return

        cliente_existe = any(
            str(cliente["codigo"]) == codigo
            for cliente in self.clientes
        )

        if not cliente_existe:
            messagebox.showerror(
                "Abonado no encontrado",
                "El codigo de abonado no existe."
            )
            return

        nueva_orden = [
            codigo,
            falla,
            tecnico,
            "Pendiente"
        ]

        ordenes.append(nueva_orden)

        self.actualizar_tabla()

        for entrada in self.campos.values():
            entrada.delete(0, tk.END)

        messagebox.showinfo(
            "Registro exitoso",
            "La orden fue registrada correctamente."
        )
    def actualizar_tabla(self):
        for elemento in self.tabla.get_children():
            self.tabla.delete(elemento)

        for indice, orden in enumerate(ordenes):
            self.tabla.insert(
                "",
                tk.END,
                iid=str(indice),
                values=orden
            )


    def finalizar_orden(self):
        seleccion = self.tabla.selection()

        if not seleccion:
            messagebox.showwarning(
                "Sin seleccion",
                "Seleccione una orden de la tabla."
            )
            return

        # Buscar la orden seleccionada mediante su identificador
        indice = int(seleccion[0])

        if ordenes[indice][3] == "Finalizada":
            messagebox.showinfo(
                "Orden finalizada",
                "Esta orden ya fue finalizada."
            )
            return

        confirmar = messagebox.askyesno(
            "Confirmar finalizacion",
            "Desea marcar esta orden como finalizada?"
        )

        if confirmar:
            ordenes[indice][3] = "Finalizada"
            self.actualizar_tabla()

            messagebox.showinfo(
                "Operacion exitosa",
                "La orden fue finalizada correctamente."
            )

if __name__ == "__main__":
    clientes_prueba = [
        {
            "codigo": "1001",
            "nombre": "Cliente de prueba",
            "direccion": "Malacatan",
            "plan": "20 Mbps",
            "precio": 200.0,
            "estado": "activo"
        }
    ]

    ventana = tk.Tk()
    OrdenesGUI(ventana, clientes_prueba)
    ventana.mainloop()
