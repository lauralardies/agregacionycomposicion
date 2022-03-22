class Ventana:
    def __init__(self, pared, superficie):
        self.__pared = pared
        self.__cristal = Cristal(superficie)
        self.__pared.ventanas().append(self)

    def superficie(self):
        return self.__cristal.superficie()