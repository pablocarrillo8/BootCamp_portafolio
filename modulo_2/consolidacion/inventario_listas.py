# LIBROS y BYTES
import zipfile 
"""
LIBROS Y BYTES
Eres contratado/a por una pequeña cadena de librerías llamada "Libros & Bytes" para desarrollar un
sistema que gestione su inventario y permita a los usuarios simular una compra en línea. Trabajarás
solo en la lógica del sistema sin preocuparte de la interfaz visual. El sistema debe cumplir con los
siguientes requerimientos y funcionalidades.
Requerimientos:
"""

# 1. Definir variables básicas y tipos de datos
# seis libros clásicos de literatura universal:
libros = [
    {"titulo": "Don Quijote de la Mancha", "autor": "Miguel de Cervantes", "precio": 19990, "cantidad_stock": 10},
    {"titulo": "Cien años de soledad", "autor": "Gabriel García Márquez", "precio": 15990, "cantidad_stock": 5},
    {"titulo": "Crimen y castigo", "autor": "Fiódor Dostoyevski", "precio": 12990, "cantidad_stock": 8},
    {"titulo": "Orgullo y prejuicio", "autor": "Jane Austen", "precio": 10990, "cantidad_stock": 12},
    {"titulo": "Madame Bovary", "autor": "Gustave Flaubert", "precio": 14990, "cantidad_stock": 6},
    {"titulo": "La Odisea", "autor": "Homero", "precio": 9.990, "cantidad_stock": 15}
]   # Lista de libros


# Descuentos por autor
descuentos_por_autor = {
    "Jane Austen": 0.15,        # 15% descuento
    "Gabriel García Márquez": 0.20       # 20% descuento
}

# Variables globales para la factura
carrito = []
total_pagado = 0
total_ahorro = 0

# Funciones del sistema de compras
# Mostrar libros disponibles
def mostrar_libros_disponibles():
    print("\nLibros disponibles en cantidad_stock:")
    for libro in libros:
        if libro["cantidad_stock"] > 0:
            print(f"- {libro['titulo']} por {libro['autor']} - ${libro['precio']} CLP ({libro['cantidad_stock']} disponibles)")

# Función para filtrar libros por rango de precios
# Solicita al usuario un rango de precios y muestra los libros que se encuentran en ese rango
def filtrar_libros_por_precio():
    try:
        minimo = float(input("Ingrese el precio mínimo: "))
        maximo = float(input("Ingrese el precio máximo: "))
        print("\nLibros en ese rango de precio:")
        encontrados = False
        for libro in libros:
            if minimo <= libro["precio"] <= maximo:
                print(f"- {libro['titulo']} - ${libro['precio']} CLP")
                encontrados = True
        if not encontrados:
            print("No se encontraron libros en ese rango de precio.")
    except ValueError:
        print("Error: Ingrese valores válidos para el precio.")

# Función para comprar libros
# Esta función recibe el título del libro y la cantidad deseada, verifica el stock y aplica descuentos si corresponde
def comprar_libros(titulo, cantidad):
    global total_pagado, total_ahorro

    for libro in libros:
        if libro["titulo"].lower() == titulo.lower():
            if libro["cantidad_stock"] >= cantidad:
                precio_unitario = libro["precio"]
                descuento = descuentos_por_autor.get(libro["autor"], 0)
                precio_descuento = precio_unitario * (1 - descuento)
                total = precio_descuento * cantidad
                ahorro = (precio_unitario * cantidad) - total

                # Actualizar stock y registrar en el carrito
                libro["cantidad_stock"] -= cantidad
                carrito.append((libro["titulo"], cantidad, total))
                total_pagado += total
                total_ahorro += ahorro

                print(f"Descuento aplicado: {int(descuento * 100)}%")
                print(f"Compra exitosa: {cantidad} x {libro['titulo']} - Total: ${int(total)} CLP\n")
                return
            else:
                print("Error: No hay suficiente stock disponible.\n")
                return
    print("Error: Libro no encontrado.\n")

# Función para mostrar la factura de compra
# Muestra los libros comprados, la cantidad, el total pagado y el ahorro por descuentos
def mostrar_factura():
    print("\n--- Factura de Compra ---")
    for item in carrito:
        print(f"{item[1]} x {item[0]} - ${int(item[2])} CLP")
    print(f"\nTotal pagado: ${int(total_pagado)} CLP")
    print(f"Ahorro total por descuentos: ${int(total_ahorro)} CLP")
    print("--- Gracias por su compra ---\n")


# Bucle principal para el sistema de compras
while True:
    print("\n--- Bienvenido al sistema de compras de Libros & Bytes ---")
    print("1. Mostrar libros disponibles")
    print("2. Filtrar libros por rango de precios")
    print("3. Comprar libro")
    print("4. Finalizar compra y mostrar factura")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        mostrar_libros_disponibles()
    elif opcion == "2":
        filtrar_libros_por_precio()
    elif opcion == "3":
        titulo = input("Ingrese el título del libro a comprar: ")
        try:
            cantidad = int(input("Ingrese la cantidad deseada: "))
            comprar_libros(titulo, cantidad)
        except ValueError:
            print("Cantidad inválida.")
    elif opcion == "4":
        mostrar_factura()
        break
    else:
        print("Opción no válida. Intente de nuevo.")

zipfile.ZipFile('inventario_listas.zip', 'w').write('inventario_listas.py')
# Fin del sistema de compras