from producto import Producto
from inventario import Inventario

inventario = Inventario()

while True:
    print("\n*** BIENVENIDO ***")
    print("Opciones en el Sistema")
    print("1. Registrar producto")
    print("2. Eliminar producto")
    print("3. Mostrar productos")
    print("4. Salir")

    opcion = input("Ingresa la opción que deseas: ")

    if opcion == "1":
        id = int(input("Ingresa el id del producto: "))
        nombre = input("Ingresa el nombre del producto: ")
        precio = int(input("Ingresa el precio del producto: "))
        categoria = input("Ingresa la categoría del producto: ")
        color = input("Ingresa el color del producto: ")

        producto = Producto(id, nombre=nombre, precio=precio, categoria=categoria, color=color)
        inventario.agregar_producto(producto=producto)
        print("\nProducto agregado correctamente")

    elif opcion == "2":
        id_a_eliminar = int(input("Ingresa el ID del producto a eliminar: "))
        inventario.eliminar_producto(id_a_eliminar)
        print("Producto eliminado correctamente")
    
    elif opcion == "3":
        inventario.mostrar_productos()
    
    else:
        print("\nHasta luego")
        break
