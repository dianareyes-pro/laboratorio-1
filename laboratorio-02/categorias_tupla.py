categorias = ("Periféricos", "Componentes", "Accesorios", "Almacenamiento")

print("CATÁLOGO DE CATEGORÍAS ")

print("Categorías disponibles:")
for posicion, categoria in enumerate(categorias, start=1):
    print(f"{posicion}. {categoria}")

elegida = input("\nIngresa el nombre de una categoría a buscar: ").strip()

if elegida in categorias:
    print(f"La categoría '{elegida}' es válida y está registrada")
else:
    print(f"La categoría '{elegida}' no está registrada en el sistema.")

print(f"Cantidad total de categorías fijas: {len(categorias)}")