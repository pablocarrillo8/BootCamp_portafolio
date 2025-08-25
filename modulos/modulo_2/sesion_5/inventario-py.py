
# Inventario de productos en Python
# Este script gestiona un inventario de productos utilizando diferentes estructuras de datos en Python.
# y realiza diversas operaciones sobre ellas.
import zipfile
# 1. Lista con cinco productos
productos = ["zapatillas", "parkas", "calcetines", "pelotas", "canillera"]
print("Productos iniciales:", productos)

# 2. Agregar dos productos más y crear productos_destacados
productos.append("medias")
productos.append("poleras")
productos_destacados = productos[:3] # selcciona los primeros 3 productos
print("Productos después de agregar dos más:", productos)
print("Productos destacados:", productos_destacados)

# 3. Diccionario inventario con cantidades en stock
inventario = {
    "zapatillas": 2,
    "parkas": 5,
    "calcetines": 10,
    "pelotas": 20,
    "canillera": 3
}
print("Inventario inicial:", inventario)

# 4. Agregar nuevo producto y mostrar stock de uno específico
inventario["medias"] = 4
print("Inventario actualizado:", inventario)
print("Stock de pelotas:", inventario["pelotas"])

# 5. Tupla con categorías y mostrar segunda categoría
categorias = ("Electrónica", "Ropa", "Alimentos")
print("Categorías:", categorias)
print("Segunda categoría:", categorias[1])

# 6. Desempaquetado de tupla en variables individuales
categoria1, categoria2, categoria3 = categorias
print("Categoría 1:", categoria1)
print("Categoría 2:", categoria2)
print("Categoría 3:", categoria3)

# 7. Set para productos únicos (elimina duplicados si existen)
productos_unicos = set(productos)
print("Productos únicos (sin duplicados):", productos_unicos)

# 8. Comprensión de listas para poner productos en mayúsculas
productos_mayusculas = [producto.upper() for producto in productos]
print("Productos en mayúsculas:", productos_mayusculas)

#with zipfile.ZipFile('new_archive.zip', 'w') as zip_ref:
#    zip_ref.write('file1.txt')