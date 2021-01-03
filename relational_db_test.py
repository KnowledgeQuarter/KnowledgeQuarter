# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 14:48:12 2020

@author: Kirsch
"""

from model import Carrier1, Goods1
from __init__ import db
import numpy as np
from flask import Blueprint, redirect, render_template, request, url_for, send_file
from flask_login import login_required, logout_user, current_user, login_user
from forms import LoginForm, SignupForm
from model import db, User, Categories
import pymysql
import pandas as pd


# Blueprint Configuration
main_bp = Blueprint(
    'test_bp', __name__,
    template_folder='templates',
    static_folder='static'
)


@main_bp.route("/test")
def test():     
    for i in range(0, 50): 
        carrier = Carrier1(
                        email = np.random.randint(0,10),
                        carrier = np.random.randint(0,10) 
                    )
    
    
        db.session.add(carrier)
    db.session.commit()
    
    return render_template("admin.html")