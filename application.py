# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 17:09:11 2020

@author: Kirsch
"""

from flask import Flask, render_template, g, redirect, url_for, request, send_file
import pymysql




#Create the web application
application = Flask(__name__)


#Initialize the web app first page
@application.route("/")
def index():

    return render_template("mvp_backend.html")


#Function recuperating the info from the form and adding it to the database
@application.route("/", methods=['GET', 'POST'])
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

    db = pymysql.connect("database-2.cotwcdzhuuco.us-east-2.rds.amazonaws.com", 'admin', 'Piloupistache1', port = 3306)
    cursor = db.cursor()
    cursor.connection.commit()
    sql = '''use tketest'''
    cursor.execute(sql)
    
    
    sql = "INSERT INTO delivery_logger " + key + " VALUES " + value

    cursor.execute(sql)
    db.commit()
    db.close()

    #Redirect the right html page
    return redirect(url_for(".thank"))


#Load the thank you html page
@application.route("/thanks")
def thank():
    return render_template("thankslog.html")

#Button to go back to logging page
@application.route("/thanks", methods=['GET', 'POST'])
def redirection_index():
    return redirect(url_for(".index"))



if __name__ == "__main__":
    # execute only if run as a script
    application.run()

