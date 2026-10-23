class Inventario:

    def __init__(self):
        self._productos = []

    def agregar(self, producto):
        
        for p in self._productos:
            if p.codigo == producto.codigo:
                return False  

        self._productos.append(producto)
        return True

    def listar(self):
        return self._productos.copy()

    def buscar_por_codigo(self, codigo):
        for producto in self._productos:
            if producto.codigo == codigo:
                return producto
        return None

    def eliminar(self, codigo):
        producto = self.buscar_por_codigo(codigo)
        if producto is not None:
            self._productos.remove(producto)
            return True  
        return False  