from aircraft_class import Aircraft

class Helicopter(Aircraft):

    def __init__(self, reg, seats = 0):
        super().__init__(self, reg, seats)
        self.rotor_number = 4

