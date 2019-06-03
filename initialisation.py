from aircraft_class import *
from flight_class import *
from passenger_class import *

craft1 = Aircraft("MD345", 150)
craft2 = Aircraft("RV111", 200)
craft3 = Aircraft("HT925", 100)

mor_riv = Flight()
hob_riv = Flight()
mor_gon = Flight()
roh_gon = Flight()

mor_riv.assign_aircraft(craft1)
hob_riv.assign_aircraft(craft2)
mor_gon.assign_aircraft(craft1)
roh_gon.assign_aircraft(craft3)

mor_riv.assign_journey("Mordor", "Rivendell", "MOR585")
hob_riv.assign_journey("Hobbiton", "Rivendell", "RIV112")
mor_gon.assign_journey("Mordor", "Gondor", "MOR660")
roh_gon.assign_journey("Rohan", "Gondor", "HOB434")

bilbo = Passenger("Bilbo", "Baggins", 7341195)
mor_riv.check_in(bilbo)

elrond = Passenger("Elrond", "Half-Elven", 1000001)
mor_riv.check_in(elrond)

gimli = Passenger("Gimli", "son of Gloin", 4459226)
roh_gon.check_in(gimli)

tom = Passenger("Tom", "Bombadil", 1000000)
mor_gon.check_in(tom)

