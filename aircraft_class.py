class Aircraft:

    aircraft_instances = []
    # Allows a staff member to register an aircraft with the airline

    def __init__(self, reg, type='', seats=0):
        Aircraft.aircraft_instances.append(self)
        self.reg = reg
        self.type = type
        self.seats = seats

