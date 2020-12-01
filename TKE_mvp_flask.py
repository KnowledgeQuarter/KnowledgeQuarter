# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 17:30:15 2020

@author: Kirsch
"""

#Import the necessary libraries
from flask import Flask, render_template, g, redirect, url_for, request, send_file
import mysql.connector
from mysql.connector.constants import ClientFlag


#Create the web application
app = Flask(__name__)


#Initialize the web app first page
@app.route("/")
def index():
    return render_template("mvp_backend.html")


#Function recuperating the info from the form and adding it to the database
@app.route("/", methods=['GET', 'POST'])
def redirection():

    #Get the data from the form
    data = request.form
    print(data)

    #Get the keys from the form - they will correspond to the columns in the database
    key = str(list(data.keys())).replace("[","(").replace("]",")").replace("'","")
    print(key)

    #Get the logging information
    value = str(list(data.values())).replace("[","(").replace("]",")")
    print(value)

    #Configure the information to establish the connection to the database
    config = {
        'user': 'root',
        'password': 'Piloupistache1',
        'host': '35.187.22.101',
        'client_flags': [ClientFlag.SSL],
        'ssl_ca': 'ssl/server-ca.pem',
        'ssl_cert': 'ssl/client-cert.pem',
        'ssl_key': 'ssl/client-key.pem'
    }




    config['database'] = 'testdb'  # add new database to config dict

    #Establish our connection
    cnxn = mysql.connector.connect(**config)
    cursor = cnxn.cursor()

    #Create the SQL query
    sql = "INSERT INTO delivery_logger " + key + " VALUES " + value

    #Execute the SQL query
    cursor.execute(sql)
    cnxn.commit()

    #Redirect the right html page
    return redirect(url_for(".thank"))


#Load the thank you html page
@app.route("/thanks")
def thank():
    return render_template("thankslog.html")

#Button to go back to logging page
@app.route("/thanks", methods=['GET', 'POST'])
def redirection_index():
    return redirect(url_for(".index"))

if __name__ == "__main__":
    # execute only if run as a script
    app.run()
