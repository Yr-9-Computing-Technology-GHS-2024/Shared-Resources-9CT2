from abc import ABC, abstractmethod
#Classes are object constructors or blueprints.

#Creating a basic class
class myclass:
    x = 5

#Creating an object in a class
p1 = myclass()
print(p1.x)

#When creating more complex classes you need to use specialized function commands such as __init__
class Person:
    def __init__(self, height, name, age):
        self.height = height
        self.name = name
        self.age = age

#Creating full blueprinted classes need to define the perameters in the __init__ command
person1 = Person(170,"jim",20)
print(person1.age)
print(person1.height)
print(person1.age)

#class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.
class object():
    pass

#Classes can also inherit from other classes
class Student(Person):
    def __init__(self, height, name, age):
        super().__init__( height, name, age)
        self.graduationyear = 2019

#Classes can store information about an object
class BankAccount:
    def __init__(self, Owner_name):
        self._Owner_name = Owner_name

    def getname(self):
        return self._Owner_name
    
#Class atributes can be altered
    def set_name(self, new_name):
        if isinstance(new_name, str):
            self._Owner_name = new_name
        else:
            raise ValueError("Name must be a string.")

Object1 = BankAccount("John Smith")
Object1.set_name("John Doe")
print(Object1.getname())

#Abstract classes can be used as a base for other classes 
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass
	
    @abstractmethod
    def volume(self):
        pass
	
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
		
    def perimeter(self):
        return 2 * 3.14 * self.radius
	
    def area(self):
        return 3.14 * self.radius ** 2
     
    def volume(self):
        return 0.75*3.14*self.radius**3
