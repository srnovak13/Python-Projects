# creating parent class
class Bird:
    name = ""
    habitat = ""
    
# creating methods for the 'bird' class
    def swim(self):
        print("There are many types of birds that can swim")

    def flight(self):
        print("Most birds can fly but some cannot")

# creating child class
class Penguin(Bird):
    can_swim = "yes"
    can_fly= "no"

# using polymorphism on parent class
    def flight(self):
        print("Penguins don't have wings, therefore cannot fly")

# creating second child glass
class Emu(Bird):
    neck_size = "long"
    tallest_rank = "second"

#using polymorphism on parent class
    def flight(self):
        print("Emus don't have wings, therefore cannot fly")
