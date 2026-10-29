
import tkinter as tk
from tkinter import ttk

from Modulo_Ordenes import ordenes


class EstadisticasGUI:

    def __init__(self, ventana, clientes):
        self.ventana = ventana
        self.clientes = clientes

        ventana.title("NETCONTROL ISP - Estadisticas")
        ventana.geometry("650x520")
        ventana.configure(bg="#eef2f7")

        titulo = tk.Label(
            ventana,
            text="ESTADISTICAS DEL SISTEMA",
            font=("Arial", 17, "bold"),
            bg="#eef2f7"
        )
        titulo.pack(pady=20)

        self.tabla = ttk.Treeview(
            ventana,
            columns=("indicador", "resultado"),
            show="headings",
            height=12
        )

        self.tabla.heading("indicador", text="Indicador")
        self.tabla.heading("resultado", text="Resultado")

        self.tabla.column("indicador", width=260)
        self.tabla.column("resultado", width=300)

        self.tabla.pack(
            fill="both",
            expand=True,
            padx=25,
            pady=10
        )

        tk.Button(
            ventana,
            text="ACTUALIZAR ESTADISTICAS",
            command=self.actualizar_estadisticas,
            bg="#1769aa",
            fg="white",
            font=("Arial", 11, "bold"),
            pady=8
        ).pack(pady=15)

        self.actualizar_estadisticas()

    def actualizar_estadisticas(self):
        for elemento in self.tabla.get_children():
            self.tabla.delete(elemento)

        total = len(self.clientes)

        activos = sum(
            1 for cliente in self.clientes
            if str(cliente["estado"]).lower() == "activo"
        )

        inactivos = sum(
            1 for cliente in self.clientes
            if str(cliente["estado"]).lower() == "inactivo"
        )

        ingreso = sum(
            float(cliente["precio"])
            for cliente in self.clientes
        )

        promedio = ingreso / total if total else 0

        pendientes = sum(
            1 for orden in ordenes
            if orden[3] == "Pendiente"
        )

        finalizadas = sum(
            1 for orden in ordenes
            if orden[3] == "Finalizada"
        )

        if self.clientes:
            barato = min(
                self.clientes,
                key=lambda cliente: float(cliente["precio"])
            )

            caro = max(
                self.clientes,
                key=lambda cliente: float(cliente["precio"])
            )

            plan_barato = (
                f'{barato["plan"]} - Q{float(barato["precio"]):.2f}'
            )

            plan_caro = (
                f'{caro["plan"]} - Q{float(caro["precio"]):.2f}'
            )
        else:
            plan_barato = "Sin clientes"
            plan_caro = "Sin clientes"

        indicadores = [
            ("Clientes registrados", total),
            ("Clientes activos", activos),
            ("Clientes inactivos", inactivos),
            ("Ingreso mensual estimado", f"Q{ingreso:.2f}"),
            ("Promedio por cliente", f"Q{promedio:.2f}"),
            ("Plan mas economico", plan_barato),
            ("Plan mas caro", plan_caro),
            ("Ordenes pendientes", pendientes),
            ("Ordenes finalizadas", finalizadas)
        ]

        for indicador, resultado in indicadores:
            self.tabla.insert(
                "",
                tk.END,
                values=(indicador, resultado)
            )


if __name__ == "__main__":
    clientes_prueba = [
        {
            "codigo": "1001",
            "nombre": "Cliente A",
            "direccion": "Malacatan",
            "plan": "20 Mbps",
            "precio": 200.0,
            "estado": "activo"
        },
        {
            "codigo": "1002",
            "nombre": "Cliente B",
            "direccion": "San Marcos",
            "plan": "30 Mbps",
            "precio": 300.0,
            "estado": "inactivo"
        }
    ]

    ventana = tk.Tk()
    EstadisticasGUI(ventana, clientes_prueba)
    ventana.mainloop()
