#Class methods are marked with a classmethod decorator.

#In class methods instead of self we use cls
class Rectangle:
    def __init__(self,width,hight):
        self.width = width
        self.hight = hight

    def calculate_area(self):
        return self.width * self.hight

    @classmethod
    def new_square(cls,side_length):
        return cls(side_length,side_length)


square = Rectangle.new_square(5)
print(square.calculate_area())

