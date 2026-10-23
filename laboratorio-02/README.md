\# Laboratorio 02: Gestor de Inventarios en Python



\*\*Aprendiz:\*\* Diana Reyes  

\*\*Programa:\*\* Tecnólogo en Análisis y Desarrollo de Software  

\*\*Repositorio:\*\* https://github.com/dianareyes-pro/laboratorios



\---



\## Descripción del Proyecto



Este laboratorio consiste en el desarrollo de un \*\*Gestor de Inventario interactivo por consola\*\* desarrollado en Python (`gestor\_inventario.py`). El programa permite administrar productos mediante un menú interactivo con opciones de registro, consulta, búsqueda, actualización, eliminación y generación de reportes económicos y estadísticos.



\---



\## Funcionalidades Implementadas



1\. \*\*Registrar Producto:\*\* Permite ingresar un producto especificando su código, nombre, categoría, precio y cantidad.

2\. \*\*Consultar Todos los Productos:\*\* Muestra el listado completo de productos guardados en el inventario.

3\. \*\*Buscar Producto:\*\* Permite localizar un producto ingresando su código único.

4\. \*\*Actualizar Existencias:\*\* Modifica el stock de un producto validando que no se ingresen cantidades negativas.

5\. \*\*Eliminar Producto:\*\* Elimina un producto del inventario mediante su código.

6\. \*\*Informes y Reportes:\*\*

&#x20;  - Cálculo del valor total del inventario (Precio × Cantidad).

&#x20;  - Producto con mayor y menor stock.

&#x20;  - Listado de categorías únicas registradas.

7\. \*\*Salir:\*\* Finaliza la ejecución del programa.



\---



\## Colecciones y Estructuras de Control Utilizadas



\- \*\*Diccionarios (`dict`):\*\* Estructura principal para almacenar cada producto (`código` como clave y un diccionario de atributos como valor).

\- \*\*Tuplas (`tuple`):\*\* Utilizadas para definir categorías fijas y no modificables de productos.

\- \*\*Conjuntos (`set`):\*\* Utilizados para extraer y mostrar de forma eficiente las categorías únicas sin duplicados.

\- \*\*Ciclo `while`:\*\* Mantiene el menú interactivo activo hasta que el usuario decida salir.

\- \*\*Estructuras `if / elif / else`:\*\* Controlan el flujo de opciones del menú y las validaciones de datos ingresados.



\---



\##  Validaciones del Sistema



\- \*\*Códigos Duplicados:\*\* No permite registrar dos productos con el mismo código.

\- \*\*Categorías Validadas:\*\* Revisa que la categoría ingresada pertenezca a las categorías permitidas en la tupla.

\- \*\*Precios y Cantidades Positivas:\*\* Rechaza precios menores o iguales a cero y cantidades de existencias negativas.



\---



\##  Instrucciones de Ejecución



Para ejecutar el programa, abre la terminal en esta carpeta y corre el siguiente comando:



```bash

python gestor\_inventario.py

