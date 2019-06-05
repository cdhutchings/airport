from passenger import *
from connection import *

db_connect = ConnMsSql("localhost,1433", "airport")


db_connect.query("INSERT INTO passengers "
                 "VALUES (5, 'Gimli', 'Gloin', 4883294);")
db_connect.docker_con.commit()
