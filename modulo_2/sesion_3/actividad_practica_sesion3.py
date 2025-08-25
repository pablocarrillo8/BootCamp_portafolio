# Promedio de notas
import zipfile
# Lista para almacenar resultados de los estudiantes
estudiantes = []


while True:
    nombre = str(input("Ingrese el nombre del estudiante : "))

    #ingreso de notas
    matematicas = float(input("Ingrese la nota del estudiante para matematicas: "))
    ciencias = float(input("Ingrese la nota del estudiante para ciencias: "))
    ingles = float(input("Ingrese la nota del estudiante para ingles: "))
    
    if matematicas >= 60 and ciencias >= 60 and ingles >= 60:
        print(f"{nombre} ha aprobado todas las materias.")
    else:
        print(f"{nombre} necesita mejorar en alguna materia o las tres.")
        #break
    # Calcular el promedio de notas
    promedio = (matematicas + ciencias + ingles) / 3
    # evaluación del promedio y comentario

    comentario = []
    if promedio >= 90:
        comentario = "Su promedio es ¡Excelente!"
        #comentario = print(f"{nombre}: Su promedio es ¡Excelente!")  La función print() muestra en pantalla pero no devuelve texto, por eso comentario se vuelve None.
    elif promedio >= 75:
        comentario = "Su promedio es Bueno"
        #comentario = print(f"{nombre}: Su promedio es Bueno")
    else:
        comentario = "Su promedio necesita mejorar"
        #comentario = print(f"{nombre}: Su promedio necesita mejorar")
   # Expresión ternaria para puntuación perfecta 
    comentario += " ¡Puntuación perfecta!" if promedio == 100 else ""
    # Guardar resultados en la lista estuadiantes
    estudiantes.append({"nombre": nombre, "comentario": comentario})

    # Preguntar si quiere continuar (punto 2)
    continuar = input("¿Desea ingresar otro estudiante? (s/n): ")
    if continuar.lower() != 's':
        break        
# Mostrar resultados con bucle for (punto 5)
print("\n Resumen de estudiantes:")
for estudiante in estudiantes:
    print(f"Estudiante: {estudiante['nombre']} - Comentario: {estudiante['comentario']}")    

with zipfile.ZipFile('actividad_practica_sesion3.zip', 'w') as zip_ref:
    zip_ref.write('actividad_practica_sesion3.py')
print("Archivo comprimido creado: actividad_practica_sesion3.zip")