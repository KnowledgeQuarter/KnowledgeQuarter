# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 19:38:14 2020

@author: Kirsch
"""

from flask import Blueprint, redirect, render_template, flash, request, session, url_for, send_file
from flask_login import login_required, logout_user, current_user, login_user
from forms import LoginForm, SignupForm
from model import db, User, Categories
import pymysql
import pandas as pd


# Blueprint Configuration
main_bp = Blueprint(
    'main_bp', __name__,
    template_folder='templates',
    static_folder='static'
)



# Load the template for the delivery logger
@main_bp.route("/")
@login_required
def delivery_logger():
    preferences = Categories.query.filter_by(email=current_user.email).first()
    return render_template("delivery_logger.html", preferences=preferences)

# Load the template for the settings page
@main_bp.route("/settings")
def settings():
    preferences = Categories.query.filter_by(email=current_user.email).first()
    return render_template("settings.html", preferences=preferences)

# Load the template for the admin page
@main_bp.route("/admin")
def admin():
    return render_template("admin.html")





@main_bp.route("/settings", methods=['GET', 'POST'])
def which_visible():


    # Get the data from the form
    data = request.form
    data = data.to_dict()

    # Get the logging information
    value = list(data.values())

    cat = {'delivery_location' : True, 'delay': True, 'inbound_outbound': True, 'carrier_name' : True,'vehicle_type': True, 'registration_number': True,
    'personal_delivery': True, 'department': True, 'number_of_packages': True, 'type_of_goods': True, 'size_of_goods': True}

    key = list(cat.keys())

    for i in key:
        if i not in value:
            cat[i] = False


    print(cat)

    user_pref = Categories.query.filter_by(email=current_user.email).first()

    print(user_pref.size_of_goods)

    user_pref.delivery_location = cat["delivery_location"]
    user_pref.delay = cat["delay"]
    user_pref.inbound_outbound = cat["inbound_outbound"]
    user_pref.carrier_name = cat["carrier_name"]
    user_pref.vehicle_type = cat["vehicle_type"]
    user_pref.registration_number = cat["registration_number"]
    user_pref.personal_delivery = cat["personal_delivery"]
    user_pref.department = cat["department"]
    user_pref.number_of_packages = cat["number_of_packages"]
    user_pref.type_of_goods = cat["type_of_goods"]
    user_pref.size_of_goods = cat["size_of_goods"]

    print(user_pref.size_of_goods)


    db.session.commit()

    return redirect(url_for("main_bp.form"))



# Load the template for the settings page
@main_bp.route("/settings", methods=['GET', 'POST'])
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
@main_bp.route("/", methods=['GET', 'POST'])
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
    return redirect(url_for("main_bp.form"))


@main_bp.route("/logout")
@login_required
def logout():
    """User log-out logic."""
    logout_user()
    return redirect(url_for('auth_bp.login'))

@main_bp.route("/", methods=['GET', 'POST'])
def login():
    # Get the data from the form
    if request.method == 'POST':
        if request.form['username'] == 'KQ':
            return redirect(url_for("main_bp.admin"))
        else:
            return redirect(url_for("main_bp.delivery_logger"))


@main_bp.route("/admin", methods=['GET', 'POST'])
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
