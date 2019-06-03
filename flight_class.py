#from itertools import count

class Flight:

    # Needed to create a global list of classes as well as some kind of global counter.
    # Initially, I imported intertools to do the count, but that wasn't easy to use, so I found a different way
    # I found that using type(self) to increase the count was better. I only have a vague idea of how this is working,
    # so I need to do a little research.

    flight_instances = []
    #count = count(1)
    count = 0

    def __init__(self):
        self.flight_instances.append(self)
        #self.count = next(self.count)
        Flight.count += 1
        self.origin = ''
        self.destination = ''
        self.aircraft = ''
        self.passengers = []
        self.time = ''
        self.flight_number = ''

    def __del__(self):
        type(self).count -= 1

        # To add an aircraft to a particular trip

    def assign_aircraft(self, aircraft):
        self.aircraft = aircraft

        # Adds the origin, destination and the flight number to the trip

    def assign_journey(self, origin, destination, flight_number):
        self.origin = origin
        self.destination = destination
        self.flight_number = flight_number

        # Allows the receptionist to add a passenger to that particular flight

    def check_in(self, passenger):
        self.passengers.append(passenger)

        # Allows staff to specify a take off time for that particular flight

    def assign_time(self):
        pass