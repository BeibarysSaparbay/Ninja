class Person:
    def __init__(self ,name ,age):
        self.name = name
        self.age = age
    
def Myfunc(self):
    print("Hello my name is " + self.name + " and I'm " + str(self.age))

x = Person("Darik" , 18)
Myfunc(x)