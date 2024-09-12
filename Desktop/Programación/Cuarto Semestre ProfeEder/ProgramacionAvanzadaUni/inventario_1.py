class Inventario:
    productos = []

    # Agregar productos
    def agregar_producto(self, producto):
        self.productos.append(producto)

    # Eliminar productos
    def eliminar_producto(self, id_producto_a_eliminar):
        for producto in self.productos:
            if producto.id == id_producto_a_eliminar:
                self.productos.remove(producto)
                print("\nSe eliminó el producto con el ID: ", id_producto_a_eliminar)
                break

    def mostrar_productos(self):
        print("\n----- Productos en el Sistema -----")

        if len(self.productos) == 0:
            print("\nNo existen productos en el sistema\n")
            return

        for producto in self.productos:
            print("\n")
            print("Id: ", producto.id)
            print("Nombre: ", producto.nombre)
            print("Precio", producto.precio)
            print("Categoria: ", producto.categoria)
            print("Color: ", producto.color)