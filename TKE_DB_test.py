# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 16:22:47 2020

@author: Kirsch
"""

####################
#Test the database #
####################

#Import the used libraries
import mysql.connector
from mysql.connector.constants import ClientFlag

#Configure the connection
config = {
    'user': 'root',
    'password': 'Piloupistache1',
    'host': '35.187.22.101',
    'client_flags': [ClientFlag.SSL],
    'ssl_ca': 'ssl/server-ca.pem',
    'ssl_cert': 'ssl/client-cert.pem',
    'ssl_key': 'ssl/client-key.pem'
}

#Establish our connection
cnxn = mysql.connector.connect(**config)

config['database'] = 'testdb'  # add new database to config dict
cnxn = mysql.connector.connect(**config)
cursor = cnxn.cursor()

# Create a table called delivery_logger with the correct column headers
cursor.execute("CREATE TABLE delivery_logger ("
               "company_name VARCHAR(255),"
               "time_in DATETIME,"
               "time_out DATETIME,"
               "parking_location ENUM('street', 'restricted'),"
               "delay ENUM('none', 'small', 'medium', 'large'),"
               "bound ENUM('inbound', 'outbound'),"
               "carrier_name VARCHAR(255),"
               "vehicle_type ENUM('pedestrian', 'bicycle', 'motorbike', 'car', 'van', 'lorry'),"
               "vehicle_registration_number VARCHAR(7),"
               "fuel ENUM('petrol', 'diesel', 'electric', 'hybrid'),"
               "vehicle_origin VARCHAR(255),"
               "previous_locations INT(255),"
               "following_locations INT(255),"
               "personal_delivery BOOL,"
               "department VARCHAR(255),"
               "number_suppliers INT(255),"
               "type ENUM('medical', 'office', 'catering'),"
               "size ENUM('box', 'letter', 'package', 'pallet'))")

cnxn.commit()

# Populate the table with dummy data
query = ("INSERT INTO delivery_logger VALUES ('Frances Crick', '2020-11-28 09:11:11',"
         "'2020-11-28 10:01:55', 'restricted', NULL, 'inbound', 'Fed Ex', 'van',"
         "'BF856X8', 'petrol', 'Birmingham', 3, 9, 0, 'IT', 1, 'office', 'box')")
cursor.execute(query)
cnxn.commit()

# More dummy data
query = ("INSERT INTO delivery_logger VALUES ('UCL', '2020-11-29 15:18:01',"
         "'2020-11-29 16:00:23', 'restricted', NULL, 'inbound', 'Royal Mail', 'van',"
         "'JS864G6', 'petrol', 'London', 1, 7, 0, 'Procurement', 2, 'office', 'pallet')")
cursor.execute(query)
cnxn.commit()

#SQL query to select all the data in the test
sql = "SELECT * FROM delivery_logger"

#Execute query
cursor.execute(sql)
result = cursor.fetchall()
cursor.close()
cnxn.commit()

#Print the data in the database, to check if the new data is there
#Now as a  list, but can easily be converted to a dataframe and thus a csv file
print(result)
