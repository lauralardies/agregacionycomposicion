class Empresa():

    def __init__(self) -> None:
        self.propietario = "YooHoo"

        self.empleado1 = "Sr. Martin"
        self.empleado2 = "Sr. Salim"
        self.empleado3 = "Sra. Xing"

        self.A = "A"
        self.B = "B"
        self.C = "C"

        self.ciudad = ""
        self.ciudad1 = "Nueva York"
        self.ciudad2 = "Los Angeles"

    def ubicacion_edificos(self):
        if self.ciudad == "Nueva York":
            edif_afectados = [self.A, self.B] # Tanto el edificio A como el edifico B están en Nueva York
        else:
            edif_afectados = self.C # El edificio C está en Los Ángeles

        return edif_afectados

    def ubicacion_empleados(self):
        if self.ubicacion_edificos() == [self.A, self.B]:
            trabajador_afectado = [self.empleado1, self.empleado2] # Estos dos empleado trabajan en los edificos A y B, en Nueva York
        else:
            trabajador_afectado = self.empleado3 # Este empleado trabaja en el edificio C, en Los Ángeles
        
        return trabajador_afectado
     
    def destruccion(self):
        catastrofe = int(input("¿Qué ciudad quieres destruir?: \n- Para destruir Nueva York pulse 1.\n- Para destruir Los Angeles pulse 2.\n"))      
        while True:
            if catastrofe == 1:
                print("La ciudad a destruir es Nueva York.")
                self.ciudad = self.ciudad1
                edificio = self.ubicacion_edificos()
                empleado = self.ubicacion_empleados()
                print("¡Se ha destruido " + str(self.ciudad) + "! Han sido afectados los edificios " + str(edificio[0]) + " y " + str(edificio[1]) + ". Lamentablemente, los empleados " + str(empleado[0]) + " y " + str(empleado[1]) + " han tenido que ser trasladados.")
                break
            if catastrofe == 2:
                print("La ciudad a destruir es Los Angeles")
                self.ciudad = self.ciudad2
                edificio = self.ubicacion_edificos()
                empleado = self.ubicacion_empleados()
                print("¡Se ha destruido " + str(self.ciudad) + "! Ha sido afectado el edificio " + str(edificio) + ". Lamentablemente, el empleado " + str(empleado) + " ha tenido que ser trasladado.")
                break

            else:
                print("Parece que no ha introducido un valor válido, inténtelo de nuevo.")