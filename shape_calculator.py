class Rectangle:    
    def __init__(self, width = 0, height = 0):
        self.width = width
        self.height = height
    
    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if self.width < 50 and self.height < 50:
            picture = ""
            for i in range(self.height):
                for j in range(self.width):
                    picture += "*"
                picture += "\n"
            return picture
        return "Too big for picture."
        
    def get_amount_inside(self, shape):
        return self.get_area() // shape.get_area()

    def __str__(self):
        return "Rectangle(width={}, height={})".format(self.width, self.height)

class Square(Rectangle): 
    def __init__(self,side):
        super().__init__(side,side)
    def set_side(self,side):
        self.set_height(side)
        self.set_width(side)
    def __str__(self):
        return "Square(side={})".format(self.width)