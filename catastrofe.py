class Ciudades: 

    def __init__(self) -> None:
        self.ciudad1 = "Nueva York"
        self.ciudad2 = "Los Angeles"

class Edificios:

    def __init__(self) -> None:
        self.A = "Edificio A"
        self.B = "Edificio B"
        self.C = "Edificio C"
        self.lugar = Ciudades()
    
    def ubicacion(self):
        if self.lugar == "Nueva York":
            edif_afectados = [self.A, self.B]
        else:
            edif_afectados = self.C
        return edif_afectados

class Empleados:
    
    def __init__(self) -> None:
        self.empleado1 = "Sr. Martin"
        self.empleado2 = "Sr. Salim"
        self.empleado3 = "Sra. Xing"
        self.lugar_trabajo = Edificios()
    
    def lugar(self):
        if self.lugar_trabajo.ubicacion() == ["Edificio A", "Edificio B"]:
            trabajador_afectado = [self.empleado1, self.empleado2]
        else:
            trabajador_afectado = self.empleado3
        
        return trabajador_afectado
     
class Empresa:

    def __init__(self) -> None:
        self.propietario = "YooHoo"
        self.empleados = Empleados()
        self.edificios = Edificios()
        self.ciudades = Ciudades()
    
    def destruccion(self):
        catastrofe = int(input("¿Qué ciudad quieres destruir?: \n- Para destruir Nueva York pulse 1.\n- Para destruir Los Angeles pulse 2."))      
        while True:
            if catastrofe == 1:
                print("La ciudad a destruir es Nueva York.")
                ciudad = self.ciudades.ciudad1
                edificio = self.edificios.ubicacion()
                empleado = self.empleados.lugar()
                print("¡Se ha destruido " + str(ciudad) + "! Han sido afectados los edificios " + str(edificio[0]) + " y " + str(edificio[1]) + ". Lamentablemente, los empleados " + str(empleado[0]) + " y " + str(empleado[1]) + " han tenido que ser trasladados.")
            if catastrofe == 2:
                print("La ciudad a destruir es Los Angeles")
                ciudad = self.ciudades.ciudad2
                edificio = self.edificios.ubicacion()
                empleado = self.empleados.lugar()
                print("¡Se ha destruido " + str(ciudad) + "! Ha sido afectado el edificio " + str(edificio) + ". Lamentablemente, el empleados " + str(empleado) + " ha tenido que ser trasladado.")

            else:
                print("Parece que no ha introducido un valor válido, inténtelo de nuevo.")
