from sqlalchemy import inspect
from datetime import datetime
from flask_validator import ValidateEmail, ValidateString, ValidateCountry
from sqlalchemy.orm import validates

from .. import db # from __init__.py

class pos_order(db.Model):  
    id              =   db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    sequence_number =   db.Column(db.Integer)
    session_id      =   db.Column(db.Integer)
    name            =   db.Column(db.String())
    state           =   db.Column(db.String())
    pos_reference   =   db.Column(db.String())
    amount_tax      =   db.Column(db.Numeric)
    amount_total    =   db.Column(db.Numeric)
    amount_paid     =   db.Column(db.Numeric)
    amount_return   =   db.Column(db.Numeric)
    currency_rate   =   db.Column(db.Numeric)
    tip_amount      =   db.Column(db.Numeric) 
    date_order      =   db.Column(db.DateTime(timezone=False),defaulte=datetime.now)
    create_date     =   db.Column(db.DateTime(timezone=False),defaulte=datetime.now)
    write_date      =   db.Column(db.DateTime(timezone=False),defaulte=datetime.now)
    employee_id     =   db.Column(db.Integer)
    cashier         =   db.Column(db.String())
    order_refunded  =   db.Column(db.String())
    customer_count  =   db.Column(db.String())
    branch_id       =   db.Column(db.Integer)
    lines           =   db.relationship("pos_order_line", back_populates='pos_order')