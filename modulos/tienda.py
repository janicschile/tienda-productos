class Tienda:
    def __init__(self, nombre, productos=[]):
        self.nombre = nombre
        self.productos = productos

    def agregarProducto(self, nuevoProducto):
        self.productos.append(nuevoProducto)
        return self

    def venderProducto(self, id):
        #cabecera()
        self.productos[id].informacion()
        del self.productos[id]
        return self

    def descuento(self, elDescuento):
        for product in self.productos:
            product.actualizarPrecio(elDescuento, False)
        return self

    def inflacion(self, laInflacion):
        for product in self.productos:
            product.actualizarPrecio(laInflacion, True)
        return self