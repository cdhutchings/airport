class Passenger:

    # Initialisation function

    passenger_instances = []

    def __init__(self, fname, lname, passport):
        self.passenger_instances.append(self)
        self.fname = fname.title()
        self.lname = lname.title()
        self.passport = passport

    def fullname(self):
        return fname + ' ' + lname