# agregacionycomposicion

Mi dirección de GitHub para este repositorio es la siguiente: [GitHub](https://github.com/lauralardies/agregacionycomposicion)
https://github.com/lauralardies/agregacionycomposicion

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
