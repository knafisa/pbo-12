class Base:
    def __init__(self):
        self.a = "pbo b"
        self.__c = "pbo b"

class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        print("panggil protected number: ")
        print(self.__c)

obj1 = Base()
print(obj1.a)