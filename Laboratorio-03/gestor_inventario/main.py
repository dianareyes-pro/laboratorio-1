from inventario import Inventario
from producto import CATEGORIAS, Producto
def mostrar_menu():
    print(" GESTOR DE INVENTARIO")
    print("1. Registrar producto")
    print("2. Listar productos")
    print("3. Buscar por código")
    print("4. Actualizar existencias")
    print("5. Eliminar producto")
    print("6. Consultar productos sin stock")
    print("7. Resumen del inventario")
    print("0. Salir")

def leer_cantidad():
    while True:
        try:
            cantidad = int(input("Cantidad: "))
            if cantidad < 0:
                print("La cantidad no puede ser negativa.")
                continue
            return cantidad
        except ValueError:
            print("Debes escribir un número entero.")

def leer_precio():
    while True:
        try:
            precio = float(input("Precio: "))
            if precio <= 0:
                print("El precio debe ser mayor que cero.")
                continue
            return precio
        except ValueError:
            print("Debes escribir un número válido.")

def main():
    inventario = Inventario()
    opcion = ""
    while opcion != "0":
        mostrar_menu()
        opcion = input("Opción: ").strip()

        if opcion == "1":
            print("\n--- Registrar Producto ---")
            codigo = input("Código: ").strip()
            nombre = input("Nombre: ").strip()
            print(f"Categorías permitidas: {', '.join(CATEGORIAS)}")
            categoria = input("Categoría: ").strip()
            precio = leer_precio()
            cantidad = leer_cantidad()

            try:
                nuevo_prod = Producto(
                    codigo, nombre, categoria, precio, cantidad
                )
                if inventario.registrar_producto(nuevo_prod):
                    print("Producto registrado exitosamente.")
                else:
                    print("Error: Ya existe un producto con ese código.")
            except ValueError as e:
                print(f"Error al crear el producto: {e}")

        elif opcion == "2":
            print("\n--- Lista de Productos ---")
            productos = inventario.listar_productos()
            if not productos:
                print("El inventario está vacío.")
            else:
                for p in productos:
                    print(
                        f"{p.codigo} - {p.nombre} - {p.categoria} - ${p.precio} - {p.cantidad} unidades"
                    )

        elif opcion == "3":
            print("\n--- Buscar Producto ---")
            codigo = input("Ingrese el código a buscar: ").strip()
            p = inventario.buscar_por_codigo(codigo)
            if p is not None:
                print(
                    f"Encontrado -> {p.codigo} | {p.nombre} | {p.categoria} | ${p.precio} | {p.cantidad} unidades"
                )
            else:
                print("Producto no registrado.")

        elif opcion == "4":
            print("\n--- Actualizar Existencias ---")
            codigo = input("Ingrese el código del producto: ").strip()
            p = inventario.buscar_por_codigo(codigo)
            if p is None:
                print("Producto no encontrado.")
            else:
                nueva_cantidad = leer_cantidad()
                if inventario.actualizar_existencias(codigo, nueva_cantidad):
                    print("Existencias actualizadas correctamente.")
                else:
                    print(
                        "No se pudo actualizar (la cantidad no puede ser negativa)."
                    )

        elif opcion == "5":
            print(" Eliminar Producto ")
            codigo = input("Ingrese el código del producto a eliminar: ").strip()
            if inventario.eliminar_producto(codigo):
                print("Producto eliminado correctamente.")
            else:
                print("El código no existe en el inventario.")

        elif opcion == "6":
            print("Productos sin Stock")
            sin_stock = inventario.productos_sin_stock()
            if not sin_stock:
                print("No hay productos agotados.")
            else:
                print("Sin existencias:")
                for p in sin_stock:
                    print(f"- {p.nombre} ({p.codigo})")

        elif opcion == "7":
            print("\n--- Resumen del Inventario ---")
            total_prod, unidades, valor, categorias = inventario.resumen()
            print(f"Productos registrados: {total_prod}")
            print(f"Unidades disponibles: {unidades}")
            print(f"Valor del inventario: ${valor}")
            cat_texto = (
                ", ".join(categorias) if categorias else "Ninguna"
            )
            print(f"Categorías utilizadas: {cat_texto}")

        elif opcion == "0":
            print("Programa finalizado.")
        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()