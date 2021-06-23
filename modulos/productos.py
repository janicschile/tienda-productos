class Productos:
    def __init__(self, nombre, precio, categoria):
        self.nombre = nombre
        self.precio = precio
        self.precioOriginal = precio
        self.categoria = categoria

    def actualizarPrecio(self, actualizaPorcentaje, incremento):
        if incremento:
            self.precio += self.precio * ( actualizaPorcentaje/100 )
            self.precioOriginal
        elif not incremento:
            self.precio -= self.precio * ( actualizaPorcentaje/100 )
            self.precioOriginal
        return self

    def informacion(self):
        if self.precio > self.precioOriginal or self.precio < self.precioOriginal:
            print(f"  Nombre del Producto: {self.nombre}\n  Categoria: {self.categoria}\n  Precio: ${self.precio} - Antes:(${self.precioOriginal}) *** OFERTA ***\n =========================================================================")
        else:
            print(f"  Nombre del Producto: {self.nombre}\n  Categoria: {self.categoria}\n  Precio: ${self.precio}\n =========================================================================")
        return self