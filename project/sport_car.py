from project.car import Car


class SportsCar(Car):
    DEFAULT_FUEL_CONSUMPTION = 10

    def __init__(self, fuel, horse_power):
        super(Car).__init__(fuel, horse_power)