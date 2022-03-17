class Yin:
    pass

class Yang:

    def __del__(self):
        print ("Yang destruido")


yin = Yin()
yang = Yang()
yin_yang = yang

print(yang)
print(yang == yin_yang)
yang.__del__()

print("?")