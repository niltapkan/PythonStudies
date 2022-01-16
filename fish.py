from animal import Animal

class Fish(Animal):
    def __init__(self, color, speed, diet_type, name):
        super().__init__(color, speed, diet_type, name)

    def __str__(self):
        return f'{self.color} {self.name} {self.speed} '