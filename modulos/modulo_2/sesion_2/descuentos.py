#Conocimientos básicos de Python
import zipfile
# Crear variables
precio_producto = 1200      # Precio del producto
cantidad = 3                # Cantidad comprada
descuento = 50              # Descuento en porcentaje

# Calcular el precio total sin descuento
total_sin_descuento = precio_producto * cantidad

# Calcular el monto de descuento
monto_descuento = total_sin_descuento * (descuento / 100)

# Calcular el precio total con descuento
total_con_descuento = total_sin_descuento - monto_descuento

# Imprimir los resultados
print("Total sin descuento: $", total_sin_descuento)
print("Monto de descuento: $", monto_descuento)
print("Total con descuento: $", total_con_descuento)

# Crear un archivo ZIP y añadir archivos a él
with zipfile.ZipFile('actividad2_modulo2.zip', 'w') as zipf:
    zipf.write('descuentos.py')  # Agrega archivo1.txt al ZIP



#  The ### zipfile ## module in Python provides tools for creating, reading, writing, appending, and
# listing ZIP archives.It supports various modes for opening ZIP files,
# such as 'r' for reading, 'w' for writing, 'a' for appending, and 'x' for exclusive creation.   


# Opening a ZIP file:
# Python

# with zipfile.ZipFile('my_archive.zip', 'r') as zip_ref:
#     # Operations on the ZIP file

# Reading files from a ZIP archive:
# Python

# with zipfile.ZipFile('my_archive.zip', 'r') as zip_ref:
#     for file_name in zip_ref.namelist():
#         print(file_name)
#         with zip_ref.open(file_name) as file:
#             content = file.read()
#             print(content)

# Creating a new ZIP file:
# Python code

# with zipfile.ZipFile('new_archive.zip', 'w') as zip_ref:
#     zip_ref.write('file1.txt')
#     zip_ref.write('file2.txt')

# Adding files to an existing ZIP file:
# Python code

# with zipfile.ZipFile('existing_archive.zip', 'a') as zip_ref:
#     zip_ref.write('file3.txt')

# Extracting all files from a ZIP archive:
# Python code 

# with zipfile.ZipFile('my_archive.zip', 'r') as zip_ref:
#     zip_ref.extractall('output_dir')

# Extracting specific files from a ZIP archive:
# Python code

# with zipfile.ZipFile('my_archive.zip', 'r') as zip_ref:
#     zip_ref.extract('file1.txt', 'output_dir')