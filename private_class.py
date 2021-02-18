#Creating a protected class
class Protected:
    def __init__(self):
        #Assigning a value to a protected variable(encapsulating)
        self._protectedVar = 13
        obj = Protected()
        #Changing the value in the protected variable
        obj._protectedVar = 1980
        print(obj._protectedVar)

#Creating a private class
class Protected:
    def __init__(self):
        #Assigning a value to the private variable
        self.__privateVar = 1125
    def getPrivate(self):
        print(self.__privateVar)
    def setPrivate(self,private):
        self.__privateVar = private

obj = Protected()
#Accessing the private variable
obj.getPrivate()
#Changing the value of the private variable
obj.setPrivate(424)
obj.getPrivate()
    
