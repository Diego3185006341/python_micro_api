from flask import Blueprint, jsonify, request
from routes.schemas import ContactSchema
from utils.db import db


from models.contact import Contact

contacts = Blueprint('contacts',__name__)

@contacts.route("/")
def home():
    contact_schema = ContactSchema(many=True)
    registros = Contact.query.all()
    return jsonify({"code":00,"response":contact_schema.dump(registros)})



@contacts.route("/new",methods=['POST'])
def new():
    json_request = request.get_json()
    new_contact = Contact(json_request["fullname"],json_request["email"],json_request["phone"])
    db.session.add(new_contact)
    db.session.commit()
    return jsonify({"code":00,"response":"create register"})

@contacts.route("/edit",methods=['POST'])
def edit():
    json_request = request.get_json()
    id = json_request["id"]
    contact = Contact.query.get(id)
    contact.email = json_request["email"]
    contact.fullname = json_request["fullname"]
    contact.phone = json_request["phone"]
    db.session.commit()
    return jsonify({"code":00,"response":"update register"})

@contacts.route("/delete/<id>")
def delete(id):
    contact = Contact.query.get(id)
    db.session.delete(contact)
    db.session.commit()
    return jsonify({"code":00,"response":"delete register"})