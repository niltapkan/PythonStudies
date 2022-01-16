class animal:
    def __init__(self, color, speed, diet_type, name):
        self.color = color 
        self.speed = speed
        self.diet_type = diet_type 
        self.name = name

    def eat(self):
        return f'{self.name.title()} is eating.'

    def sleep(self):
        return f'{self.name.title()} is sleeping.'
    
    def move(self):
        return f'{self.name.title()} is moving.'

    
        