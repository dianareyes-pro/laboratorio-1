\# Gestor de Inventarios Multi-Laboratorio — Evolución Progresiva



\*\*Aprendiz:\*\* Diana Faizury Reyes Correa (`dianareyes-pro`)  

\*\*Programa:\*\* Tecnólogo en Análisis y Desarrollo de Software (ADSO)  

\*\*Ficha:\*\* 33880887  

\*\*Repositorio Oficial:\*\* \[https://github.com/dianareyes-pro/laboratorios](https://github.com/dianareyes-pro/laboratorios)



\---



\## Resumen de Evolución del Proyecto



Este repositorio documenta la evolución progresiva en la construcción de un \*\*Gestor de Inventarios en Python\*\*, transitando desde la programación imperativa básica hasta una arquitectura orientada a objetos desacoplada, con persistencia de datos en archivos JSON, generación de reportes ejecutivos en CSV y manejo defensivo de excepciones.



\---



\## 📂 Estructura General del Repositorio



```text

laboratorios/

├── laboratorio-01/          # Lógica secuencial, variables, operadores y cotizador interactivo

├── laboratorio-02/          # Estructuras de control, colecciones (dict, list, set) y menú CRUD

├── Laboratorio-03/          # Programación Orientada a Objetos (POO), clases, encapsulamiento y propiedades

└── laboratorio-04/          # Persistencia JSON, exportación CSV, excepciones y arquitectura limpia

&#x20;   ├── datos/               # Almacenamiento persistente (productos.json)

&#x20;   ├── reportes/            # Archivos exportados en CSV

&#x20;   ├── almacenamiento.py    # Servicio de lectura/escritura y respaldos (.bak)

&#x20;   ├── reportes.py          # Servicio de generación de informes tabulares

&#x20;   ├── producto.py          # Entidad de dominio con validadores

&#x20;   ├── inventario.py        # Colección de objetos y lógica de negocio

&#x20;   └── main.py              # Interfaz interactiva de consola con control defensivo

