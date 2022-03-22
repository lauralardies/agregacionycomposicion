from yin import Yin
from yang import Yang

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