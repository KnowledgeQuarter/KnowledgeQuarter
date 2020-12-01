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


#SQL query to select all the data in the test
sql = "SELECT * FROM tke_db"

#Execute query
cursor.execute(sql)


result = cursor.fetchall()
cursor.close()
cnxn.commit() 

#Print the data in the database, to check if the new data is there
#Now as a  list, but can easily be converted to a dataframe and thus a csv file 
print(result)