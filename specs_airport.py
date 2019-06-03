from initialisation import *

print("Receptionist can check-in a passenger")
before = len(Passenger.passenger_instances)
legolas = Passenger("Legolas", "Greenleaf", 7433001)
after = len(Passenger.passenger_instances)
print(before + 1 == after)
print("///////////////////")


print("Receptionist can assign a passenger to a flight")
prebook = len(mor_gon.passengers)
mor_gon.passengers.append(legolas)
postbook = len(mor_gon.passengers)
print(prebook + 1 == postbook)
print("///////////////////")


print("Receptionist can list all existing flights")
#print(len(mor_gon.flight_instances))
#print(roh_gon.count)
print(len(Flight.flight_instances) == Flight.count)

