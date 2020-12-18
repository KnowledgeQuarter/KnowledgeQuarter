# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 17:09:11 2020

@author: Kirsch
"""

from flask import Flask, render_template, g, redirect, url_for, request, send_file
import pymysql
import pandas as pd

# Create the web application
application = Flask(__name__)

# Initialize the web app's first page
@application.route("/")
def index():
    return render_template("index.html")

# Load the template for the delivery logger
@application.route("/delivery_logger")
def delivery_logger():
    return render_template("delivery_logger.html")

# Load the template for the settings page
@application.route("/settings")
def settings():
    return render_template("settings.html")

# Load the template for the admin page
@application.route("/admin")
def admin():
    return render_template("admin.html")

# Load the template for the settings page
@application.route("/settings", methods=['GET', 'POST'])
def get_csv():

    db = pymysql.connect('knowledge-quarter-db.cnq2qddxvg55.us-east-2.rds.amazonaws.com', 'admin', 'Kn0w!3dg$_Qu&r3r', port = 3306)
    cursor = db.cursor()
    cursor.connection.commit()
    sql = '''use kq_contracts_and_logger'''
    cursor.execute(sql)

    sql = '''select * from delivery_logger'''
    cursor.execute(sql)
    data = cursor.fetchall()

    df = pd.DataFrame(list(data), columns = ['time_in','time_out',
                                          'delivery_location', 'delay', 'bound',
                                          'carrier', 'vehicle_type',
                                          'vehicle_registration_number',
                                          'personal_delivery',
                                          'department',
                                          'number_packages',
                                          'type',
                                          'size'])

    df.to_csv('outputs/your_data.csv', sep = ',' )


    return send_file('outputs/your_data.csv',
        mimetype='text/csv',
        attachment_filename='your_data.csv',
        as_attachment=True)



# Function to fetch the info from the form and add it to the database
@application.route("/delivery_logger", methods=['GET', 'POST'])
def form():

    # Get the data from the form
    data = request.form
    print(data)

    # Get the keys from the form - they will correspond to the columns in the database
    key = str(list(data.keys())).replace("[","(").replace("]",")").replace("'","")
    print(key)

    # Get the logging information
    value = str(list(data.values())).replace("[","(").replace("]",")")
    print(value)

    db = pymysql.connect('knowledge-quarter-db.cnq2qddxvg55.us-east-2.rds.amazonaws.com', 'admin', 'Kn0w!3dg$_Qu&r3r', port = 3306)
    cursor = db.cursor()
    cursor.connection.commit()
    sql = '''use kq_contracts_and_logger'''
    cursor.execute(sql)


    sql = "INSERT INTO delivery_logger " + key + " VALUES " + value

    cursor.execute(sql)
    db.commit()
    db.close()

    # Redirect to the same html page
    return redirect(url_for("form"))


@application.route("/", methods=['GET', 'POST'])
def login():
    # Get the data from the form
    if request.method == 'POST':
        if request.form['username'] == 'KQ':
            return redirect(url_for("admin"))
        else:
            return redirect(url_for("delivery_logger"))


@application.route("/admin", methods=['GET', 'POST'])
def get_csv_kq():

    db = pymysql.connect('knowledge-quarter-db.cnq2qddxvg55.us-east-2.rds.amazonaws.com', 'admin', 'Kn0w!3dg$_Qu&r3r', port = 3306)
    cursor = db.cursor()
    cursor.connection.commit()
    sql = '''use kq_contracts_and_logger'''
    cursor.execute(sql)

    sql = '''select * from delivery_logger'''
    cursor.execute(sql)
    data = cursor.fetchall()

    df = pd.DataFrame(list(data), columns = ['time_in','time_out',
                                          'delivery_location', 'delay', 'bound',
                                          'carrier', 'vehicle_type',
                                          'vehicle_registration_number',
                                          'personal_delivery',
                                          'department',
                                          'number_packages',
                                          'type',
                                          'size'])

    df.to_csv('outputs/your_data.csv', sep = ',' )


    return send_file('outputs/your_data.csv',
        mimetype='text/csv',
        attachment_filename='your_data.csv',
        as_attachment=True)


if __name__ == "__main__":
    # Execute only if run as a script
    application.run()
