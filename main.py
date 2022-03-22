from yin import Yin
from yang import Yang
from pared import Pared
from ventana import Ventana
from casa import Casa

# Ejercicio 2
print("\nEjercicio 2:\n")

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

# Ejercicio 3:
print("\nEjercicio 3:\n")

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

from pared_cortina import ParedCortina

pared_cortina = ParedCortina("SUR", 10)

casa = Casa([pared_norte, pared_oeste, pared_cortina, pared_este])

print(casa.superficie_cristal())