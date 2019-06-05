from passenger import *
from connection import *

db_connect = ConnMsSql("localhost,1433", "airport")

for x in db_connect.return_passengers():

    row = list(x)
    Passenger(row[0], row[1], row[2], row[3])

print("Passenger Name", "Passport No.")

for y in Passenger.passenger_instances:
    print(y.fname + ' ' +y.lname, y.passport)
