from passenger import *
from connection import *

db_connect = ConnMsSql("localhost,1433", "airport")

faramir = Passenger("6", 'Faramir', 'Denethorson', 2734419)


db_connect.query(f"INSERT INTO passengers "
                 f"VALUES ({faramir.id}, '{faramir.fname}', '{faramir.lname}', {faramir.passport});")
db_connect.docker_con.commit()
