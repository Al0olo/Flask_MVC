from sqlalchemy import inspect
from datetime import datetime
from flask_validator import ValidateEmail, ValidateString, ValidateCountry
from sqlalchemy.orm import validates

from .. import db # from __init__.py

class pos_order_line(db.Model):
    id                      =   db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    company_id              =   db.Column(db.Integer)
    product_id              =   db.Column(db.Integer)
    order_id                =   db.Column(db.Integer, db.ForeignKey("pos_order.id"))
    refunded_orderline_id   =   db.Column(db.Integer)
    create_uid              =   db.Column(db.Integer)
    write_uid               =   db.Column(db.Integer)
    name                    =   db.Column(db.String())
    notice                  =   db.Column(db.String())
    full_product_name       =   db.Column(db.String())
    customer_note           =   db.Column(db.String)
    price_unit              =   db.Column(db.Numeric)
    qty                     =   db.Column(db.Numeric)
    price_subtotal          =   db.Column(db.Numeric)
    price_subtotal_incl     =   db.Column(db.Numeric)
    total_cost              =   db.Column(db.Numeric)
    discount                =   db.Column(db.Numeric)
    is_total_cost_computed  =   db.Column(db.Boolean)
    create_date             =   db.Column(db.DateTime(timezone=False),defaulte= datetime.now)
    write_date              =   db.Column(db.DateTime(timezone=False),defaulte= datetime.now)
    price_extra             =   db.Column(db.Numeric)
    sale_order_origin_id    =   db.Column(db.Integer)
    sale_order_line_id      =   db.Column(db.Integer)
    down_payment_details    =   db.Column(db.String)
    reward_id               =   db.Column(db.Integer)
    coupon_id               =   db.Column(db.Integer)
    reward_identifier_code  =   db.Column(db.String())
    is_reward_line          =   db.Column(db.Boolean)
    points_cost             =   db.Column(db.Numeric)
    note                    =   db.Column(db.String())
    uuid                    =   db.Column(db.String())
    mp_skip                 =   db.Column(db.Boolean)
    is_combo                =   db.Column(db.Boolean)
    pos_order               =   db.relationship("pos_order", back_populates="pos_order_line")