from aircraft_class import Aircraft

class Plane(Aircraft):

    def __init__(self, reg, seats=0):
        super().__init__(reg, seats)
        self.wing_number = 2