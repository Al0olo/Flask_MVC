from flask import request, jsonify
from datetime import datetime
from .. import db
from .models import pos_order
from sqlalchemy import and_


def get_pos_order_By_Period_controller(fromDate,toDate):
    class Element(Base):
        __tablename__ = 'pos_order'
        id = db.Column(db.Integer, primary_key=True)
        date_order = db.Column(db.DateTime)
    
    startDate = datetime.strptime(fromDate, '%d/%m/%y')
    endDate = datetime.strptime(toDate, '%d/%m/%y')
    pos_orders = pos_order.query.filter(and_(Element.dt >= startDate, Element.dt <= endDate))
    response = []
    for pos_order in pos_orders: response.append(pos_order.toDict())
    return jsonify(response)

