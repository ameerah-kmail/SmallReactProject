from flask import Blueprint, request, jsonify
from models.event import Event, format_event
from datetime import datetime
from database import db

event_bp = Blueprint('event_bp', __name__)

#create an event
@event_bp.route('/event',methods =['POST'])
def create_event():
    name=request.json['name']
    description=request.json['description']
    event = Event(name=name, description=description)  # Pass both name and description
    db.session.add(event)
    db.session.commit()
    return format_event(event)

#get all events
@event_bp.route('/events',methods =['GET'])
def get_events():
    events=Event.query.order_by(Event.date.asc()).all()
    event_list=[]
    for event in events:
        event_list.append(format_event(event))
    return {'events':event_list}

#get single event
@event_bp.route('/event/<id>',methods=['GET'])
def get_event(id):
    event=Event.query.filter_by(id=id).one_or_none()
    formatted_event=format_event(event)
    return {'event':formatted_event}

#delete an event
@event_bp.route('/event/<id>',methods=['DELETE'])
def delete_event(id):
    event=Event.query.filter_by(id=id).one_or_none()
    db.session.delete(event)
    db.session.commit()
    return f'Event {id} deleted'

#update an event
@event_bp.route('/event/<id>',methods=['PUT'])
def update_event(id):
    event=Event.query.filter_by(id=id)#get list
    name=request.json['name']
    event.update(dict(name=name,date=datetime.utcnow()))
    db.session.commit()
    return{'event':format_event(event.one_or_none())}
