from dataclasses import fields
from models.contact import Contact
from utils.ma import ma

class ContactSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Contact
        fields = ("id","fullname","email","phone")
        