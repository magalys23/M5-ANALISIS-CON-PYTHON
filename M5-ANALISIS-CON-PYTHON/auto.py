class Auto:
    def __init__(self,marca,modelo,anio,kilometraje=0):
        self.marca=marca
        self.modelo=modelo
        self.anio=anio
        self.kilometraje=kilometraje
    def mostrarInformacion(self):
        print(f"El auto es de marca {self.marca} y su modelo es {self.modelo} y del año {self.anio}")  
    def actualizarKilometraje(self,nuevoKilometraje):
        if nuevoKilometraje<self.kilometraje:
            print(f"El kilometraje no se puede reducir")
        else:
            self.kilometraje = nuevoKilometraje
    def realizarViaje(self,km):
        if km<0:
            print("La cantidad de kilómetros debe ser positiva.")
        else:
            self.kilometraje=self.kilometraje+km
    def estadoAuto(self):
        if self.kilometraje<20000:
            print("Estoy como nuevo")
        elif self.kilometraje>20000 and self.kilometraje<100000:
            print("Ya estoy usado")
        elif self.kilometraje>100000:
            print("¡Ya déjame descansar por favor!")
    #Método estático
    @staticmethod
    def compararKilometraje(auto1,auto2):
        if auto1.kilometraje==auto2.kilometraje:
            return "Los autos tiene el mismo kilometraje"
        else:
            return "Los autos no tienen el mismo kilometraje"
    #Método clase
    @classmethod
    def toyotaAuto(cls,kilometraje):
        marca="Toyota"
        modelo="Nuevo"
        anio=2024
        return cls(marca,modelo,anio,kilometraje)
    @classmethod
    def autoAntiguo(cls, marca, modelo):
        return cls(marca, modelo, 1990)
    @staticmethod
    def validarAnio(anio):
        if anio >= 2000 and anio <= 2024:
            return "es un auto de la decada de los 2000"
        else:
            return "es un auto de la decada de los años 90"
