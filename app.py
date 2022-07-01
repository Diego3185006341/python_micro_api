from flask import Flask
from routes.contacts import contacts
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.register_blueprint(contacts)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:admin123@localhost/contactsdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


SQLAlchemy(app)
Marshmallow(app)



