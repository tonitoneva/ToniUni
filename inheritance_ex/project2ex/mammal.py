from inheritance_ex.project2ex.animal import Animal


class Mammal(Animal):
    def __init__(self, name):
        super().__init__(name)