from mongoengine import *

class Service(Document):
    name = StringField()
    yob = IntField()
    gender = IntField()
    height = StringField()
    phone = StringField()
    address = StringField()
    status = BooleanField()
    description = StringField()
    image = StringField()
    measurements = StringField()
