class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled
    pass

class Circle(Shape):
    def __init__(self, radius, color, is_filled):
        super().__init__(color, is_filled)
        self.radius = radius
        print(f"Dein kreis hat die Farbe {self.color} und ist gefüllt: {self.is_filled} und hat einen Radius von {self.radius}")

    @staticmethod
    def printing():
        print(f"{"lol"} ist so toll")
class Square(Shape):
    def __init__(self, width, color, is_filled):
        super().__init__(color, is_filled)
        self.width = width
        print(f"Dein Square hat die Farbe {self.color} und ist gefüllt: {self.is_filled} und hat einen Radius von {self.width}")

class Traingle(Shape):
    def __init__(self, width, height, color, is_filled):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height
        print(f"Dein Traingle hat die Farbe {self.color} und ist gefüllt: {self.is_filled} und hat einen Radius von {self.width} und die Höhe von {self.height}")

circle = Circle("40cm", "Red", True)
square = Square("30cm", "Green", False)
triangle = Traingle("15cm","10cm", "Blue",  True)




Circle.printing()