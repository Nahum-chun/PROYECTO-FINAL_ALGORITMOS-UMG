# Universidad Mariano Gálvez

**Facultad:** Ingeniería

**Carrera:** Ingeniería en Sistemas de Información y Ciencias de la Computación

**Curso:** Algoritmos

**Docente:** Emanuel Alejandro Mazariegos Cifuentes

**Proyecto:** NET CONTROL ISP

## 1. Documentación Técnica

### Descripción del sistema

Diseñamos NET CONTROL ISP como una herramienta de gestión y administración para proveedores de servicios de internet. Nuestra plataforma nos permite manejar el ciclo de vida de los clientes (altas, bajas, búsquedas y eliminación), asignar planes de velocidad y registrar órdenes de trabajo técnico cuando nos reportan fallas. Además, integramos un panel de control y estadísticas para visualizar nuestros ingresos mensuales, el estado de los clientes y un listado ordenado del valor de los planes contratados.

### Cómo lo hicimos

Construimos el sistema íntegramente en Python 3 utilizando la biblioteca estándar, sin depender de paquetes de terceros.

* **Almacenamiento:** Decidimos no utilizar una base de datos externa; manejamos los registros en memoria RAM durante el tiempo de ejecución a través de listas y diccionarios compartidos.

* **Lógica Principal:** Combinamos programación estructurada para el menú de consola (CLI) y manejo de eventos para la interfaz gráfica.

* **Algoritmia:** Programamos el ordenamiento de los clientes desde cero utilizando el algoritmo "Bubble Sort", comparando iterativamente las posiciones de memoria según la llave `precio` de cada diccionario.

* **Interfaz:** Utilizamos la librería nativa `tkinter` junto con componentes `Treeview` para renderizar las tablas de datos.

### Manual de Uso y Capturas

**Requisitos:** Necesitamos tener Python 3.x instalado en el equipo.

**Pasos de ejecución:**

1. Descomprimimos la carpeta con todos los archivos `.py` del proyecto.

2. Abrimos la terminal, navegamos a la ruta de la carpeta y ejecutamos: `python main.py`.

3. Ingresamos nuestras credenciales de acceso (Usuario: `pepe`, Contraseña: `5555`).  
   <img width="1246" height="122" alt="Captura de pantalla 2026-10-30 113808" src="https://github.com/user-attachments/assets/f1560cb0-8780-4cdd-bf29-236a3c94ad32" />


4. Utilizamos el teclado numérico para navegar por el menú principal (Opciones 1 al 9).  
   <img width="507" height="297" alt="Captura de pantalla 2026-10-30 113904" src="https://github.com/user-attachments/assets/bdeb8f94-0cdf-427f-930b-3c51ac00c958" />


5. **Para agregar clientes (Opción 1):** Digitamos el código, nombre, dirección, plan, precio y estado (activo/inactivo) siguiendo las instrucciones de la terminal.  
   <img width="466" height="217" alt="Captura de pantalla 2026-10-30 114015" src="https://github.com/user-attachments/assets/881fffea-788c-4abe-9b04-f952c6cbca6f" />


6. **Para asignar órdenes (Opción 5):** Ingresamos un código de cliente válido. Configuramos el sistema para bloquear el registro si el abonado no existe.  
   <img width="440" height="163" alt="Captura de pantalla 2026-10-30 114059" src="https://github.com/user-attachments/assets/4be650c6-38a9-4007-b9ad-f25ebc117801" />


7. **Para usar la interfaz gráfica (Opción 8):** Abrimos una ventana de Windows independiente. Al hacer clic en "Ordenar por Precio (Burbuja)", la tabla organiza a los clientes registrados del plan más barato al más caro de manera visual.  
   <img width="1078" height="893" alt="Captura de pantalla 2026-10-30 114146" src="https://github.com/user-attachments/assets/7908bb69-5847-4e23-a442-e6217d1e5732" />

<img width="841" height="632" alt="Captura de pantalla 2026-10-30 114158" src="https://github.com/user-attachments/assets/b4ef3112-513c-419d-b3b7-9fafd86d876e" />


## 2. Documentación Administrativa

### Integrantes y rol de cada uno

Nos dividimos el desarrollo del proyecto asignando módulos específicos para cada integrante del grupo:

* **Nahúm Gamaliel Chún Ramírez (0903-26-9546):** Desarrolló la estructura central de nuestro programa y las operaciones de base de datos en memoria. Creó los scripts `main.py` y `clientes.py` (Lógica CRUD de abonados y menú principal).

* **Pedro Andrés Navarro Mérida (0903-26-12272):** Se encargó de la capa visual y la lógica de estructuras de datos. Desarrolló `Modulo_de_Interfaz_Grafica.py` y `main_Módulo_de_Ordenamiento.py` (Implementación del algoritmo Bubble Sort).

* **José Pablo Tul Escobar (0903-26-8337):** Asumió la responsabilidad de la lógica de negocio secundaria y métricas. Creó el archivo `Modulo_Ordenes.py` (Gestión de fallas, técnicos asignados y cálculo de estadísticas financieras).

### Organización del equipo

Adoptamos un modelo de trabajo modular. Definimos previamente las estructuras de datos que utilizaríamos de forma global (las listas compartidas `clientes` y `ordenes`). Al estandarizar que cada cliente sería un diccionario con claves específicas y cada orden una lista, los tres pudimos programar nuestros respectivos scripts de forma independiente. Finalmente, unificamos el código importando todas las funciones hacia nuestro orquestador principal (`main.py`).

### Conclusiones

1. Comprobamos que la separación del código en distintos módulos facilitó nuestra depuración de errores y nos permitió trabajar en el mismo sistema simultáneamente sin generar conflictos de integración.

2. Al implementar manualmente el algoritmo de ordenamiento de burbuja, aprendimos a manipular diccionarios y listas complejas en Python basándonos en un atributo específico (el precio), lo que optimizó la presentación de nuestros datos.

3. Confirmamos que el uso de la librería estándar `tkinter` fue una excelente decisión para trasladar nuestra aplicación de consola a una interfaz gráfica amigable, mejorando drásticamente la experiencia de uso.

## 3. Documentación de Seguridad

### Riesgos de nuestro login actual

Identificamos que el sistema de autenticación que implementamos en `main.py` y `main_gui.py` presenta vulnerabilidades críticas que comprometen la seguridad del sistema:

* **Credenciales "Hardcoded":** Escribimos el usuario (`pepe`) y la contraseña (`5555`) directamente en texto plano en el código fuente. Cualquier persona con acceso a nuestros archivos `.py` puede leer las credenciales sin esfuerzo.

* **Falta de cifrado (Hashing):** Nuestras contraseñas no pasan por ninguna función criptográfica.

* **Ausencia de almacenamiento seguro:** No realizamos validación contra una base de datos segura.

* **Bloqueo efímero:** Controlamos el bloqueo tras tres intentos fallidos con una variable local en memoria. Si alguien reinicia el programa (`python main.py`), el contador vuelve a cero, permitiendo ataques de fuerza bruta ilimitados.

### Cómo podríamos mejorarlo

Para llevar nuestro login a un estándar profesional, necesitamos aplicar los siguientes cambios:

1. **Migrar a Base de Datos:** Guardar los usuarios en una base de datos (como SQLite o MySQL) completamente fuera de nuestro código fuente.

2. **Implementar Hashing:** Antes de guardar o validar contraseñas, debemos procesarlas utilizando algoritmos de derivación de claves seguros como `bcrypt` o `Argon2`. Así, incluso si roban la base de datos, no podrán leer las contraseñas.

3. **Variables de entorno (.env):** Si requerimos usar credenciales maestras, debemos alojarlas en variables de entorno locales en el servidor, jamás en nuestros scripts de Python.

4. **Bloqueo por IP/Tiempo:** Registrar los intentos fallidos vinculados al usuario o a la IP con "timestamps" para generar bloqueos temporales reales (ej. cuenta bloqueada por 15 minutos) que sobrevivan al reinicio de nuestra aplicación.
