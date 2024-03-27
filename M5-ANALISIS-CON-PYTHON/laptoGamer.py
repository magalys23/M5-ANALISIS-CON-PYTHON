from laptos import*
class LaptoGamer(Lapto):
    def __init__(self, marca, procesador, memoria,targetaGrafica, costo=500, impuesto=10):
        super().__init__(marca, procesador, memoria, costo, impuesto)
        self.targetaGrafica=targetaGrafica
    def __str__(self):
        return f"Marca: {self.marca}\n Procesador: {self.procesador}\n Memoria: {self.memoria}\n Targeta Gráfica: {self.targetaGrafica}\n Costo:{self.costo}\n Impuesto:{self.impuesto}\n"

    def realizarDiagnosticoSistema(self):
        realizadoDiagnostico=super().realizarDiagnosticoSistema()
        resutadoJuegos=self.realizarDiagnosticoJuegos()
        realizadoDiagnostico["Resultado Juegos"]=resutadoJuegos
        return realizadoDiagnostico
    def realizarDiagnosticoJuegos(self):
        juegos=["FORNITE","COD","GTA"]
        resultados={}
        for juegos in self.targetaGrafica:
            fpsBase=30
            if "RTX" in self.targetaGrafica:
                fps=fpsBase*3
            elif "GTX" in self.targetaGrafica:
                fps=fpsBase*2
            else:
                fps=fpsBase
            resultados[juegos]=f"{fps} FPS"
        return resultados
    def realizarInformeUso(self):
        informe=super().realizarInformeUso()
        informe.update({
            "Tipo": "Gaming",
            "Uso Recomendado":"Juego de video",
            "Horas de uso":10,
            "Recomendaciones de software": ["Antivirus","VPN"]
        })
        return informe


    pass