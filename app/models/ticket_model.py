from mongoengine import Document, StringField

class Ticket(Document):
    meta = {"collection": "tickets"}
    
    title = StringField(required=True)
    description = StringField(required=True)
    priority = StringField(default="medium")