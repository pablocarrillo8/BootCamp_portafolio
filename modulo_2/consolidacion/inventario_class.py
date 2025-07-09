class Libro:
    def __init__(self, titulo, autor, precio, stock):
        self.titulo = titulo
        self.autor = autor
        self.precio = precio
        self.stock = stock

    def tiene_stock(self, cantidad):
        return self.stock >= cantidad

    def aplicar_descuento(self, porcentaje):
        return self.precio * (1 - porcentaje)

    def restar_stock(self, cantidad):
        self.stock -= cantidad


class Libreria:
    def __init__(self):
        self.libros = []
        self.descuentos = {}
        self.carrito = []
        self.total_pagado = 0
        self.total_ahorro = 0

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def definir_descuento(self, autor, porcentaje):
        self.descuentos[autor] = porcentaje

    def mostrar_libros_disponibles(self):
        print("\nLibros disponibles en stock:")
        for libro in self.libros:
            if libro.stock > 0:
                print(f"- {libro.titulo} por {libro.autor} - ${libro.precio} CLP ({libro.stock} disponibles)")

    def filtrar_por_precio(self, minimo, maximo):
        print("\nLibros en el rango de precios:")
        encontrados = False
        for libro in self.libros:
            if minimo <= libro.precio <= maximo:
                print(f"- {libro.titulo} - ${libro.precio} CLP")
                encontrados = True
        if not encontrados:
            print("No se encontraron libros en ese rango.")

    def comprar_libro(self, titulo, cantidad):
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                if libro.tiene_stock(cantidad):
                    descuento = self.descuentos.get(libro.autor, 0)
                    precio_desc = libro.aplicar_descuento(descuento)
                    total = precio_desc * cantidad
                    ahorro = (libro.precio * cantidad) - total

                    libro.restar_stock(cantidad)
                    self.carrito.append((libro.titulo, cantidad, total))
                    self.total_pagado += total
                    self.total_ahorro += ahorro

                    print(f"Descuento aplicado: {int(descuento * 100)}%")
                    print(f"Compra exitosa: {cantidad} x {libro.titulo} - Total: ${int(total)} CLP\n")
                    return
                else:
                    print("Error: No hay suficiente stock disponible.\n")
                    return
        print("Error: Libro no encontrado.\n")

    def mostrar_factura(self):
        print("\n--- Factura de Compra ---")
        for item in self.carrito:
            print(f"{item[1]} x {item[0]} - ${int(item[2])} CLP")
        print(f"\nTotal pagado: ${int(self.total_pagado)} CLP")
        print(f"Ahorro total por descuentos: ${int(self.total_ahorro)} CLP")
        print("--- Gracias por su compra ---\n")


# Crear librería y cargar libros
libreria = Libreria()
libreria.agregar_libro(Libro("Data Science con Python", "Juan Pérez", 25500, 10))
libreria.agregar_libro(Libro("Introducción a la IA", "Laura Torres", 30000, 5))
libreria.agregar_libro(Libro("Fundamentos de Física", "Isaac Newton", 18000, 2))
libreria.agregar_libro(Libro("Aprende HTML y CSS", "Ana Ruiz", 15000, 0))
libreria.agregar_libro(Libro("Python para Principiantes", "Guido van Rossum", 22000, 8))

# Definir descuentos
libreria.definir_descuento("Juan Pérez", 0.15)
libreria.definir_descuento("Laura Torres", 0.10)

# Menú interactivo
while True:
    print("\n--- Sistema de Compras ---")
    print("1. Mostrar libros disponibles")
    print("2. Filtrar libros por rango de precios")
    print("3. Comprar libro")
    print("4. Finalizar compra y mostrar factura")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        libreria.mostrar_libros_disponibles()
    elif opcion == "2":
        try:
            minimo = float(input("Ingrese el precio mínimo: "))
            maximo = float(input("Ingrese el precio máximo: "))
            libreria.filtrar_por_precio(minimo, maximo)
        except ValueError:
            print("Error: Ingrese valores válidos para el precio.")
    elif opcion == "3":
        titulo = input("Ingrese el título del libro a comprar: ")
        try:
            cantidad = int(input("Ingrese la cantidad deseada: "))
            libreria.comprar_libro(titulo, cantidad)
        except ValueError:
            print("Cantidad inválida.")
    elif opcion == "4":
        libreria.mostrar_factura()
        break
    else:
        print("Opción no válida. Intente de nuevo.")