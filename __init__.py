# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 12:51:18 2020

@author: Kirsch
"""
"""Initialize app."""


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()
login_manager = LoginManager()

#Init and configure the web application
def create_app():
    application = Flask("application")

    application.config['SECRET_KEY'] = 'Kn0w!3dg$_Qu&r3r'
    application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    db.init_app(application)
    
    login_manager.init_app(application)
    
    with application.app_context():
        
        from auth import auth_bp
        from main import main_bp
        
        application.register_blueprint(auth_bp)
        application.register_blueprint(main_bp)

        
        db.create_all()

    return application