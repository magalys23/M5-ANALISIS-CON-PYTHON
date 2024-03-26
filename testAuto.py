from auto import*
# auto = Auto("Toyota", "Corolla", 2020)
# auto.mostrarInformacion()
# auto.actualizarKilometraje(30000)
# auto.realizarViaje(300)
# auto.estadoAuto()

print(" INFORMACIÓN ")
auto1 = Auto("Ford", "Fiesta", 2015, 40000) 
auto2 = Auto("Chevrolet", "Spark", 1998, 20000)

auto1.mostrarInformacion()
auto2.mostrarInformacion()
#Comparar kilometrajes
print(Auto.compararKilometraje(auto1,auto2))
#Validar año
print(f"El auto de marca {auto1.marca}",Auto.validarAnio(auto1.anio))
print(f"El auto de marca {auto2.marca}",Auto.validarAnio(auto2.anio))
#toyotaAuto
auto3=Auto.toyotaAuto(30000)
print(auto3.__dict__)
#autoAntiguo
autoAntiguo = Auto.autoAntiguo("Chevrolet", "Camaro")
autoAntiguo.mostrarInformacion()