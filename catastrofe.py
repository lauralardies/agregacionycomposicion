class Ciudades: 

    def __init__(self) -> None:
        self.ciudad1 = "Nueva York"
        self.ciudad2 = "Los Angeles"

class Edificios:

    def __init__(self) -> None:
        self.A = "Edificio A"
        self.B = "Edificio B"
        self.C = "Edificio C"
    
class Empleados:
    
    def __init__(self) -> None:
        self.empleado1 = "Sr. Martin"
        self.empleado2 = "Sr. Salim"
        self.empleado3 = "Sra. Xing"
        self.lugar_trabajo = Edificios()
    
class Empresa(Edificios, Empleados):

    def __init__(self) -> None:
        super(Edificios, Empleados).__init__()
        self.propietario = "YooHoo"
        self.empleados = Empleados()
        self.edificios = Edificios()
        self.ciudades = Ciudades()
    
    def ubicacion_edificos(self):
        if self.ciudades == "Nueva York":
            edif_afectados = [self.A, self.B]
        else:
            edif_afectados = self.C
        return edif_afectados

    def ubicacion_empleados(self):
        if self.ubicacion_edificos() == ["Edificio A", "Edificio B"]:
            trabajador_afectado = [self.empleado1, self.empleado2]
        else:
            trabajador_afectado = self.empleado3
        
        return trabajador_afectado
     
    def destruccion(self):
        catastrofe = int(input("¿Qué ciudad quieres destruir?: \n- Para destruir Nueva York pulse 1.\n- Para destruir Los Angeles pulse 2.\n"))      
        while True:
            if catastrofe == 1:
                print("La ciudad a destruir es Nueva York.")
                ciudad = self.ciudades.ciudad1
                edificio = self.ubicacion_edificos()
                empleado = self.ubicacion_empleados()
                print("¡Se ha destruido " + str(ciudad) + "! Han sido afectados los edificios " + str(edificio[0]) + " y " + str(edificio[1]) + ". Lamentablemente, los empleados " + str(empleado[0]) + " y " + str(empleado[1]) + " han tenido que ser trasladados.")
                break
            if catastrofe == 2:
                print("La ciudad a destruir es Los Angeles")
                ciudad = self.ciudades.ciudad2
                edificio = self.ubicacion_edificos()
                empleado = self.ubicacion_empleados()
                print("¡Se ha destruido " + str(ciudad) + "! Ha sido afectado el edificio " + str(edificio) + ". Lamentablemente, el empleados " + str(empleado) + " ha tenido que ser trasladado.")
                break

            else:
                print("Parece que no ha introducido un valor válido, inténtelo de nuevo.")

while True:
    decision = input("¿Quieres crear una catástrofe? [Y]/N: ")
    decision = decision.capitalize()
    if decision == "N":
        exit()
    else:
        inicio = Empresa()
        catastrofe = inicio.destruccion()