from inheritance_ex.project2ex.mammal import Mammal


class Bear(Mammal):
    def __init__(self, name):
        super().__init__(name)