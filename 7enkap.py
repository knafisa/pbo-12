class Base:
    def __init__(self):

        self._c = "pbo b"

class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        print("panggil protected number: ")
        print(self._c)

obj1 = Base()
print(obj1._c)