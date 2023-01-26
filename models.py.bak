
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

import datetime



db = SQLAlchemy()


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    WebID = db.Column('WebID', db.String(100))
    InvoiceNumber = db.Column('InvoiceNumber', db.String(20))
    Institution = db.Column('Institution', db.String(50))
    InvoiceDate = db.Column('InvoiceDate', db.Date, default=datetime.datetime.now().date)
    Instructor = db.Column('Instructor', db.String(50))
    AdminKey = db.Column('AdminKey', db.String(20))
    Email = db.Column('Email', db.String(50))
    Usercode = db.Column('Usercode', db.String(20))
    AdminCount = db.Column(db.Integer)
    site_license_checkbox = db.Column('site_license_checkbox', db.String(5))
    site_license_date = db.Column('site_license_date', db.Date, default=datetime.datetime.now().date)
    reflection_checkbox = db.Column('reflection_checkbox', db.String(5))
    custom_message_checkbox = db.Column('custom_message_checkbox', db.String(5))
    custom_message = db.Column('custom_message', db.Text)
    show_extra_questions = db.Column('show_extra_questions', db.String(5))
    Q91 = db.Column('Q91', db.String(200))
    Q92 = db.Column('Q92', db.String(200))


    def __repr__(self):
        return f'''<Users (
            WebID: {self.WebID}
            InvoiceNumber: {self.InvoiceNumber}
            Institution: {self.Institution}
            InvoiceDate: {self.InvoiceDate}
            Instructor: {self.Instructor}
            Email: {self.Email}
            Usercode: {self.Usercode}
            AdminCount: {self.AdminCount}
            site_license_checkbox: {self.site_license_checkbox}
            site_license_date: {self.site_license_date}
            reflection_checkbox: {self.reflection_checkbox}
            custom_message_checkbox: {self.custom_message_checkbox}
            custom_message: {self.custom_message}
            show_extra_questions: {self.show_extra_questions}
            Q91: {self.Q91}
            Q92: {self.Q92}
        )'''

       