class ParedCortina(Pared):
    def __init__(self, orientacion, superficie):
        Pared.__init__(self, orientacion)
        self.__cristal = Cristal(superficie)

    def superficie_cristal(self):
        return self.__cristal.superficie()