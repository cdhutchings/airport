class Passenger:

    # Initialisation function

    passenger_instances = []

    def __init__(self, id,  fname, lname, passport):
        Passenger.passenger_instances.append(self)
        self.id = id
        self.fname = fname.title()
        self.lname = lname.title()
        self.passport = passport

    def fullname(self):
        return fname + ' ' + lname