from laptos import Lapto
from laptoGamer import*
from laptoBussines import*
laptoPepito=Lapto("Lenovo","i7",32)
laptoMaria=Lapto("Lenovo","i7",32,600)


#__dict__ permite observar el contenido del objeto
# print(laptoPepito.__dict__)
# print(laptoPepito.valorFinal())
# # print(f"El valor de descuento: {laptoPepito.valorDescuento(10)}")
# for numero in range(1,1000):
#     asusLapto=Lapto.asusLapto(numero)
#     print(asusLapto.__dict__)
#print(Lapto.compararCosto(laptoPepito,laptoMaria))

laptoJuanito=LaptoGamer("ASUS","i7",4,"RTX 8GA")
# print(laptoJuanito.realizarDiagnosticoSistema())

# laptopEmpresarial = LaptopBusiness("Lenovo", "i7", 16) 
# diagnostico = laptopEmpresarial.realizarDiagnosticoSistema()

# print(diagnostico)
def imprimirInforme(Lapto):
    informe=Lapto.realizarInformeUso()
    for clave,valor in informe.items():
        print(f"{clave}: {valor}")
    print("\n")

print("PEPITO")
imprimirInforme(laptoPepito)
print("JUANITO")
imprimirInforme(laptoJuanito)    