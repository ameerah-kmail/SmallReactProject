from flask_sqlalchemy import SQLAlchemy
from app import db

class Ticket(db.Model):
    __tablename__ = 'tickets'

    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'), nullable=False)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    event = db.relationship('Event', back_populates='tickets')

    def __repr__(self):
        return f"<Ticket {self.id} for Event {self.event_id}>"