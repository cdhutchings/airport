from initialisation import *
import pytest


def test_check_in1():

    # Checks that the passenger_instances list has increased by one when a new passenger is added

    before = len(Passenger.passenger_instances)
    legolas = Passenger("Legolas", "Greenleaf", 7433001)
    after = len(Passenger.passenger_instances)

    assert before + 1 == after

# Passenger can be checked in with name and passport number

def test_check_in2():

    # Checks that the passenger instance "sam" has all the correct attributes

    fname = "Samwise"
    lname = "Gamgee"
    passport = 2457296

    sam = Passenger(fname, lname, passport)
    results = [sam.fname, sam.lname, sam.passport]

    assert results == [fname, lname, passport]


# Create two specific passengers
def test_check_in3():

    # Checks that the last entry in the passenger instances list has all the correct information

    first = "Thorin"
    last = "Oakenshield"
    pport = 5683402

    thorin = Passenger(first, last, pport)
    results = [Passenger.passenger_instances[-1].fname, Passenger.passenger_instances[-1].lname, Passenger.passenger_instances[-1].passport]

    assert results == [first, last, pport]


def test_check_in4():

    # Same as above

    first = "Grima"
    last = "Wormtongue"
    pport = 5557393

    grima = Passenger(first, last, pport)
    results = [Passenger.passenger_instances[-1].fname, Passenger.passenger_instances[-1].lname, Passenger.passenger_instances[-1].passport]

    assert results == [first, last, pport]

# If passenger has either no name or passport number, get an error

def test_passenger_error():

    # Checks that an exception is raised when an attempt is made to create a passenger with no arguments

    with pytest.raises(Exception):
        error = Passenger()

# A plane can be created with a registration number
def test_aircraft_register():

    # Checks that the last instance of aircraft in the aircraft_instances list has the correct registration

    registration = "GD745"

    craft = Plane(registration)

    result = Aircraft.aircraft_instances[-1].reg

    assert registration == result

# A flight can be created without any specific information
def test_flight_creation():

    # Checks that the flight_instances list increased by 1 when a flight is created

    bef = len(Flight.flight_instances)
    test = Flight()
    aft = len(Flight.flight_instances)
    assert bef + 1 == aft

# Can add a plane
def test_aircraft_assign():

    # Checks that the last flight instance has the correct registration after use of the assign_aircraft method

    test = Flight()

    test.assign_aircraft(craft1)

    assert Flight.flight_instances[-1].aircraft.reg == "MD345"


# Can add an origin and destination
def test_flight_details():

    # Same as above but using the assign_journey method

    test = Flight()

    ori = "Hobbiton"
    des = "Mordor"
    num = "1DNSW"

    test.assign_journey(ori, des, num)

    assert [ori, des, num] == [Flight.flight_instances[-1].origin, Flight.flight_instances[-1].destination,
                               Flight.flight_instances[-1].flight_number]


def test_passenger_assign():

    # checks that the passenger list of a particular flight increases by 1 when a passenger is added to that flight

    prebook = len(mor_gon.passengers)
    legolas = Passenger("Legolas", "Greenleaf", 7433001)
    mor_gon.passengers.append(legolas)
    postbook = len(mor_gon.passengers)
    assert prebook + 1 == postbook

# The passenger list is a list of objects which are of the Passenger class
def test_passenger_list():

    # Checks that a flights passenger list /is/ a list

    assert type(mor_riv.passengers) == list

def test_passenger_type():

    # Checks that every instance of the passenger list is of class "Passenger"

    legolas = Passenger("Legolas", "Greenleaf", 7433001)
    mor_riv.check_in(legolas)

    for x in mor_riv.passengers:
        assert type(x) == Passenger



def test_list_flights():

    # Compares the count of flights created and the length of the flight instances list

    assert len(Flight.flight_instances) == Flight.count