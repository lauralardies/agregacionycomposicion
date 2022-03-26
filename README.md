# agregacionycomposicion

Mi dirección de GitHub para este repositorio es la siguiente: [GitHub](https://github.com/lauralardies/agregacionycomposicion)
https://github.com/lauralardies/agregacionycomposicion

Ejercicio 1:
```
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

```

Ejercicio 2:
```
class Yin:
    pass

class Yang:

    def __del__ (self):
        print ("Yang destruido")


yin = Yin()
yang = Yang()
yin.yang = yang

print(yang)
print(yang == yin.yang)
del(yin.yang)
del(yang)
print("?")

# El problema que teníamos era que había dos instancias de la clase Yang. Sólo borrábamos una de ellas y por lo tanto la clase
# Yang todavía existía en la otra instancia. Al terminar el programa se borraba esa segunda instancia y cuando ya no había más 
# instancias de la clase Yang era cuando se mostraba el mensaje. El problema se arregla borrando las dos instancias de Yang.
```

Ejercicio 3:
```
class Cristal:
    def __init__(self, superficie):
        self.__superficie = superficie

    def superficie(self):
        return self.__superficie

class Pared:
    def __init__(self, orientacion):
        self.__orientacion = orientacion
        self.__ventanas = []

    def ventanas(self):
        return self.__ventanas

    def superficie_cristal(self):
        superficie = 0
        for ventana in self.ventanas():
            superficie += ventana.superficie()
        return superficie

class Ventana:
    def __init__(self, pared, superficie):
        self.__pared = pared
        self.__cristal = Cristal(superficie)
        self.__pared.ventanas().append(self)

    def superficie(self):
        return self.__cristal.superficie()

class Casa:
    def __init__(self, paredes):
        self.__paredes = paredes

    def paredes(self):
        return self.__paredes

    def superficie_cristal(self):
        superficie = 0
        for pared in self.paredes():
            superficie += pared.superficie_cristal()
        return superficie

pared_norte = Pared("NORTE")
pared_oeste = Pared("OESTE")
pared_sur = Pared("SUR")
pared_este = Pared("ESTE")

ventana_norte = Ventana(pared_norte, 0.5)
ventana_oeste = Ventana(pared_oeste, 1)
ventana_sur = Ventana(pared_sur, 2)
ventana_este = Ventana(pared_este, 1)

casa = Casa([pared_norte, pared_oeste, pared_sur, pared_este])

print(casa.superficie_cristal())

class ParedCortina(Pared):
    def __init__(self, orientacion, superficie):
        Pared.__init__(self, orientacion)
        self.__cristal = Cristal(superficie)

    def superficie_cristal(self):
        return self.__cristal.superficie()

pared_cortina = ParedCortina("SUR", 10)

casa = Casa([pared_norte, pared_oeste, pared_cortina, pared_este])

print(casa.superficie_cristal())
```
