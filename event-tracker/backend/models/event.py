
from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime
#from app import db
from database import db 

class Event(db.Model):
    __tablename__='events'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, nullable=False ,default=datetime.utcnow)
    description = db.Column(db.String(200), nullable=True)
    tickets = db.relationship('Ticket', back_populates='event')
    users = db.relationship('UserEvent', back_populates='event')
    
    def __repr__(self):
        return f"Event: {self.name}" 
    
    def __init__(self, name, date=None, description=None):
            self.name = name
            self.date = date or datetime.utcnow()
            self.description = description
        
def format_event(event):
    return{
        "name":event.name,
        "id":event.id,
        "date":event.date
    }    