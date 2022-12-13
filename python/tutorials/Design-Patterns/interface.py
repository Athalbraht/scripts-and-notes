# Interface

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass
        
    @abstractmethod
    def stop(self):
        pass
    
    def open_doors(self):
        print("Doors opened")

class Interface(ABC):
    @abstractmethod
    def beep(self): pass

class Car(Vehicle):
    
    #overriding abstract method
    def go(self):
        print("Gone")
    
    #overriding abstract method
    def stop(self):
        print("Stopped")

class CarC(Vehicle, Interface):
    
    #overriding abstract method
    def go(self):
        print("Audi: Gone")
    
    #overriding abstract method
    def stop(self):
        print("Audi: Stopped")

    def beep(self): print('beeeeep')
        
Bmw = Car()
Bmw.open_doors()

audi = CarC()
audi.go()
audi.beep()
