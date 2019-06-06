from passenger import *
from connection import *

db_connect = ConnMsSql("localhost,1433", "airport")

azog = Passenger(7, 'Azog', 'the Goblin', 6774833)

try:
    db_connect.insert_passenger(azog.id, azog.fname, azog.lname, azog.passport)

except pyodbc.ProgrammingError:

    print("There has been an issue committing your entry to the database. Please check how your function is formatted.")