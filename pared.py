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