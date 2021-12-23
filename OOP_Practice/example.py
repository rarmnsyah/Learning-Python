class hero:
    def __init__(self, name, health, attack):
        self.__name = name
        self.__health = health
        self.__attack = attack

    def serang(self, lawan):
        print("{} Menyerang {} dengan damage sebesar {}".format(self.__name, lawan.__name, self.__attack))
        lawan.diserang(self.__attack,self)

    def diserang(self, damageDiterima, lawan):
        print("{} diserang oleh {} dengan damage sebesar {}".format(self.__name, lawan.__name, damageDiterima))
        self.__health -= damageDiterima
        print("Darah {} tersisa sebesar {}".format(self.__name, self.__health))

antimage = hero('antimage', 100, 20)
tian = hero('tian', 100,50)

# print(antimage.__name)
antimage.serang(tian)
