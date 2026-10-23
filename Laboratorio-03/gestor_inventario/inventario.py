class Inventario:

    def __init__(self):
        self._productos = []

    def registrar_producto(self, producto):
        if self.buscar_por_codigo(producto.codigo) is not None:
            return False
        self._productos.append(producto)
        return True

    def listar_productos(self):
        return self._productos.copy()

    def buscar_por_codigo(self, codigo):
        for producto in self._productos:
            if producto.codigo == codigo:
                return producto
        return None

    def actualizar_existencias(self, codigo, nueva_cantidad):
        producto = self.buscar_por_codigo(codigo)
        if producto is not None:
            return producto.actualizar_existencias(nueva_cantidad)
        return False

    def eliminar_producto(self, codigo):
        producto = self.buscar_por_codigo(codigo)
        if producto is not None:
            self._productos.remove(producto)
            return True
        return False

    def productos_sin_stock(self):
        return [p for p in self._productos if p.cantidad == 0]

    def resumen(self):
        total_productos = len(self._productos)
        unidades_disponibles = sum(p.cantidad for p in self._productos)
        valor_total = sum(p.calcular_valor() for p in self._productos)
        categorias_utilizadas = {p.categoria for p in self._productos}
        return (
            total_productos,
            unidades_disponibles,
            valor_total,
            categorias_utilizadas,
        )