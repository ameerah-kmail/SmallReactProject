from flask import Flask,request
from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime
from flask_cors import CORS
from database import db
from controllers.event_controller import event_bp
#from controllers.ticket_controller import ticket_bp
#from controllers.user_controller import user_bp
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://ameerah:123@localhost/event-tracker'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.app_context().push()
CORS(app)


# Initialize SQLAlchemy and Flask-Migrate
#db = SQLAlchemy(app)
db.init_app(app)
migrate = Migrate(app, db)
from models.event import Event
from models.ticket import Ticket
from models.user import User
from models.user_event import UserEvent

# Import models after initializing db to avoid circular imports
#with app.app_context():
#    db.create_all() 
       
app.register_blueprint(event_bp)
#app.register_blueprint(ticket_bp)
#app.register_blueprint(user_bp)

if __name__ == '__main__':
    app.run()