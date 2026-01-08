# print(type(10))
# a: list[int]= [10, 20,30]
# a.append(10)

class Auto:
    # name: str = "BMW"
    # hp: int = 200
    # ms: int = 300

    def __init__(self, name: str, hp:int, speed: int)-> None:
        self.__name = name
        self.__hp = hp
        # self.ms = ms
        self.__speed = speed

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, val: int)->None:
        self.__speed = val

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, val: int)->None:
        self.__name = val

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, val: int)->None:
        self.__hp = val


    def __str__(self)->str:
        return "объект класса авто {self.name}"

    def calc_time(self, lenght:float)->float:
        return lenght / self.speed

    def __get_info(self)->None:
        print(f"Model: {self._name}")
        print(f"speed  {self._speed}")

    def calc_dist(self, time:float)->float:
        return self.speed * time

    def info(self):
        self.__get_info()


bmw: Auto = Auto("BMW", 300,120)
lada: Auto =Auto("Lada", 160,90)
print(bmw.speed)
print(bmw.name)
print(bmw.hp)
print(bmw)
# print(bmw.speed)
# print(bmw.calc_time(300),lada.calc_time(300) )
# print()
# print(bmw.calc_dist(2),lada.calc_dist(2) )

print()
# bmw.get_info()
# lada.get_info()
# bmw.get_info()
# Auto.get_info(bmw)
print()
# bmw.info()

# lada.name = "lada"
# bmw.name = "BMW"

# print(bmw.__dict__)
# print(bmw.name)
# print(bmw.hp)
# print(bmw.ms)

# print()

# print(lada.__dict__)
# print(lada.name)
# print(lada.hp)
# print(lada.ms)
