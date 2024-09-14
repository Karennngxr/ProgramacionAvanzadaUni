class Producto:
    id = 0
    nombre = ""
    precio = 0
    categoria = ""
    color = ""

    def __init__(self, id, nombre, precio, categoria, color):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        self.color = color