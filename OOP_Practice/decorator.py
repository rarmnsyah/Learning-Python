# private variable (__.(variable))
# protected variable (_.(variable))
class hero:
    __jumlah = 0

    def __init__(self, name, health, attack):
        # private variable
        self.__name = name
        self.__health = health
        self.__attack = attack
        hero.__jumlah += 1

    # getter
    def getName(self):
        return self.__name

    # contoh getter yang lebih simpel (bisa dirubah)
    @property
    def attack(self):
        pass
    
    @attack.getter
    def attack(self):
        return self.__attack

    # static method (decorator), getter untuk variable -
    # yang menempel ke objek dan ke class
    @staticmethod
    def getJumlah2():
        return hero.__jumlah

    # properti (menganggap method sebagai sebuah variable) / getter vers lain
    @property
    def info(self):
        return "name : {} \nhealth : {}\nattack : {}".format(self.__name, self.__health, self.__attack) 

    # setter
    def diserang(self,damage_diterima):
        self.__health -= damage_diterima

    @attack.setter
    def attack(self, input):
        self.__attack = input

antimage = hero('antimage', 100, 20)
antimage.diserang(50)

# cara untuk mengakses private variable
print(antimage.getName())

# contoh error dalam mengakses private variable
# print(antimage.__name) -> error karena variablenya diprivate

gardevoir = hero('gardevoir', 50, 20)
print(hero.getJumlah2())

print(gardevoir.info)
print(gardevoir.attack)
gardevoir.attack = 123
print(gardevoir.attack)

