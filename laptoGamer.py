from laptos import*
class LaptoGamer(Lapto):
    def __init__(self, marca, procesador, memoria,targetaGrafica, costo=500, impuesto=10):
        super().__init__(marca, procesador, memoria, costo, impuesto)
        self.targetaGrafica=targetaGrafica
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

    pass