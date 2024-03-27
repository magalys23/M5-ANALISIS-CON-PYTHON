from laptos import *
from laptoGamer import*

class LaptopBusiness(Lapto):
    def __init__(self, marca, procesador, memoria, costo=500,almacenamiento=100, duracionBateria=4,impuesto=10):
        super().__init__(marca, procesador, memoria, costo, impuesto)
        self.almacenamiento = almacenamiento
        self.duracionBateria = duracionBateria
    def __str__(self):
        return f"Marca: {self.marca}\n Procesador: {self.procesador}\n Memoria: {self.memoria}\n Costo:{self.costo}\n Almacenamiento: {self.almacenamiento}\n Duración Bateria: {self.duracionBateria}\n Impuesto:{self.impuesto}\n"
    def realizarDiagnosticoSistema(self):
        resultadoBase = super().realizarDiagnosticoSistema()

        resultadosAdicionales = {
            "ALMACENAMIENTO": "OK" if self.almacenamiento >= 500 else "Aumentar almacenamiento",
            "DURACION DE BATERIA": "OK" if self.duracionBateria >= 8 else "Aumentar duración de batería",
            "CONECTIVIDAD DE RED": self.verificar_conectividad_red()
        }
        resultadoBase.update(resultadosAdicionales)
        return resultadoBase

    def verificar_conectividad_red(self):
        disponibilidadWifi = random.choice([True, False])
        accesoServidores = random.choice([True, False])
        latenciaRed = random.randint(1, 100)  # Simulando latencia en ms
        resultadosConectividad = {
            "DISPONIBILIDAD WIFI": disponibilidadWifi,
            "ACCESO SERVIDORES": accesoServidores,
            "LATENCIA DE RED": f"{latenciaRed}ms"
        }
        return resultadosConectividad