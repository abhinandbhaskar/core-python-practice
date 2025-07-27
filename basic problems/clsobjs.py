# Syntax


# class ClassName:
#     "DocString"
#     class Varibles
#     method Definitions

# class ClassName:
#     "DocString"
#     class Variables
#     method Definitions


# class ClassName:
#     "DocString"
#     class Variables
#     method defintions


# class Rectangle:
#     no_of_rectangle = 0
#     def __init__(self,l,b):
#         self.length = l
#         self.breadth = b
#         Rectangle.no_of_rectangle+=1
#     def getArea(self):
#         return self.length * self.breadth
#     def getPerimeter(self):
#         return 2*(self.length+self.breadth)
    
# r1=Rectangle(10,20)
# r2=Rectangle(5.25,6)

# print(r1.getArea())
# print(r1.getPerimeter())
# print(r2.getArea())
# print(r2.getPerimeter())


# class Rectangle:
#     no_of_reactangle = 0
#     def __init__(self,l,b):
#         self.length=l
#         self.breadth=b
#         Rectangle.no_of_reactangle+=1
#     def getArea(self):
#         return self.length * self.breadth
#     def getPerimeter(self):
#         return 2*(self.length+self.breadth)
    
# r1=Rectangle(10,20)
# r2=Rectangle(5,6)

# print(r1.getArea())
# print(r1.getPerimeter())
# print(r2.getArea())
# print(r2.getPerimeter())
# print(Rectangle.no_of_reactangle)
    



# class Rectangle:
#     no_of_rectangle = 0
#     def __init__(self,l,b):
#         self.length=l
#         self.breadth=b
#         Rectangle.no_of_rectangle+=1
#     def getArea(self):
#         return self.length*self.breadth
#     def getPerimeter(self):
#         return 2*(self.length+self.breadth)
    
# r1=Rectangle(20,30)
# r2=Rectangle(55,66)
# print(r1.getArea())
# print(r1.getPerimeter())
# print(r2.getArea())
# print(r2.getPerimeter())

# print(Rectangle.no_of_rectangle)
# print("L",getattr(r1,'length'))



# class Rectangle:
#     "Class for rectangle"
#     no_of_rectangles=0
#     def __init__(self,l,b):
#         self.length=l
#         self.breadth=b
#         self.__name="Rectangle"+str(self.no_of_rectangles+1)
    
#     def getArea(self):
#         return self.length * self.breadth
#     def getPerimeter(self):
#         return 2*(self.length+self.breadth)
    
#     def displayRectangle(self):
#         print("Rectangle",self.__name)
#         print("Length",self.length)
#         print("Breadth",self.breadth)

# r1=Rectangle(10,20)
# r1.displayRectangle()   
# print(r1.length)     


# inheritance

# class child_classname(base_classname):
#     Docstring
#     Child Class Varibles
#     Child Method Definitions


# class child_classname(base_classname):
#     child Class Variables
#     Child Method Definitions

# class child_classname(base_classname):
#     child class variables
#     child method definitions

class BaseClass1:
    def __init__(self,l,b):
        self.length=l
        self.breadth=b
    def getArea(self):
        return self.breadth*self.length
    def getPerimeter(self):
        return 2*(self.breadth+self.length)
    
class DerivedClass1(BaseClass1):
    def DisplayHere(self):
        print("Hello guys")
obj1=DerivedClass1(20,10)
print(obj1.getArea())
print(obj1.getPerimeter())
print(obj1.DisplayHere())