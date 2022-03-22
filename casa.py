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