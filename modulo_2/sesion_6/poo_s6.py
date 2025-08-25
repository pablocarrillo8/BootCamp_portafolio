#usando POO en Python 
#sistema de gestión de libros en una biblioteca

import zipfile

# 1. Definimos la clase Libro con atributos privados
class Libro:
    # 2. Constructor para inicializar los atributos del libro
    def __init__(self, titulo, autor, isbn):
        self._titulo = titulo    # Atributo privado: título del libro
        self._autor = autor      # Atributo privado: autor del libro
        self._isbn = isbn        # Atributo privado: ISBN del libro

    # 3. Métodos get para acceder a los atributos desde fuera de la clase
    def get_titulo(self):
        return self._titulo      # Devuelve el título

    def get_autor(self):
        return self._autor       # Devuelve el autor

    def get_isbn(self):
        return self._isbn        # Devuelve el ISBN

    # 4. Método que describe el libro con todos sus datos
    def descripcion(self):
        # Devuelve una cadena con el formato solicitado
        return f"Título: {self._titulo}, Autor: {self._autor}, ISBN: {self._isbn}"

# 5. Clase Biblioteca para gestionar una colección de libros
class Biblioteca:
    def __init__(self):
        self.libros = []  # Lista vacía para almacenar objetos de tipo Libro

    # Método para agregar un libro a la biblioteca
    def agregar_libro(self, libro):
        self.libros.append(libro)  # Añade el libro a la lista de libros

    # 6. Método para mostrar todos los libros en la biblioteca
    def mostrar_libros(self):
        # Recorre la lista de libros e imprime su descripción
        for libro in self.libros:
            print(libro.descripcion())

# 7. Parte principal del programa: crear libros, agregarlos a la biblioteca y mostrarlos

# Crear una instancia de Biblioteca
mi_biblioteca = Biblioteca()

# Crear dos objetos de tipo Libro

libro1 = Libro("Rayuela", "Julio Cortázar", "978-8437604947")
libro2 = Libro("La casa de los espíritus", "Isabel Allende", "978-1400034941")
libro3 = Libro("La ciudad y los perros", "Mario Vargas Llosa", "978-8490626773")
libro4 = Libro("Como agua para chocolate", "Laura Esquivel", "978-0385420174")

# Agregar los libros a la biblioteca
mi_biblioteca.agregar_libro(libro1)
mi_biblioteca.agregar_libro(libro2)
mi_biblioteca.agregar_libro(libro3)
mi_biblioteca.agregar_libro(libro4) 

# Mostrar los detalles de los libros almacenados
mi_biblioteca.mostrar_libros()

# 8. Guardar la biblioteca en un archivo ZIP
with zipfile.ZipFile('biblioteca.zip', 'w') as zipf:
    zip_ref = zipf.writestr('poo_s6.py', '\n'.join(libro.descripcion() for libro in mi_biblioteca.libros))
# El archivo ZIP contiene un archivo de texto con la descripción de los libros