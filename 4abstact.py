# Python program showing
# abstract base class work
from abc import ABC, abstractmethod

class Polygon(ABC):
    
    @abstractmethod
    def noofsides(self):
        pass

class Triangle(Polygon):
    
    # overriding abstract method
    def noofsides(self):
        print("I have 3 sides")

class Pentagon(Polygon):
    def noofsides(self):
        print("I have 5 sides")

class Hexagon(Polygon):
    def noofsides(self):
        print("I have 6 sides")

class Quadrilateral(Polygon):
    def noofsides(self):
        print("I have 4 sides")

# Driver code
R = Triangle()
R.noofsides()

K = Quadrilateral()
K.noofsides()

R = Pentagon()
R.noofsides()

K = Hexagon()
K.noofsides()