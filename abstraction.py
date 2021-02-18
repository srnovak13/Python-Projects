from abc import ABC, abstractmethod

#Creating a class using the abstract method
class Animal(ABC):
    #Defining the method used by parent and child classes
     def habitat(self):
        print("Animals live on Earth")

    #Defining the abstract method
     @abstractmethod
     def dietary_needs(self):
        pass
#Creating a child class of "Animal"
class Human(Animal):
    #Utilizing the abstract method created from the parent class
    def dietary_needs(self):
        print("Most humans are omnivores")

#Creating an object that utilizes both child and parent methods
H = Human()
#Utilizing the child method
H.dietary_needs()
#Utilizing the parent method
H.habitat()
