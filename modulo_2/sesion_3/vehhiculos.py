class PuclicVehicle:
    def __init__(self, vehicle_id):
        self.vehicle_id = vehicle_id
        self.__paradas_visitadas = []
 
    def visit_stop(self, paradadistancia):
        self.__paradas_visitadas.append(paradadistancia)
   
    def stop_count(self):
        return len(self.__paradas_visitadas)
 
    def ver_paradas_visitadas(self):
        print(self.__paradas_visitadas)
 
    def distance_estimate(self):
        sumadistancia = sum(self.__paradas_visitadas)
        return sumadistancia
   
 
vehicle1 = PuclicVehicle("CC01")
vehicle1.visit_stop(100)
vehicle1.visit_stop(200)
vehicle1.visit_stop(300)
vehicle1.ver_paradas_visitadas()
print(vehicle1.distance_estimate())
print(vehicle1.stop_count())