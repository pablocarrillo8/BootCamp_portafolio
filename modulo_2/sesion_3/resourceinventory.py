class ResourceInventory:
    def __init__(self, id_inventario):
        # Atributos
        self.id_inventario = id_inventario # atributo público
        self._recursos = [] # Lista privada
 
 
    def add_resource(self, item):# Agregar un recurso
       
 
    def resource_frequency(self, item): #Contar la frecuencia de un recurso específico
        return self._recursos.count(item)
 
    def get_resources(self):# Presenta la lista completa de recursos agregados.
        pass
 
    def resource_priority(count):# Calcular una prioridad usando math.log()
        pass
 
 
def main():
    inventory = None
 
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Ingresar ID del inventario")
        print("2. Ingresar recursos urbanos")
        print("3. Mostrar recursos en el inventario")
        print("4. Calcular prioridad de un recurso")
        print("5. Salir")
        opcion = input("Seleccione una opción (1-5): ")
 
        if opcion == '1':
            pass
 
        elif opcion == '2':
            pass
 
        elif opcion == '3':
            pass
 
        elif opcion == '4':
            pass
 
        elif opcion == '5':
            print("Salir. ¡Hasta pronto!")
            break
 
        else:
            print("Opción inválida. Intente nuevamente.")
 
 
