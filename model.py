# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 12:06:26 2020

@author: Kirsch
"""

"""Database models."""
from __init__ import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model, ):
    """User account model."""

    __tablename__ = 'flasklogin-users'
    
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    name = db.Column(
        db.String(100),
        nullable=False,
        unique=False
    )
    email = db.Column(
        db.String(40),
        unique=True,
        nullable=False
    )
    password = db.Column(
        db.String(200),
        primary_key=False,
        unique=False,
        nullable=False
	)

    created_on = db.Column(
        db.DateTime,
        index=False,
        unique=False,
        nullable=True
    )
    last_login = db.Column(
        db.DateTime,
        index=False,
        unique=False,
        nullable=True
    )

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(
            password,
            method='sha256'
        )

    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User {}>'.format(self.name)

    
    
    

class Categories(db.Model):
    
    
    __tablename__ = 'visible-categories'

    
    email = db.Column(
        db.String(40),
        unique=True,
        primary_key = True
        
    )
     
    time_in = db.Column(db.Boolean, unique=False, default=True)
    
    time_out = db.Column(db.Boolean, unique=False, default=True)
    
    delivery_location = db.Column(db.Boolean, unique=False, default=True)
    
    delay = db.Column(db.Boolean, unique=False, default=True)
    
    inbound_outbound = db.Column(db.Boolean, unique=False, default=True)
    
    carrier_name = db.Column(db.Boolean, unique=False, default=True)
    
    vehicle_type = db.Column(db.Boolean, unique=False, default=True)
    
    registration_number = db.Column(db.Boolean, unique=False, default=True)
    
    personal_delivery = db.Column(db.Boolean, unique=False, default=True)
    
    department = db.Column(db.Boolean, unique=False, default=True)
    
    number_of_packages = db.Column(db.Boolean, unique=False, default=True)
    
    type_of_goods = db.Column(db.Boolean, unique=False, default=True)
    
    size_of_goods = db.Column(db.Boolean, unique=False, default=True)
    
    
    def __repr__(self):
        return '{}'.format(self.email)
    
    
    
class Carrier1(db.Model):
    
    __tablename__ = 'carriers1'

    
    id = db.Column(db.Integer, primary_key=True)


    email = db.Column(
        db.String(40),
        
    )
    
    carrier = db.Column(
        db.String(40),
        
    )
     
    
    
    def __repr__(self):
        return '{}'.format(self.email)
    
     
    
class Goods1(db.Model):
    
    
    __tablename__ = 'goods'

    id = db.Column(db.Integer, primary_key=True)


    email = db.Column(
        db.String(40),
        unique=True,
        primary_key = True
        
    )
    
    goods = db.Column(
        db.String(40),
        unique=True
        
    )
     
    
    
    def __repr__(self):
        return '{}'.format(self.email)
    
    
    


    
    
