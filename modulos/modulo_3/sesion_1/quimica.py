#  Guía de Aprendizaje: Reto 2 – Balance de Reacciones Químicas
#  ¿Qué es una ecuación química?
# Una ecuación química representa una reacción química. Muestra cómo unas sustancias (reactantes) se transforman en otras (productos) mediante un proceso químico.
################### Ejemplo:#############
#
# CH4+2O2→CO2+2H2O
# CH4​+2O2​→CO2​+2H2​O
#
##### Componentes de una ecuación química:
#     Reactantes: Sustancias iniciales que reaccionan (izquierda de la flecha).
#         En el ejemplo: CH₄ y O₂
#     Productos: Sustancias formadas al final (derecha de la flecha).
#         En el ejemplo: CO₂ y H₂O
#     Flecha (→): Indica la dirección de la reacción.
#     Coeficientes: Números delante de los compuestos que indican cuántas moléculas o moles intervienen.
#
###################  ¿Qué es el balanceo químico? ###################
#
# Es el proceso de igualar el número de átomos de cada elemento en los reactantes y en los productos. 
# Se hace para cumplir con la Ley de Conservación de la Materia (la materia no se crea ni se destruye).
#
#  Función: balancear_reaccion
#   Esta función valida si una reacción química está balanceada basándose en los coeficientes de sus componentes.
#   Requisitos de la función:
#     Debe recibir una lista de al menos 4 coeficientes (2 para reactivos y 2 para productos, mínimo).
#     Debe dividir la lista por la mitad: la primera mitad son reactantes y la segunda, productos.
#     Calcula la suma total de coeficientes de ambos lados.
#     Compara ambas sumas: si la diferencia absoluta entre ellas es menor a 0.01, la reacción se considera balanceada.